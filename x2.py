import logging
from logging.handlers import TimedRotatingFileHandler

file_handler = TimedRotatingFileHandler(
    "app.log", when="midnight", interval=1, backupCount=5
    )

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

logger.warning("This is a warning message")