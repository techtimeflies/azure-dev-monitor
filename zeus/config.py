import configparser
import os

config_file = os.path.join(os.getcwd(), 'config.ini')

parser = configparser.ConfigParser()
parser.sections()
parser.read(config_file)
