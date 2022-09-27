import configparser
import os
from pathlib import Path

SERVICE_NAME = "commodity-histogram"

_CONFIG_PATH_ORDER = [os.path.dirname(os.path.abspath(__file__)) + os.path.sep + '.' + os.path.sep + 'config.ini',
                      os.path.dirname(os.path.abspath(__file__)) + os.path.sep + '..' + os.path.sep + 'config.ini']
CONFIG_PATH = None

for p in _CONFIG_PATH_ORDER:
    if os.path.isfile(p):
        CONFIG_PATH = p
        break

if CONFIG_PATH is None:
    print("Unable to find config.ini")
    exit(1)


_config = configparser.ConfigParser()
_config.read(CONFIG_PATH)

LOG_DIR = _config['default']['log_dir']

try:
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
except Exception as e:
    print("Unable to utilize logging path: " + CONFIG_PATH)


SQL_DB_HOSTNAME     = _config['sql-database']['hostname']
SQL_DB_PORT         = int(_config['sql-database']['port'])
SQL_DB_DBNAME       = _config['sql-database']['dbname']
SQL_DB_USERNAME     = _config['sql-database']['username']
SQL_DB_PASSWORD     = _config['sql-database']['password']

REST_PORT = _config['rest']['port']
