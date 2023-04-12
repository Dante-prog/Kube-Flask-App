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
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:nd3Ruzsq4xa.RfHMQhkJmNUV@flask-app-post-db.cdjokhunziur.us-east-1.rds.amazonaws.com:5432/postgres'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
