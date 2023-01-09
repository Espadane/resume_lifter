import time
from config import *
from logger import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from config import *


def _create_driver():
    try:
        options = Options()
        options.add_argument(f'user-agent={USER_AGENT}')
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=DRIVER_PATH,\
                                        options=options)
        logger.debug('Драйвер создан')
        return driver

    except WebDriverException as error:
        logger.warning(f'{error.msg}')
        
def _login(driver):
    _move_to_site(driver)
    _push_login_button(driver)
    _push_login_with_pass_btn(driver)
    _input_authorization_data(driver)
    _push_enter_btn(driver)
    _go_to_my_resumes(driver)
    _lift_my_resumes(driver)
    
def _move_to_site(driver):
    try:
        driver.get(HH_URL)
        logger.debug('Перешли на сайт HH.')
    except WebDriverException as error:
        logger.warning(f'{error.msg}')

def _push_login_button(driver):
    try:
        login_btn = driver.find_element(by=By.LINK_TEXT, value='Войти')
        login_btn.click()
        logger.debug('Кнопка "Войти" нажата.')
    except WebDriverException as error:
        logger.warning(f'{error.msg}')

def _close_driver(driver):
    try:
        driver.quit()
        logger.debug('Драйвер закрыт.')
    except WebDriverException as error:
        logger.warning(f'{error.msg}')

def _push_login_with_pass_btn(driver):
    try:
        buttons = driver.find_elements(by=By.TAG_NAME, value='button')
        for button in buttons:
            if 'Войти с паролем' in button.text:
                button.click()
        driver.implicitly_wait(2)
        logger.debug('Кнопка "Войти с паролем нажата".')
    except WebDriverException as error:
        logger.warning(f'{error.msg}')

def _input_authorization_data(driver):
    try:
        inputs = driver.find_elements(by=By.TAG_NAME, value='input')
        for element in inputs:
            if 'почта' in element.get_attribute('placeholder'):
                element.send_keys(HH_LOGIN)
                driver.implicitly_wait(2)
                logger.debug('Логин введен.')
            elif 'Пароль' in element.get_attribute('placeholder'):
                element.send_keys(HH_PASSWORD)
                driver.implicitly_wait(2)
                logger.debug('Пароль введен.')
            else:
                continue
    except WebDriverException as error:
        logger.warning(f'{error.msg}')

def _push_enter_btn(driver):
    try:
        buttons = driver.find_elements(by=By.TAG_NAME, value='button')
        for button in buttons:
            if button.get_attribute('data-qa') == 'account-login-submit':
                button.click()
        driver.implicitly_wait(10)
        logger.debug('Кнопка входа нажата успешно.')
    except WebDriverException as error:
        logger.warning(f'{error.msg}')

def _go_to_my_resumes(driver):
    try:
        my_resumes_btn = driver.find_element(by=By.LINK_TEXT,
                                             value='Мои резюме')
        my_resumes_btn.click()
        driver.implicitly_wait(10)
        logger.debug('Перешли в "Мои резюме".')
    except WebDriverException as error:
        logger.warning(f'{error.msg}')

def _lift_my_resumes(driver):
    counter = 0
    try:
        buttons = driver.find_elements(by=By.TAG_NAME, value='button')
        for button in buttons:
            if button.get_attribute('data-qa') == 'resume-update-button':
                button.click()
                logger.debug('Кнопка поднятия резюме нажата.')
                counter +=1
        if counter == 0:
            logger.debug('Резюме требующих поднятия нет.')
            resume_update_text = driver.find_element(by=By.CLASS_NAME,
                                            value='applicant-resumes-update')
            logger.debug(resume_update_text.text)
        else:
            logger.debug(f'Поднято {counter} резюме')
    except WebDriverException as error:
        logger.warning(f'{error.msg}')



def main():
    driver = _create_driver()
    _login(driver)
    time.sleep(5)
    _close_driver(driver)
    
if __name__=='__main__':
    main()