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

