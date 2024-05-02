import os
#Задание 1
def read_recipes(file_name):
    cook_book = {}
    #Здесь я дополнительно указал кодировку для считывания файла чтобы русские символы были читаемы
    with open(file_name, 'r', encoding='UTF-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredient_dict = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(ingredient_dict)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book

#Путь файла
file_name = r'C:\Users\User\Desktop\test\recipes.txt'
cook_book = read_recipes(file_name)
print(cook_book)

#Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list

# Пример вызова функции
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)

#Задание 3
def merge_files(file_names, output_file):
    file_info = []

    # Читаем содержимое файлов и сохраняем информацию о количестве строк
    for file_name in file_names:
        with open(file_name, 'r', encoding='UTF-8') as file:
            content = file.readlines()
            file_info.append((file_name, len(content), content))

    # Сортируем файлы по количеству строк
    file_info.sort(key=lambda x: x[1])

    # Записываем отсортированные файлы в результирующий файл
    with open(output_file, 'w', encoding='UTF-8') as result_file:
        for file_name, line_count, lines in file_info:
            result_file.write(f"{file_name}\n{line_count}\n")
            result_file.writelines(lines)


# Пример вызова функции с заданными именами файлов
file_names = [r"C:\Users\User\Desktop\test\files\1.txt", r"C:\Users\User\Desktop\test\files\2.txt", r"C:\Users\User\Desktop\test\files\3.txt"]  # Имена файлов в папке
output_file = "merged_file.txt"  # Имя файла для результата
merge_files(file_names, output_file)

Вот что получилось:
```
C:\Users\User\Desktop\test\files\2.txt
1
Тревога началась в тринадцать часов ноль две минуты. C:\Users\User\Desktop\test\files\1.txt
8
Начальник  полиции
лично позвонил в шестнадцатый участок. А спустя  одну минуту тридцать секунд
в дежурке и других комнатах нижнего этажа раздались звонки
     Когда Иенсен  --  комиссар  шестнадцатого  участка --  вышел  из своего
кабинета,  звонки еще  не смолкли. Иенсен был мужчина средних лет,  обычного
сложения, с лицом плоским и невыразительным. На последней ступеньке винтовой
лестницы  он задержался  и  обвел взглядом помещение дежурки. Затем поправил
галстук и проследовал к машине.C:\Users\User\Desktop\test\files\3.txt
9
     В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди
потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире
резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.
Одеты они были хорошо, но как-то удивительно походили друг на друга и все до
одного спешили. Они шли нестройными  вереницами, широко разливались, завидев
красный  светофор или  металлический  блеск кафе-автоматов.  Они непрестанно
озирались по сторонам и теребили портфели и сумочки.
     Полицейские  машины  с  включенными  сиренами  пробивались  сквозь  эту
толчею.
```