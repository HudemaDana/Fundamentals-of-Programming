from src.services.services import Services


class Test:

    def test_create_new_list(self):
        assert (Services().create_new_list()) == [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9],
                                                  [9, 10], [10, 11]]

    def test_set_list(self):
        list = [[1, 1], [2, 2], [3, 3]]
        Services().set_list(list, [4, 4])
        assert (list) == [[1, 1], [2, 2], [3, 3], [4, 4]]

    def test_add(self):
        list = [[1, 1], [2, 2], [3, 3]]
        Services().add(list, 4, 4)
        assert (list) == [[1, 1], [2, 2], [3, 3], [4, 4]]

    def test_filter(self):
        list = [[1, 1], [2, 2], [3, 3], [4, 4]]
        Services().filter(list, 1, 2)
        assert list == [[2, 2], [3, 3]]
        Services().filter(list, -3, 2)
        assert list == [[2, 2], [3, 3]]
        Services().filter(list, 1, 10)
        assert list == [[2, 2], [3, 3]]

    def test_undo(self):
        list = [[[1, 1], [2, 2], [3, 3], [4, 4]], [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2]],
                [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [10, 10]]]
        Services().undo(list)
        assert(list) == [[[1, 1], [2, 2], [3, 3], [4, 4]], [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2]]]
        Services().undo(list)
        assert (list) == [[[1, 1], [2, 2], [3, 3], [4, 4]]]

    def tests(self):
        self.test_create_new_list()
        self.test_set_list()
        self.test_add()
        self.test_undo()