import logging

app_logger = logging.getLogger('app')

def main():
    app_logger.warning("warning logged to app logger")

    child_logger = logging.getLogger('bob.child')
    
    child_logger.warning(f"warning logged to child logger of {child_logger.parent.name} logger")


if __name__ == '__main__':
    main()