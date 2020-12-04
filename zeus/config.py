'''
Makes it easy to read a config file
'''

from configparser import ConfigParser
from pathlib import Path
import os


config_file='zeus.ini'
CONFIG_PATHS=[
    os.path.join(str(Path.home()), config_file),
    os.path.join(os.getcwd(), config_file)
]

def get_config():
    '''return the first config file found'''

    files = [x for x in CONFIG_PATHS if os.path.exists(x)]

    if files is None or len(files) == 0: return None

    return files[0]
    
def config_exists():
    return get_config() is not None

def get_setting(section="DEFAULT", my_setting=None):

    if my_setting is None: return

    parser = ConfigParser()
    parser.read(get_config())
    try:        
        ret = parser.get(section, my_setting)
    except Exception:
        ret = None
    return ret

def get_default_setting(my_setting):
    if my_setting is None: return

    return get_setting("DEFAULT", my_setting)

