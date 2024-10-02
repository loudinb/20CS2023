import logging

logger = logging.getLogger(__name__)

class User:
    def __init__(self, name):
        self.name = name
        logger.info(f'User created: {self.name}')

    def greet(self):
        logger.debug(f'Greeting user: {self.name}')
        print(f'Hello, {self.name}')

    def farewell(self):
        logger.debug(f'Saying goodbye to user: {self.name}')
        print(f'Goodbye, {self.name}')
