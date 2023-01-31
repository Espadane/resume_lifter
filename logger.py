import logging
from config import PROJECT_DIR, PROJECT_NAME


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_handler = logging.FileHandler(f'{PROJECT_DIR}hh.log')
logger_formatter = logging.Formatter(
    f'{PROJECT_NAME}: %(asctime)s - %(levelname)s - \
%(funcName)s: %(lineno)d - %(message)s', 
    datefmt='%d.%b.%Y %H:%M')
logger.addHandler(logger_handler)
logger_handler.setFormatter(logger_formatter)
