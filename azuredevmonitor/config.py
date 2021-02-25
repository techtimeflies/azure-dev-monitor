"""
Makes it easy to read a config file
"""

from configparser import ConfigParser
from pathlib import Path
import os
import logging

class Config:

    instance = None
    config_file = 'azuredevmonitor.ini'
    log_dir = os.path.join(os.getcwd(), "logs")

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Config()

        return cls.instance

    def __init__(self):
        
        # paths to check for the config file
        self.CONFIG_PATHS=[
            os.path.join(str(Path.home()), self.config_file),
            os.path.join(os.getcwd(), self.config_file)
        ]

        # exit if there is no config file found
        if not self.config_exists():
            return

        # make the config parser available for other functions
        self.parser = ConfigParser()
        self.parser.read(self.get_config())

        self.configure_logging()

    def configure_logging(self):
        logger = logging.getLogger('azuredevmonitor')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages

        try:
            os.mkdir(self.log_dir)
        except Exception:
            pass

        fh = logging.FileHandler(os.path.join(self.log_dir, self.get_setting("LOGGING", "FILE_NAME")))
        fh.setLevel(self.get_setting("LOGGING", "LEVEL"))
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)

    def get_config(self):
        """return the first config file found"""

        files = [x for x in self.CONFIG_PATHS if os.path.exists(x)]

        if files is None or len(files) == 0: return None

        return files[0]
        
    def config_exists(self):
        """check if the config exists"""
        
        return self.get_config() is not None

    def get_setting(self, section="DEFAULT", my_setting=None):
        """get a value from the config"""

        if my_setting is None: return

        try:        
            ret = self.parser.get(section, my_setting)
        except KeyError:
            ret = None
        return ret

    def get_default_setting(self, my_setting):
        """get a default value from the config"""
        
        if my_setting is None: return

        return self.get_setting("DEFAULT", my_setting)

def get_instance():
    return Config()