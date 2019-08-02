from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # Create parser
    parser = ConfigParser()
    # Read config file
    parser.read(filename)

    # Get section
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            key, value = param
            db[key]=value
    else:
        raise Exception("Section {0} not found in {1} file".format(section, filename))
    return db
