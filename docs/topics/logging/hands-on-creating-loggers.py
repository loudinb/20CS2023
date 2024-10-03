import logging

root_logger = logging.getLogger()
module_logger = logging.getLogger(__name__)
app_logger = logging.getLogger('app')


def main():
    root_logger.warning("warning logged to root logger")
    module_logger.warning("warning logged to module logger")
    app_logger.warning("warning logged to app logger")


if __name__ == '__main__':
    main()