import configparser
import os
from pathlib import Path

SERVICE_NAME = "commodity-histogram"

__CONFIG_PATH_ORDER = [os.path.dirname(os.path.abspath(__file__)) + os.path.sep + '.' + os.path.sep + 'config.ini',
                      os.path.dirname(os.path.abspath(__file__)) + os.path.sep + '..' + os.path.sep + 'config.ini']
CONFIG_PATH = None

for p in __CONFIG_PATH_ORDER:
    if os.path.isfile(p):
        CONFIG_PATH = p
        break

if CONFIG_PATH is None:
    print("Unable to find config.ini")
    exit(1)


__config = configparser.ConfigParser()
__config.read(CONFIG_PATH)

LOG_DIR = __config['default']['log_dir']

try:
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
except Exception as e:
    print("Unable to utilize logging path: " + CONFIG_PATH)


SQL_DB_HOSTNAME     = __config['sql-database']['hostname']
SQL_DB_PORT         = int(__config['sql-database']['port'])
SQL_DB_DBNAME       = __config['sql-database']['dbname']
SQL_DB_USERNAME     = __config['sql-database']['username']
SQL_DB_PASSWORD     = __config['sql-database']['password']

REST_PORT = __config['rest']['port']
