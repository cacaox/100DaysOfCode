# 設定の読み書き
import configparser


config = configparser.ConfigParser()
config['DEFAULUT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': '80'
}
config['db_server'] = {
    'port': 3306
}
with open('config.ini', 'w') as config_file:
    config.write(config_file)