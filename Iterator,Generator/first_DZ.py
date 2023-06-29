
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.cursor1 = 0
        self.cursor2 = 0
        return self

    def __next__(self):
        while self.cursor2 < 3:
            if self.cursor < len(self.list_of_list[self.cursor]):
                if self.cursor1 < len(self.list_of_list[self.cursor]):
                    item = self.list_of_list[self.cursor][self.cursor1]
                    self.cursor1 += 1
                    return item
                else:
                    self.cursor1 = 0
                    self.cursor += 1
                    self.cursor2 += 1
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