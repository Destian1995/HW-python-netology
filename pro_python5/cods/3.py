# Импортируем декоратор
import datetime

def logger_with_path(log_path):
    def logger(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(log_path, 'a') as log_file:
                log_file.write(f'{datetime.datetime.now()} - {func.__name__} called with args: {args}, kwargs: {kwargs}. Returned: {result}\n')
            return result
        return wrapper
    return logger

# Применение к итератору и генератору
class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.main_index = 0
        self.sub_index = 0

    def __iter__(self):
        return self

    @logger_with_path('iterator_log.txt')
    def __next__(self):
        while self.main_index < len(self.nested_list):
            if self.sub_index < len(self.nested_list[self.main_index]):
                item = self.nested_list[self.main_index][self.sub_index]
                self.sub_index += 1
                return item
            self.main_index += 1
            self.sub_index = 0
        raise StopIteration

def flat_generator(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item

# Пример использования
nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# Используем итератор с логированием
for item in FlatIterator(nested_list):
    print(item)

# Используем генератор с логированием
@logger_with_path('generator_log.txt')
def use_flat_generator(nested_list):
    return list(flat_generator(nested_list))

flat_list = use_flat_generator(nested_list)
print(flat_list)
