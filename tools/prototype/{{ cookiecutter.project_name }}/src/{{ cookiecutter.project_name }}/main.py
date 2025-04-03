from {{ cookiecutter.project_name }}.settings import CommonSettings, TaskSettings
from {{ cookiecutter.project_name }}.tasks import BasicTask
from loguru import logger


def main():
    common_settings = CommonSettings()
    task_settings = TaskSettings()
    logger.info(f"starting application: {common_settings.SERVICE_NAME}")
    task = BasicTask(common_settings, task_settings)
    task.run()


if __name__ == "__main__":
    main()
