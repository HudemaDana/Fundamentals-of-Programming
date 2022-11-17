"""
  Program functionalities module
"""

def get_apartment(dict,i):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param i: a position in a list from the dictionary
    :return: the number of an apartment on the i position
    """
    return dict['apartment'][i]

def get_amount(dict,i):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param i: a position in a list from the dictionary
    :return: the value of total amount of money that need to be paid by an apartment
    """
    return dict['amount'][i]

def get_water(dict,i):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param i: a position in a list from the dictionary
    :return: the value of the expense to water
    """
    return dict['water'][i]

def get_heating(dict,i):
    """

   :param dict: dictionary in which we keep all data about expenses of an apartment
    :param i: a position in a list from the dictionary
    :return: the value of the expense to heating
    """
    return dict['heating'][i]

def get_electricity(dict,i):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param i: a position in a list from the dictionary
    :return: the value of the expense to the electricity
    """
    return dict['electricity'][i]

def get_gas(dict,i):
    """
   :param dict: dictionary in which we keep all data about expenses of an apartment
    :param i: a position in a list from the dictionary
    :return: the value of the expense to the gas
    """
    return dict['gas'][i]

def get_other(dict,i):
    """

   :param dict: dictionary in which we keep all data about expenses of an apartment
    :param i: a position in a list from the dictionary
    :return: the value of the expense to others utilities
    """
    return dict['other'][i]

def get_value_type(dict,type,i):

    if type == 'water':
         return dict['water'][i]

    elif type =='heating':
         return dict['heating'][i]

    elif type =='electricity':
         return dict['electricity'][i]

    elif type =='gas':
         return dict['gas'][i]

    else:
         return dict['other'][i]

def get_list(nr):
    return nr


def set_dict(a,val):
    """

    :param a: is a calling of an element from the dictionary s.t a=dict[type], where type is one of the 5 given expenses
    :param val: the value that will be added to the dictionary on a new position
    :return: adds a number to a given list in the dictionary
    """
    a.append(val)

def set_value(dict,type,i,am,ok):
    if ok == 1:
        dict[str(type)][i] += am
    else:
        dict[str(type)][i] = 0

    return dict[str(type)][i]


def add(dict, list_max, ap:int, typee, am:int):
    """

    :param dict:
    :param ap:  apartment which has an amount of money to pay
    :param typee: type of expense that must be payed
    :param am: amount of the expense
    :return:  if there is a new apartment, it's added to the list, otherwise we just add the expense to the
              existing apartment and to the total amount of money that must be payed
    """
    if typee in dict:
        if ap in dict['apartment']:
            for i in range(0, len(dict['apartment'])):
                if get_apartment(dict,i) == ap:
                    dict['amount'][i]=set_value(dict,'amount',i,am,1)
                    dict[str(typee)][i]=set_value(dict,typee,i,am,1)
                    list_max[i][type_expense(typee)]=change_max(dict,list_max,typee,i)

        else:
            set_dict(dict['apartment'], ap)
            set_dict(dict['amount'], am)
            set_dict(dict['water'], 0)
            set_dict(dict['heating'], 0)
            set_dict(dict['electricity'], 0)
            set_dict(dict['gas'], 0)
            set_dict(dict['other'], 0)
            set_dict(list_max, [ap, 0, 0, 0, 0, 0])


            dict[typee][len(dict['gas'])-1]=set_value(dict,typee,len(dict['gas'])-1,am,1)
            list_max[len(list_max)-1][type_expense(typee)] = am
    else:
        raise KeyError("key doesn't exist")


def remove_to(dict, first:int, final:int):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param first: first apartment in a range [a,b] of positive integers
    :param final: last apartment in a range [a,b] of positive integers
    :return: removes all the payments for the apartment in range [first,final]
    """

    if first > final:
        raise ValueError("invalid input, please switch the numbers")

    else:
        if (first in dict['apartment']) or (final in dict['apartment']):
            for i in range(0, len(dict['apartment'])):
                if get_apartment(dict,i)>= first and get_apartment(dict,i)<=final:
                    dict['water'][i] = dict['heating'][i] = dict['electricity'][i] = dict['gas'][i] = dict['other'][i]=0
                    dict['amount'][i] = 0

        else:
            raise IndexError("invalid index")


def remove_ap(dict,ap:int):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :param ap: the number of an apartment
    :return: the function removes all the expenses for a given apartment. In case in which the apartment doesn't exists
             function will show a warning message
    """
    if ap in dict['apartment']:
        for i in range(0,len(dict['apartment'])):
            if get_apartment(dict,i) == ap:
                dict['amount'][i] = dict['water'][i] = dict['heating'][i] = dict['electricity'][i] = dict['gas'][i] = dict['other'][i] = 0
    else:
        raise ValueError("invalid value")


def remove_type(dict, type, ok):
    """
    :param ok: it's used to make program understand if we have to do just a remove (ok==1) or a filter (ok==0)
    :param dict: dictionary in which we keep all data about an apartment expenses
    :param type: represents one of the 5 expenses given ( water, electricity, gas, heating and other)
    :return:  the function removes a given type of expense from all apartments
    """
    if type in dict:
        for i in range(0,len(dict['apartment'])):
            if ok == 1:
                dict['amount'][i] -= get_value_type(dict,type,i)
            dict[str(type)][i] = 0
    else:
        raise KeyError("key doesn't exist")


