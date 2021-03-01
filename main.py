import yaml
from datetime import datetime
from git import Repo
# pip install git-python

FILE_TO_COMMIT_NAME: str = 'update_me.yaml'

# read file contents to figure out how many times we commited.
with open(FILE_TO_COMMIT_NAME, 'r') as file:
    YAML_FILE = {
        'UPDATE_TIMES':int(yaml.safe_load(file)['UPDATE_TIMES']) + 1,
        'LAST_UPDATE':datetime.now().strftime("%A %B %d %Y at %X%p")
                 }
# Write new contents to file to be commited.
with open(FILE_TO_COMMIT_NAME, 'w') as file:
    yaml.dump(YAML_FILE, file, default_flow_style=False, sort_keys=True)
repo = Repo('.')  # if repo is CWD just do '.'
repo.index.add([FILE_TO_COMMIT_NAME])
repo.index.commit(f'Updated {YAML_FILE["UPDATE_TIMES"]} times')
origin = repo.remote('origin')
origin.push()