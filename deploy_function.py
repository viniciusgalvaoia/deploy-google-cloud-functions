import argparse
import io
import logging
import pathlib
import subprocess
from zipfile import ZipFile, ZipInfo

from google.cloud import storage
from rich.logging import RichHandler
from rich.traceback import install

FORMAT = "[%(levelname)s] [%(message)s]"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%Y-%m-%d %H:%M:%S]",
    handlers=[RichHandler(show_level=False, show_path=False)],
)
install()
logger = logging.getLogger("main")


def compress_folder(folder_dir: str) -> io.BytesIO:
    logger.info(f"Compressing folder {folder_dir}")
    source_dir = pathlib.Path(folder_dir)
    archive = io.BytesIO()
    with ZipFile(archive, "w") as zip_archive:
        for file_path in source_dir.iterdir():
            with open(file_path, "r") as file:
                zip_entry_name = file_path.name
                zip_file = ZipInfo(zip_entry_name)
                zip_archive.writestr(zip_file, file.read())

    archive.seek(0)
    return archive


def upload_zipfile_to_gcs(
    zipfile: str, client: str, bucket_name: str, object_name: str
):
    logger.info(f"Uploading file {object_name} to {bucket_name} bucket")
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_file(zipfile, content_type="application/x-zip-compressed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update cloud functions")
    parser.add_argument(
        "source",
        help="Source directory with main.py and requirements.txt files",
    )
    parser.add_argument("function", help="Function name to be updated")
    args = parser.parse_args()
    source_directory = args.source
    function_name = args.function
    logger.info(f"Updating {function_name} function using files on {source_directory}")
    object_name = f"{function_name}.zip"
    bucket_name = "humane-cloud-functions"
    compressed_folder = compress_folder(source_directory)
    storage_client = storage.Client()
    upload_zipfile_to_gcs(compressed_folder, storage_client, bucket_name, object_name)
    command = (
        f"gcloud functions deploy {function_name} "
        f"--source gs://{bucket_name}/{object_name} "
        "--entry-point start "
        "--runtime python39 "
        "--trigger-http "
        "--allow-unauthenticated "
    )
    subprocess.run(
        command,
        shell=True,
    )
