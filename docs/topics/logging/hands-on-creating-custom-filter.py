import logging

# TODO-1: Create LevelFilter Class.  Implement the filter method
#         that only allows log records with a level of WARNING or
#         higher to be processed.
class LevelFilter(logging.Filter):

    def filter(self, record):
        return record.levelno >= logging.WARNING

# TODO-2: Create a Logger named app and assign it to the logger variable
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# TODO-3: Create a StreamHandler and assign it to the console_handler variable
console_handler = logging.StreamHandler()

# TODO-4: Create a FileHandler using app.log for the file name
#         and assign it to the file_handler variable
file_handler = logging.FileHandler("app.log")

# TODO-5: Add the LevelFilter to the file_handler using the addFilter method
file_handler.addFilter(LevelFilter())

# TODO-6: Add the console_handler logger using the addHandler method
logger.addHandler(console_handler)

# TODO-7: Add the file_handler logger using the addHandler method
logger.addHandler(file_handler)

logger.critical("This is a critical message")
logger.error("This is an error message")
logger.warning("This is a warning message")
logger.debug("This is a debug message")
