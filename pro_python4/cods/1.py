class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.main_index = 0
        self.sub_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.main_index < len(self.nested_list):
            if self.sub_index < len(self.nested_list[self.main_index]):
                item = self.nested_list[self.main_index][self.sub_index]
                self.sub_index += 1
                return item
            self.main_index += 1
            self.sub_index = 0
        raise StopIteration

# Пример использования:
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item)

# Для создания плоского списка с помощью comprehension выражения:
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
