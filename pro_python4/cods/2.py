def flat_generator(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item

# Пример использования:
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

for item in flat_generator(nested_list):
    print(item)
