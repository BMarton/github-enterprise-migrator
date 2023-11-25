import os
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-r", "--repo", required=True,
                help="name of the repo")
args = vars(ap.parse_args())

import_pat = ""
export_pat = ""


source_org = ""
target_org = ""
admin_user = ""
android_team = ""
ios_team = ""


def command(text):
    os.system(text)


def migrate_project(project):
    # project variables
    source_repo = project
    target_repo = project
    # Set impot and export and default tokens
    set_env_variables()
    # Migrate the repo
    command(
        "gh gei migrate-repo --github-source-org {} --source-repo {} --github-target-org {} --target-repo {}".format(
            source_org,
            source_repo,
            target_org,
            target_repo))
    # Add an Admin
    command("gh api --method=PUT repos/{}/{}/collaborators/{} -f permission=admin".format(target_org, target_repo, admin_user))
    # Add Maintainer Teams
    command("gh api -X PUT /orgs/{}/teams/{}/repos/{}/{} -f permission=maintain".format(target_org, android_team, target_org,
                                                                                        target_repo))
    command(
        "gh api -X PUT /orgs/{}/teams/{}/repos/{}/{} -f permission=maintain".format(target_org, ios_team, target_org,
                                                                                    target_repo))
    # Change Visibility to Internal
    command("gh api -X PATCH repos/{}/{} -fvisibility=internal".format(target_org, target_repo))
    # Archive old repository


def set_env_variables():
    os.environ["GH_PAT"] = import_pat
    os.environ["GH_SOURCE_PAT"] = export_pat
    os.environ["GH_TOKEN"] = import_pat


repo = args['repo']
# Read the file line by line
if ".txt" in repo:
    # Using readlines()
    file = open(repo, 'r')
    Lines = file.read().splitlines()

    # Strips the newline character
    for line in Lines:
        migrate_project(line)
        print("---------------------------------------------------------------------------------------------------------")
else:
    migrate_project(repo)
