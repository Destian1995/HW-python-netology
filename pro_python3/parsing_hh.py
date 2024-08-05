from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os

# Запуск браузера в фоновом режиме, без GPU и песочницы.
def connect_site(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def searchitems(driver, keywords, jsondict=None):
    if jsondict is None:
        jsondict = {}

    vacancy_class_name = 'vacancy-name'
    salary_class_name = 'compensation-text'
    company_class_name = 'company-info-text'
    city_class_name = 'vacancy-serp__vacancy-address'
    link_class_name = 'bloko-link'

    wait = WebDriverWait(driver, 10)

    vacancies = driver.find_elements(By.XPATH, f"//*[contains(@class, '{vacancy_class_name}')]")
    salaries = driver.find_elements(By.XPATH, f"//*[contains(@class, '{salary_class_name}')]")
    companies = driver.find_elements(By.XPATH, f"//*[contains(@class, '{company_class_name}')]")
    cities = driver.find_elements(By.XPATH, f"//*[contains(@data-qa, '{city_class_name}')]")
    links = driver.find_elements(By.XPATH, f"//*[contains(@class, '{link_class_name}')]")

    citiesitog = [city.text for city in cities if city.text]
    links1 = [element.get_attribute('href') for element in links if
              element.get_attribute('href') and 'https://spb.hh.ru/vacancy/' in element.get_attribute('href')]
    salaries1 = [salary.text for salary in salaries if salary.text]

    for city, vacancy, salary, company, link in zip(citiesitog, vacancies, salaries1, companies, links1):
        # Переходим на страницу вакансии, чтобы проверить описание
        driver.get(link)
        time.sleep(3)

        description_element = driver.find_element(By.XPATH, '//div[@class="vacancy-description"]')
        description = description_element.text if description_element else "No description"

        if any(keyword in description for keyword in keywords):
            print(
                f'Город: {city}, Вакансия: {vacancy.text}, Зарплата: {salary}, Компания: {company.text}, Ссылка: {link}')
            jsondict[vacancy.text] = {
                'Город': city,
                'Зарплата': salary.replace(u"\u202F", " "),
                'Компания': company.text,
                'Ссылка': link
            }

        # Возвращаемся на предыдущую страницу с вакансиями
        driver.back()
        time.sleep(3)

    return jsondict


def nextpage(driver):
    nextpage_class = 'pager-next'
    try:
        dalshe = driver.find_element(By.XPATH, f"//*[contains(@data-qa, '{nextpage_class}')]")
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(dalshe))
        button.click()
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Кнопка не найдена: {e}")
        return False


def write_to_json(jsondict, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(jsondict, file, indent=4, ensure_ascii=False)


def main(cities, keywords, output_path):
    url = f"https://spb.hh.ru/search/vacancy?text=python&search_field=description&enable_snippets=true&area={cities[0]}&area={cities[1]}"
    driver = connect_site(url)
    dictj = {}
    try:
        while True:
            time.sleep(3)
            searchitems(driver, keywords, dictj)
            time.sleep(3)
            if not nextpage(driver):
                break
        write_to_json(dictj, output_path)
    finally:
        driver.quit()


if __name__ == '__main__':
    cities = [1, 2]  # Можно изменить на любой список городов
    keywords = ['Django', 'Flask']  # Можно изменить на любые ключевые слова
    output_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'test', 'vacancies.json')

    main(cities, keywords, output_path)
