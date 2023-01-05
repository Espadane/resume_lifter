from os import getenv
from sys import exit


hh_login = getenv("MY_EMAIL")
if not hh_login:
    exit("Ошибка: не задана почта.")

hh_password = getenv("MY_PASSWORD")
if not hh_password:
    exit("Ошибка: не задан пароль.")

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"