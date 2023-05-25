import configparser

config = configparser.ConfigParser()
config.sections()
config.read('settings.ini')
config.sections()

if 'DEFAULT' in config:
    directory = config['DEFAULT']['dir']
    file_type = config['DEFAULT']['file type']
    recursive = config['DEFAULT']['recursive']

if 'server params' in config:
    Port = config['server params']['Port']
    address = config['server params']['address']
    user = config['server params']['user']
    password = config['server params']['password']

