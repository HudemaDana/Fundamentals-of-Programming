"""
test file
"""

from functions import *

def test_getter(dict):

    assert get_apartment(dict,2) == 3
    assert get_amount(dict,2) == 100
    assert get_gas(dict,5) == 0
    assert get_water(dict,6) == 0
    assert get_electricity(dict,1) == 1
    assert get_heating(dict,7) == 7
    assert get_other(dict, 4) == 10


def test_setter(dict):
    l = {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1],'electricity': [1, 1, 1], \
         'gas': [1, 1, 1], 'other': [1, 1, 1]}
    assert (set_value(l,'amount',1,200,0)) == 0
    assert (set_value(l,'gas',2,100,1)) == 101


def test_add():
    l = {'apartment': [],'amount': [],'water': [],'heating': [],'electricity': [],'gas': [],'other': []}
    list=[]

    add(l, list, 5, 'gas', 200)
    assert(l) == {'apartment': [5],'amount': [200],'water': [0],'heating': [0],\
                                   'electricity': [0],'gas': [200],'other': [0]}

    l = {'apartment': [1], 'amount': [10], 'water': [10], 'heating': [0], 'electricity': [0], 'gas': [0], 'other': [0]}
    add(l,list,1,'heating',10)
    assert(l) == {'apartment': [1],'amount': [20],'water': [10],'heating': [10],\
                                      'electricity': [0],'gas': [0],'other': [0]}


def test_remove_to():
    l = {'apartment': [1,2,3], 'amount': [5,5,5], 'water': [1,1,1], 'heating': [1,1,1], 'electricity': [1,1,1],\
         'gas': [1,1,1], 'other': [1,1,1]}

    remove_to(l,1,2)
    assert(l) == {'apartment': [1,2,3], 'amount': [0,0,5], 'water': [0,0,1], 'heating': [0,0,1], 'electricity': [0,0,1],\
                                'gas': [0,0,1], 'other': [0,0,1]}


def test_remove_ap():
    l = {'apartment': [1,2,3], 'amount': [5,5,5], 'water': [1,1,1], 'heating': [1,1,1], 'electricity': [1,1,1],\
         'gas': [1,1,1], 'other': [1,1,1]}

    remove_ap(l, 1)
    assert(l) == {'apartment': [1,2,3], 'amount': [0,5,5], 'water': [0,1,1], 'heating': [0,1,1], 'electricity': [0,1,1],\
         'gas': [0,1,1], 'other': [0,1,1]}


def test_remove_type():
    l = {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], 'electricity': [1, 1, 1], \
         'gas': [1, 1, 1], 'other': [1, 1, 1]}

    remove_type(l, 'water', 1)
    assert (l) =={'apartment': [1,2,3], 'amount': [4,4,4], 'water': [0,0,0], 'heating': [1,1,1], 'electricity': [1,1,1],\
                                       'gas': [1,1,1], 'other': [1,1,1]}



def test_replace():
    l = {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1],'electricity': [1, 1, 1], \
         'gas': [1, 1, 1], 'other': [1, 1, 1]}

    replace(l,2,'gas',100)
    assert(l) == {'apartment': [1, 2, 3], 'amount': [5, 104, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1],'electricity': [1, 1, 1], \
         'gas': [1, 100, 1], 'other': [1, 1, 1]}


def test_type_expense():
    assert (type_expense('water')) == 1
    assert (type_expense('heating')) == 2
    assert (type_expense('electricity')) == 3
    assert (type_expense('gas')) == 4
    assert (type_expense('other')) == 5
    assert (type_expense('waaskjdi')) == None


def test_number_expense():
    assert(number_expense(1)) == 'water'
    assert (number_expense(2)) == 'heating'
    assert (number_expense(3)) == 'electricity'
    assert (number_expense(4)) == 'gas'
    assert (number_expense(5)) == 'other'
    assert (number_expense(6)) == None


