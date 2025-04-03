from pydantic_settings import BaseSettings
from starlette.config import Config


config = Config()


class CommonSettings(BaseSettings):
    SERVICE_NAME: str = config("SERVICE_NAME", default="{{ cookiecutter.project_name }}")
    VERSION: str = config("VERSION", default="0.0.0")


class TaskSettings(BaseSettings):    
    CONFIG_URL: str = config("VERSION", default="s3://path/to/dataset") 
