import configparser
import os
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")
class ReadFile:
    data_path = data_path
    ini_path = ini_path

    def read_data(self):
        with open(self.data_path, encoding="utf8") as f:
            data = yaml.safe_load(f)
        return data


if __name__ == '__main__':

    # print(os.path.realpath(__file__))
    # print(data_path)
    # print(ini_path)
    print(ReadFile().read_data()['host']['host_url'])
    print(ReadFile().read_data()['userinfo']['userid'])

