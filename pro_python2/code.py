import csv
import re
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
file_path = r'C:\Users\User\Desktop\test\phonebook_raw.csv'
result_file = r'C:\Users\User\Desktop\test\output.csv'

with open(file_path, encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: Приведение ФИО к формату "Фамилия, Имя, Отчество"
for contact in contacts_list:
    full_name = ' '.join(contact[:3]).split()
    while len(full_name) < 3:
        full_name.append('')
    contact[:3] = full_name

# Приведение телефонов к формату +7(999)999-99-99 доб.9999
phone_pattern = re.compile(
    r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(?:\s*доб\.*\s*(\d+))?"
)
phone_sub = r"+7(\2)\3-\4-\5 доб.\6"

for contact in contacts_list:
    contact[5] = re.sub(phone_pattern, phone_sub, contact[5]).replace(' доб. ', ' доб.')

# Объединение дублирующихся записей
contacts_dict = {}
for contact in contacts_list:
    key = (contact[0], contact[1])
    if key not in contacts_dict:
        contacts_dict[key] = contact
    else:
        existing = contacts_dict[key]
        for i in range(2, len(contact)):
            if not existing[i]:
                existing[i] = contact[i]

# Преобразование словаря обратно в список
contacts_list = list(contacts_dict.values())

# TODO 2: Сохраните получившиеся данные в другой файл
with open(result_file, "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

pprint(contacts_list)
