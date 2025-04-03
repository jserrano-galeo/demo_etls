from dataclasses import dataclass
from time import sleep
from loguru import logger
from {{ cookiecutter.project_name }}.models import InputDocument
from {{ cookiecutter.project_name }}.settings import CommonSettings, TaskSettings


@dataclass
class BasicTask:
    """
    Basic Task
    """
    def __init__(self, common_settings: CommonSettings, task_settings: TaskSettings):
        self.common_settings = common_settings
        self.task_settings = task_settings

    def run(self):
        input_document = InputDocument(url=self.task_settings.URL)
        logger.info(f"Starting task for {input_document}")
        sleep(5000)
        return self
