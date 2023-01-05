# Resume lifter

Небольшой скрипт написанный на Python с использованием библиотеки Selenium. 
Написан под вебдрайвер Google Chrome. Просто поднимает резюме в поиске на HeadHunter.
Можно настроить время поднятия через Cron.

## Инструкция по запуску

- Создать и активировать виртуальное окружение, обновить pip ("python3 -m venv venv && source venv/bin/activate && secret && python3 -m pip install --upgrade pip")
- Установить зависимости ("pip3 install -r requerements.txt")
- Прописать в config.py переменные окружения:
    - MY_EMAIL - почта от HH
    - MY_PASSWORD - пароль от HH
    - Если необходимо поменять USER_AGENT
- Дать права на запуск файлу ("chmod +x ./lifter")
- Запустить скрипт "./lifter"

## Запуск скрипта по расписанию

