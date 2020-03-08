import configparser

# Read config from file
def get_config():
    setupconfig = configparser.ConfigParser()
    setupconfig.read('setup.cfg')
    config = {}
    config['bike'] = 'TE310'
    config['orientation'] = setupconfig['Parameters']['orientation']
    config['language'] = setupconfig['Parameters']['language']
    config['theme'] = setupconfig['Parameters']['theme']
    return config
