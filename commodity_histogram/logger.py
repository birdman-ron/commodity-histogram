import os
import logging
import config


def get_logger():
    log_file_handler = logging.FileHandler(config.LOG_DIR + os.path.sep + config.SERVICE_NAME + '.log')
    log_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file_handler.setFormatter(log_file_formatter)

    logger = logging.getLogger(config.SERVICE_NAME)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(log_file_handler)
    return logger
