import logging
import os

LOG_PATH = "Service.log"


# SETUP logger
log_format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class DevelopmentConfig():
    port = 5000
    debug = True
    log_path = "Service.log"
    documentation_path = "/swagger-ui"


class ProductionConfig():
    port = 8000
    debug = False
    log_path = "Service.log"
    documentation_path = None


configurations = {
    "dev":  DevelopmentConfig(),
    "prod": ProductionConfig()}

env_var_name = "Service_CONFIG"
env_var_default = "dev"

environment = os.environ.get(env_var_name, env_var_default)
print(env_var_name)
print(environment)

config = configurations[environment]



#postgres_local_base = os.environ['DATABASE_URL']
#postgres_local_base = os.environ['DATABASE_URL']
postgres_db = {'drivername': 'postgres',
               'username': 'unicorn_user',
               'password': 'magical_password',
               'host': 'localhost',
               'port': 5432,
               'database': 'rainbow_database'}

#url = URL(**postgres_db)
url = "EMPTY_URL"



basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = url
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = url
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = url


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
