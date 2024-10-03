import logging

# Create a logger
logger = logging.getLogger(__name__)

# Create a stream handler
console_handler = logging.StreamHandler()

# Set logger attributes
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)

# Log a message
logger.info("This is an info message")
logger.debug("This is a debug message")