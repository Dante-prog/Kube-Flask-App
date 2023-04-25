import os
import secrets
from dotenv import load_dotenv
load_dotenv()
Secret_key = secrets.token_hex(16)

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = Secret_key

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://linpostgres:2K63^1hgvJKPRdUC@lin-20237-7125-pgsql-primary.servers.linodedb.net:5432/postgres'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
