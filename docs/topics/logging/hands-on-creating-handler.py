import logging

logger = logging.getLogger("app")

file_handler = logging.FileHandler("app.log")

logger.addHandler(file_handler)

logger.warning("hello")