def test_sum(dict):
    assert(sum(dict,'gas')) == 283


def test_change_max():
    l = {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1],\
         'electricity': [1, 1, 1], 'gas': [1, 1, 1], 'other': [1, 1, 1]}
    list=[[1,6,2,1,1,1],[2,12,1,1,8,1],[3,5,1,1,1,1]]

    assert(change_max(l,list,'water', 0)) == 6
    assert (change_max(l,list,'gas', 1)) == 8


def test_sort_app():
    a=[2,1,3,4,5,9,6]
    b=['a','b','c','d','e','f','g']

    sort_app(a,b)
    assert(a)== [1,2,3,4,5,6,9]
    assert (b)==['b','a','c','d','e','g','f']


def test_sort_typee():
    a=[[1,9],[2,8],[3,7],[4,6],[5,5]]
    sort_typee(a)

    assert (a) == [[5,5],[4,6],[3,7],[2,8],[1,9]]


def test_filter_type():
    l = {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
         'electricity': [1, 1, 1], 'gas': [1, 1, 1], 'other': [1, 1, 1]}
    filter_type(l,'gas')
    assert(l) =={'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [0, 0, 0], 'heating': [0, 0, 0], \
                'electricity': [0, 0, 0], 'gas': [1, 1, 1], 'other': [0, 0, 0]}


def test_filter_am():
    l = {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
         'electricity': [1, 1, 1], 'gas': [1, 1, 1], 'other': [1, 1, 1]}

    filter_am(l,100)
    assert (l) == {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
                   'electricity': [1, 1, 1], 'gas': [1, 1, 1], 'other': [1, 1, 1]}
    filter_am(l,1)
    assert (l) == {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [0,0,0], 'heating': [0,0,0], \
                   'electricity': [0,0,0], 'gas': [0,0,0], 'other': [0,0,0]}


def test_convert_dict_list():
    l = {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
         'electricity': [1, 1, 1], 'gas': [1, 1, 1], 'other': [1, 1, 1]}
    list=[]

    convert_dict_list(l,list)
    assert(list) ==[[1,5,1,1,1,1,1],[2,5,1,1,1,1,1],[3,5,1,1,1,1,1]]


def test_convert_list_dict():
    list =[[1,5,1,1,1,1,1],[2,5,1,1,1,1,1],[3,5,1,1,1,1,1]]
    l= {'apartment': [1, 2, 3], 'amount': [5, 4, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
        'electricity': [1, 0, 1], 'gas': [1, 2, 1], 'other': [1, 1, 1]}

    convert_list_dict(l,list)
    assert(l) =={'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
                 'electricity': [1, 1, 1], 'gas': [1, 1, 1], 'other': [1, 1, 1]}


def test_undo():
    l=[[[1,5,1,1,1,1,1],[2,5,1,1,1,1,1],[3,5,1,1,1,1,1]],[[1,5,1,1,1,1,1],[2,4,1,1,0,2,1],[3,5,1,1,1,1,1]]]
    d={'apartment': [1, 2, 3], 'amount': [5, 4, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
        'electricity': [1, 0, 1], 'gas': [1, 2, 1], 'other': [1, 1, 1]}
    undo(d,l)
    assert(d) == {'apartment': [1, 2, 3], 'amount': [5, 5, 5], 'water': [1, 1, 1], 'heating': [1, 1, 1], \
                 'electricity': [1, 1, 1], 'gas': [1, 1, 1], 'other': [1, 1, 1]}


def big_boss_test(dict):
    test_setter(dict)
    test_getter(dict)
    test_add()
    test_remove_to()
    test_remove_type()
    test_remove_ap()
    test_replace()

    test_type_expense()
    test_number_expense()

    test_sum(dict)
    test_change_max()

    test_sort_app()
    test_sort_typee()

    test_filter_type()
    test_filter_am()

    test_convert_list_dict()
    test_convert_dict_list()

    test_undo()
