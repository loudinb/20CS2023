import logging

# TODO-1: Create LevelFilter Class.  Implement the filter method
#         that only allows log records with a level of WARNING or
#         higher to be processed.
class CustomFilter(logging.Filter):

    def __init__(self, name):
        self.name = name

    def filter(self, record):
        record.name = self.name
        return True

formatter = logging.Formatter(
    '%(asctime)s - %(message)s - [%(name)s]'
    )

# TODO-2: Create a Logger named app and assign it to the logger variable
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)


file_handler = logging.FileHandler("app.log")
file_handler.addFilter(CustomFilter("Alice"))
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


logger.critical("This is a critical message")
logger.error("This is an error message")
logger.warning("This is a warning message")
logger.info("This is a info message")
logger.debug("This is a debug message")