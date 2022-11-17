import unittest
from src.iterator_struct.Iterator_module import IteratorStructure, sort_compare,gnomeSort, filter,prop


class TestIteratorStructure(unittest.TestCase):
    def setUp(self) -> None:
        self.c = IteratorStructure()

    def tearDown(self) -> None:
        pass

    def test_getter(self):
        self.c.list = [1, 2, 3, 4, 5]
        self.assertEqual(self.c.__getitem__(2), 3)

    def test_setter(self):
        self.c.list = [1, 2, 3, 4, 5]
        self.c.__setitem__(1,3)
        self.assertEqual(self.c.list, [1, 3, 3, 4, 5])

    def test_del(self):
        self.c.list = [1, 2, 3, 4, 5]
        self.c.__delitem__(1)
        self.assertEqual(self.c.list, [1, 3, 4, 5])

    def test_next(self):
        try:
            assert self.c.__next__() == True
        except StopIteration as si:
            assert str(si) == "No element next"

        self.c.list = [1, 2, 3, 4, 5]
        iter = self.c.__next__()

        self.assertEqual(iter,1)

    def test_iter(self):
        iter = self.c.__iter__()
        self.assertEqual(iter, self.c)

    def test_gnome_sort(self):
        list=[7,6,5,4,3,2,1]
        list = gnomeSort(list,sort_compare)
        self.assertEqual(list,[1,2,3,4,5,6,7])

    def test_filter(self):
        list= [0,0,0,0,1,1,2]
        list= filter(list,prop)
        self.assertEqual(list,[1,1,2])