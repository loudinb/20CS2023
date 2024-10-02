import logging
from user import User

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def main():
    logger = logging.getLogger(__name__)
    logger.info('Starting the application')
    
    user = User('John')
    user.greet()
    user.farewell()
    
    logger.info('Application finished')

if __name__ == "__main__":
    setup_logging()
    main()