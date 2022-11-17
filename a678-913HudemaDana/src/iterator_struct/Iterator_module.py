class IteratorStructure:

    def __init__(self):
        self.list = []
        self._poz = 0

    def __setitem__(self, key, value):
        self.list[key] = value

    def __getitem__(self, item):
        return self.list[item]

    def __delitem__(self, key):
        if key <= len(self.list):
            del self.list[key]

    def __next__(self):
        if self._poz == len(self.list):
            raise StopIteration("No element next")
        self._poz += 1
        return self.list[self._poz - 1]

    def __iter__(self):
        self._poz = 0
        return self

    def __len__(self):
        return len(self.list)


def sort_compare(list, index):
    if list[index] >= list[index - 1]:
        return True
    return False


def gnomeSort(list, sort_compare):
    index = 0
    while index < len(list):
        if index == 0:
            index = index + 1
        if sort_compare(list,index):
            index = index + 1
        else:
            list[index], list[index - 1] = list[index - 1], list[index]
            index = index - 1
    return list


def prop(element):
    return element != 0


def filter(list, prop):
    index = 0
    filtered_list = []
    while index < len(list):
        if prop(list[index]) is True:
            filtered_list.append(list[index])
        index += 1

    return filtered_list
