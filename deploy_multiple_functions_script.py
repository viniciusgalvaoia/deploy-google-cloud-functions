import subprocess

source_dir_and_functions_dict = {
    "C:\humane\\talentcards\cloud_functions\\groups_to_bq": "groups_to_bq",
    "C:\humane\\talentcards\cloud_functions\\groups_to_landing_zone": "groups_to_landing_zone",
    "C:\humane\\talentcards\cloud_functions\\reports_to_bq": "reports_to_bq",
    "C:\humane\\talentcards\cloud_functions\\reports_to_landing_zone": "reports_to_landing_zone",
    "C:\humane\\talentcards\cloud_functions\\sets_to_bq": "sets_to_bq",
    "C:\humane\\talentcards\cloud_functions\\sets_to_landing_zone": "sets_to_landing_zone",
    "C:\humane\\talentcards\cloud_functions\\users_engagement_to_bq": "users_engagement_to_bq",
    "C:\humane\\talentcards\cloud_functions\\users_to_bq": "users_to_bq",
    "C:\humane\\talentcards\cloud_functions\\users_to_landing_zone": "users_to_landing_zone",
    "C:\humane\\talentcards\cloud_functions\\talentcards-manual-users-extraction-to-gbq": "manual-users-extraction-to-gbq",
}

for source_dir, function_name in source_dir_and_functions_dict.items():
    command = f"python deploy_function.py {source_dir} {function_name}"
    subprocess.run(
        command,
        shell=True,
    )
