import yaml
from main import DIR, ENVIRON


class YamlRead:
    @staticmethod
    def env_config():
        with open(file=f'{DIR}/config/env/{ENVIRON}/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def data_config():
        with open(file=f'{DIR}/config/data/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    pass
    # # print(dataConfig)
    # mustKey = dataConfig['mustKeys']  # 值为列表
    # # print(mustKey)
    # key = mustKey['startindex']
    # print(key)