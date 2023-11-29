# Python Script for GitHub Enterprise Bulk Migration

Script accepts one or more projects as a parameter and migrate them between organization, adds one administrator and two teams as maintainers. Easily can be modified to serve other purposes to manage git repos.

## Prerequisites
The scipt uses the following tools:
- Python 3
- [GitHub CLI](https://github.com/cli/cli#installation)
- [GitHub Enterprise Importer (GEI)](https://github.com/github/gh-gei)
- [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28)

## Setup

Edit migrator.py

```
# import token
import_pat = ""
# export token
export_pat = ""

# exporter org name
source_org = ""
# importer org name
target_org = ""
# admin user to add to the repo(s)
admin_user = ""
# teams to add to the repo(s)
android_team = ""
ios_team = ""
```

## Using the Migrator

To use migrator.py for one repository, run the command

> `python migrator.py -r "repository_name"`

To use migrator.py for batch migration, run the command

> `python migrator.py -r "projects.txt"`

#### Example projects.txt

```
repository_name1
repository_name2
repository_name3
...
..
.
```