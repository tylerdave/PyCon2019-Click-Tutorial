import click
import pytoml

from codecs import open
from pathlib import Path

APP_NAME = 'Click Tutorial'
APP_DIR = click.get_app_dir(APP_NAME)

def state_file_path():
    return Path(APP_DIR, 'tutorial-state.toml')

def save(new_state):
    with open(state_file_path(), mode='w', encoding='utf-8') as statefile:
        pytoml.dump(new_state, statefile)

def load():
    with open(state_file_path(), mode='r', encoding='utf-8') as statefile:
        return pytoml.load(statefile)

def initialize():
    if not Path(APP_DIR).exists():
        Path(APP_DIR).mkdir(parents=True, exist_ok=True) 
    default_state = {
        'lessons': {
        },
    }
    save(default_state)

def is_initialized():
    try:
        state = load()
    except FileNotFoundError:
        return False
    except:
        raise
    if 'lessons' in state:
        return True
    else:
        return False