from git import Repo
# pip install git-python
import yaml

update_times = {}

with open("update_me.yaml", 'r') as stream:
    try:
        update_times = {'UPDATE_TIMES':int(yaml.safe_load(stream)['UPDATE_TIMES']) + 1}
    except yaml.YAMLError as exc:
        print(exc)

with open("update_me.yaml", 'w') as stream:
    yaml.dump(update_times, stream, default_flow_style=False)
repo = Repo('.')  # if repo is CWD just do '.'
repo.index.add(['update_me.yaml','main.py'])
repo.index.commit(f'Updated {update_times["UPDATE_TIMES"]} times')
origin = repo.remote('origin')
origin.push()