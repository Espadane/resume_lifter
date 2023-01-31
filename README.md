# Resume lifter

Небольшой скрипт написанный на Python с использованием библиотеки Selenium. 
Написан под вебдрайвер Google Chrome. Просто поднимает резюме в поиске на HeadHunter.
Можно настроить время поднятия через Cron.

## Инструкция по запуску

- Создать и активировать виртуальное окружение, обновить pip - `python3 -m venv venv && source venv/bin/activate && python3 -m pip3 install --upgrade pip`
- Установить зависимости - `pip3 install -r requirements.txt`
- Установить Google Chrome
- Прописать в config.py переменные окружения:
    - MY_EMAIL - почта от HH.
    - MY_PASSWORD - пароль от HH.
    - Если необходимо поменять USER_AGENT.
- Дать права на запуск файлу - `chmod +x ./main.py`
- Сменить уровень логера на 'WARNING' если необходимо.
- Запустить скрипт - `python3 ./main.py`

## Запуск скрипта по расписанию
- Установить зависимости вне виртуального окружения.
- Изменить PROJECT_DIR в config.py на путь к папке проекта.
- Изменить `crontab -e`. Например поднятия каждые 4 часа:
```
MY_EMAIL=your@email.com
MY_PASSWORD=MyVeryStrongPassword
0 7 * * * path_to_python3 absolute_path_to_main.py
10 11 * * * path_to_python3 absolute_path_to_main.py
20 15 * * * path_to_python3 absolute_path_to_main.py
30 19 * * * path_to_python3 absolute_path_to_main.py
```