def replace(dict, ap:int, type, am:int):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :param ap: the number of a given apartment (integer if it's possible)
    :param type: represents one of the 5 given expenses ( water, electricity, gas, heating and others)
    :param am: the amount of money that will be replaced in a type of expense
    :return: The function replace a given expense and change the total amount of money to be paid. In case in which
             the function doesn't find the number of the apartment in the dictionary, it shows a warning message on
             the screen
    """
    if ap in dict['apartment']:
        for i in range(0, len(dict['apartment'])):
            if dict['apartment'][i] == ap:
                dict['amount'][i] = get_amount(dict,i) - dict[str(type)][i] + am
                dict[str(type)][i] = am
    else:
        raise ValueError("invalid Value")


def sum(dict,typee):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param typee: the type of expense depending on which the sum will be done
    :return: the total amount of a certain type of expense
    """

    if (typee in dict) and (typee not in ['amount', 'apartment']):
        sum = 0
        for i in range(0,len(dict['gas'])):
            sum += get_value_type(dict,typee,i)
        return sum

    elif typee in ['amount','apartment']:
        raise Exception("cannot do the sum on this one")
    else:
        raise KeyError("couldn't find this type of expense")


def type_expense(word):
    """

    :param word: it's one of the given types of expenses
    :return: it returns a representative number for one of the 5 given words
    """
    if word == 'water':
        return 1
    if word == 'heating':
        return 2
    if word == 'electricity':
        return 3
    if word == 'gas':
        return 4
    if word == 'other':
        return 5

def number_expense(nr):
    """

    :param nr: it's a representative number for one of the 5 type of expenses
    :return: it returns the name of the expense
    """
    if nr == 1:
        return 'water'
    if nr == 2:
        return 'heating'
    if nr == 3:
        return 'electricity'
    if nr == 4:
        return 'gas'
    if nr == 5:
        return 'other'

def change_max(dict, list_max, typee, ap):
    """
    :param typee: the type of expense
    :param ap: the position where we can find the apartment
    :return: it returns the maximum between the last value of the expense and the current value of the expense
    """
    if (dict[typee][ap] > list_max[ap][type_expense(typee)]):
            return dict[typee][ap]

    return list_max[ap][type_expense(typee)]


def max(dict, list_max,ap):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param list_max: a list in which we keep the maximum values of the expenses
    :param ap: the apartment we are looking for
    :return: returns the position in which we find the searched apartment
    """
    if ap in dict['apartment']:
        for i in range(0,len(list_max)):
            if list_max[i][0] == ap:
                return i
    else:
        raise ValueError("incorrect input, try again to find the max")

def sort_app(l,a):
    """

    :param l: a list
    :param a: another list
    :return: returns the sorted l and a according to l values
    """
    i = 0
    while i < (len(l)-1):
        pos = i
        j = i + 1
        while j < len(l):
            if l[j] < l[pos]:
                pos = j
            j += 1

        aux = l[i]
        l[i] = l[pos]
        l[pos] = aux

        aux = a[i]
        a[i] = a[pos]
        a[pos] = aux
        i += 1


def sort_typee(l):
    """

    :param l:a list
    :return: returns the sorted list
    """
    i=0
    while i<4:
        pos=i
        j=i+1
        while j<5:
            if l[j][1]<l[pos][1]:
                pos=j
            j+=1
        aux=l[i]
        l[i]=l[pos]
        l[pos]=aux
        i+=1


def filter_type(dict,typee):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param typee: the type of the expense
    :return: it transform all the expenses to 0 out of the specified one in the type variable
    """
    if typee in dict:
        for i in range(2,len(dict)):
            if type_expense(typee) != (i-1):
                remove_type(dict,number_expense(int(i-1)),0)
    else:
        raise KeyError("didn't find the key to filter")

def filter_am(dict,am):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param am: the value expenses can't greater or equal to
    :return: returns the dictionary with all the values which are greater or equal to am being 0
    """
    for i in range(2,len(dict)):
        for j in range(0,len(dict['apartment'])):
            if dict[number_expense(i-1)][j] >= am:
                dict[number_expense(i-1)][j]=0

def convert_dict_list(dict,l):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param l: list in which we will transfer all the data from the dictionary
    """
    for i in range(0,len(dict['apartment'])):
        l.append([dict['apartment'][i],dict['amount'][i],dict['water'][i],dict['heating'][i],\
                  dict['electricity'][i],dict['gas'][i],dict['other'][i]])

def convert_list_dict(dict,list):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param list: list that was transformed at a moment from a dictionary
    """
    for i in range(2,7):
        for j in range(0,len(list)):
            dict[number_expense(i-1)][j] = get_list(list[j][i])

    for i in range(0,len(list)):
        dict['apartment'][i] = get_list(list[i][0])
        dict['amount'][i] = get_list(list[i][1])


def undo(dict, history):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :param history: the backup list, where we keep all the previous forms of the dictionary
    """
    if len(history) > 1:
        history.pop()
        list = history[-1][:]
        convert_list_dict(dict,list)
    else:
        raise Exception("There is no more undo. Pls stop and do something else :)")