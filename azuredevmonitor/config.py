'''
Makes it easy to read a config file
'''

from configparser import ConfigParser
from pathlib import Path
import os

class Config():

    instance = None
    config_file='azuredevpy.ini'

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = AppConfig()

        return cls.instance
        
    def __init__(self):
        
        #paths to check for the config file
        self.CONFIG_PATHS=[
            os.path.join(str(Path.home()), self.config_file),
            os.path.join(os.getcwd(), self.config_file)
        ]

        #exit if there is no config file found
        if not self.config_exists():
            return

        #make the config parser available for other functions
        self.parser = ConfigParser()
        self.parser.read(self.get_config())
        

    def get_config(self):
        '''return the first config file found'''

        files = [x for x in self.CONFIG_PATHS if os.path.exists(x)]

        if files is None or len(files) == 0: return None

        return files[0]
        
    def config_exists(self):
        '''check if the config exists'''
        
        return self.get_config() is not None

    def get_setting(self, section="DEFAULT", my_setting=None):
        '''get a value from the config'''

        if my_setting is None: return

        try:        
            ret = self.parser.get(section, my_setting)
        except Exception:
            ret = None
        return ret

    def get_default_setting(self, my_setting):
        '''get a default value from the config'''
        
        if my_setting is None: return

        return self.get_setting("DEFAULT", my_setting)

def get_instance():
    return Config()