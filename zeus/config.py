from configparser import ConfigParser
import os


config_file=os.path.join(os.getcwd(), 'config.ini')

def get_setting(section="DEFAULT", my_setting=None):

    if my_setting is None: return

    parser = ConfigParser()
    parser.read(config_file)
    try:        
        ret = parser.get(section, my_setting)
    except Exception:
        ret = None
    return ret

def config_exists():
    return os.path.exists(config_file)

def get_default_setting(my_setting):
    if my_setting is None: return

    return get_setting("DEFAULT", my_setting)