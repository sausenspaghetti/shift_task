import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_HOST = os.getenv('SQLALCHEMY_DATABASE_HOST') or 'localhost'
    SQLALCHEMY_DATABASE_PASSWORD = os.getenv('SQLALCHEMY_DATABASE_PASSWORD') or '123456'
    SQLALCHEMY_DATABASE_USER = os.getenv('SQLALCHEMY_DATABASE_USER') or 'postgres'
    SQLALCHEMY_DATABASE_NAME = os.getenv('SQLALCHEMY_DATABASE_NAME') # or 'fastapi_tutorial'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or 'postgresql'

    SQLALCHEMY_DATABASE_URL = "{uri}://{username}:{psw}@{host}/{db_name}".format(
        uri=SQLALCHEMY_DATABASE_URI,
        username=SQLALCHEMY_DATABASE_USER,
        psw=SQLALCHEMY_DATABASE_PASSWORD,
        host=SQLALCHEMY_DATABASE_HOST,
        db_name=SQLALCHEMY_DATABASE_NAME
    )


class DevConfig(Config):
    pass


config = {
    'default': Config,
    'develop': DevConfig
}
