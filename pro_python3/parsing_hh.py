import requests
import json

url = "https://api.hh.ru/vacancies"
params = {
    'text': 'python',
    'area': [1, 2],  # 1 - Москва, 2 - Санкт-Петербург
    'per_page': 100,  # Количество вакансий на одной странице
    'page': 0  # Номер страницы (начинается с 0)
}

result = []

# Количество страниц для парсинга
num_pages = 5

for page in range(num_pages):
    params['page'] = page
    response = requests.get(url, params=params)
    data = response.json()

    for item in data['items']:
        description_url = item['url']
        description_response = requests.get(description_url)
        description_data = description_response.json()

        description = description_data.get('description', '')
        if 'Django' in description and 'Flask' in description:
            salary = item['salary']
            if salary:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
                currency = salary.get('currency', 'RUR')
                if salary_from and salary_to:
                    salary_str = f"{salary_from} - {salary_to} {currency}"
                elif salary_from:
                    salary_str = f"{salary_from} {currency}"
                elif salary_to:
                    salary_str = f"{salary_to} {currency}"
                else:
                    salary_str = 'Не указана'
            else:
                salary_str = 'Не указана'

            result.append({
                'Ссылка на вакансию': item['alternate_url'],
                'Зарплата': salary_str,
                'Компания': item['employer']['name'],
                'Город': item['area']['name']
            })

# Файл с конечной выгрузкой
with open(r'C:\Users\User\Desktop\test\vacancies.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
