import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logger_handler = logging.FileHandler('./hh.log')
logger_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s')
logger.addHandler(logger_handler)
logger_handler.setFormatter(logger_formatter)