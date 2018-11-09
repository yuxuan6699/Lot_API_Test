import os
import configparser
import getpathInfo

config_path = os.path.join(getpathInfo.get_Path(), 'config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='GB18030')

class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

if __name__ == '__main__':
    print(config_path)
    print(ReadConfig().get_http('baseurl'))

