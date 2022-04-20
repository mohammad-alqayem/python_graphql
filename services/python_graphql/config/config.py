import os

DB_NAME = os.environ['db_name']
DB_USERNAME = os.environ['db_username']
DB_PWD = os.environ['db_password']
DB_IP = os.environ['db_ip_address']

DB_URL = f"postgresql://{DB_USERNAME}:{DB_PWD}@{DB_IP}:5432/{DB_NAME}"
