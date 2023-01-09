from os import getenv
from sys import exit
from webdriver_manager.chrome import ChromeDriverManager


PROJECT_DIR = './'

HH_LOGIN = getenv("MY_EMAIL")
if not HH_LOGIN:
    exit("Ошибка: не задана почта.")

HH_PASSWORD = getenv("MY_PASSWORD")
if not HH_PASSWORD:
    exit("Ошибка: не задан пароль.")
    
HH_URL = 'https://www.hh.ru'

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    
DRIVER_PATH = ChromeDriverManager().install()