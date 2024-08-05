class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = []
        self.list_index = 0
        self.element_index = 0

    def __iter__(self):
        self.list_index = 0
        self.element_index = 0
        self.current_list = self.list_of_list[self.list_index] if self.list_of_list else []
        return self

    def __next__(self):
        while self.list_index < len(self.list_of_list):
            if self.element_index < len(self.current_list):
                item = self.current_list[self.element_index]
                self.element_index += 1
                return item
            self.list_index += 1
            self.element_index = 0
            if self.list_index < len(self.list_of_list):
                self.current_list = self.list_of_list[self.list_index]
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
