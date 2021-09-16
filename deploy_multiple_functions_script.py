import subprocess

source_dir_and_functions_dict = {
    "C:\humane\\talentcards\cloud_functions\\groups_to_bq": "talentcard-groups-to-bq",
    "C:\humane\\talentcards\cloud_functions\\groups_to_landing_zone": "talentcard-groups-to-landing-zone",
    "C:\humane\\talentcards\cloud_functions\\reports_to_bq": "talentcard-reports-to-bq",
    "C:\humane\\talentcards\cloud_functions\\reports_to_landing_zone": "talentcard-reports-to-landing-zone",
    "C:\humane\\talentcards\cloud_functions\\sets_to_bq": "talentcard-sets-to-bq",
    "C:\humane\\talentcards\cloud_functions\\sets_to_landing_zone": "talentcard-stalentcard-sets-to-landing-zone",
    "C:\humane\\talentcards\cloud_functions\\users_engagement_to_bq": "talentcard-users-engagement-to-bq",
    "C:\humane\\talentcards\cloud_functions\\users_to_bq": "talentcard-users-to-bq",
    "C:\humane\\talentcards\cloud_functions\\users_to_landing_zone": "talentcard-users-to-landing-zone",
    "C:\humane\\talentcards\cloud_functions\\talentcards-manual-users-extraction-to-gbq": "talentcards-manual-users-extraction-to-gbq",
}

for source_dir, function_name in source_dir_and_functions_dict.items():
    command = f"python deploy_function.py {source_dir} {function_name}"
    subprocess.run(
        command,
        shell=True,
    )
