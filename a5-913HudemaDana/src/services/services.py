from src.domain.domain import Complex
import random


class Services:

    def create_new_list(self):
        """

        :return: a list which contains 10 complex numbers
        """
        list = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]
        return list

    def get_nums(self):
        list = []
        for i in range(10):
            nr = Complex(random.randint(-100, 100), random.randint(-100, 100))
            nr.set_pair(list)

        return list

    def set_list(self, list, val):
        """

        :param list: contains a list of complex numbers
        :param val: represents a value we want to add to the list
        :return: add the value to the list
        """
        list.append(val[:])

    def add(self, list, a, b):
        """

        :param list: contains a list of complex numbers
        :param a: it represents the real part of a complex number
        :param b: it represents the imaginary part of a complex number
        :return: adds a pair [a,b] which represents the parts of a complex number
        """
        number = Complex(a, b)
        number.set_pair(list)

    def filter(self, list, start, end):
        """

        :param list: contains a list of complex numbers
        :param start: the position where we start to filter
        :param end: the position where we finish the filter
        :return: the program returns the list filtered, where anything but numbers between [a,b] interval is 0
        """

        if start > end or end < 0 or start > len(list) - 1:
            raise ValueError("The interval doesn't exist. Please try other values")

        else:
            l = []
            if start < 0:
                if end <= len(list) - 1:
                    for i in range(0, end + 1):
                        l.append(list[i])
            else:
                if end <= len(list) - 1:
                    for i in range(start, end + 1):
                        l.append(list[i])
                else:
                    for i in range(start, len(list)):
                        l.append(list[i])

            list = l
            return list

    def undo(self, backup):
        """

        :param backup: a list in which we save all the operations that have been done
        :return:
        """
        if len(backup) > 1:
            backup.pop()
            l = backup[-1][:]

            return backup, l
        else:
            raise Exception("There is no other undo to be done")
