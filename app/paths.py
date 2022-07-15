import os


APP_PATH = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(APP_PATH, 'db', 'netflix.db')

CONFIGS_PATH = os.path.join(APP_PATH, 'configs')
DEV_CONFIG_FILE_PATH = os.path.join(CONFIGS_PATH, 'dev_config.py')
PROD_CONFIG_FILE_PATH = os.path.join(CONFIGS_PATH, 'prod_config.py')

DATA_PATH = os.path.join(APP_PATH, 'data')

STATIC_PATH = os.path.join(APP_PATH, 'blueprints', 'static')
