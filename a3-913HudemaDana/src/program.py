"""
  Write non-UI functions below
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


def test_getter(dict):

    assert get_apartment(dict,2) == 3
    assert get_amount(dict,2) == 100
    assert get_gas(dict,5) == 0
    assert get_water(dict,6) == 0
    assert get_electricity(dict,1) == 1
    assert get_heating(dict,7) == 7
    assert get_other(dict, 4) == 10

def test_setter(dict):

    assert set_value(dict,'amount',5,200,0) == 0
    assert set_value(dict,'gas',2,100,1) == 124


def add(dict, ap:int, typee, am:int):
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
                    dict[str(typee)][i]=set_value(dict,typee,i,am,0)


        else:
            set_dict(dict['apartment'], ap)
            set_dict(dict['amount'], am)
            set_dict(dict['water'], 0)
            set_dict(dict['heating'], 0)
            set_dict(dict['electricity'], 0)
            set_dict(dict['gas'], 0)
            set_dict(dict['other'], 0)


            dict[typee][len(dict['gas'])-1]=set_value(dict,typee,len(dict['gas'])-1,am,1)

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


def remove_type(dict, type):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :param type: represents one of the 5 expenses given ( water, electricity, gas, heating and other)
    :return:  the function removes a given type of expense from all apartments
    """
    for i in range(0,len(dict['apartment'])):
        dict['amount'][i] -= get_value_type(dict,type,i)
        dict[str(type)][i] = 0



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




def split_command(dict,command):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :param command: a string that is written by a user in order to make a command to the program
    :return: depending how the string starts, it's gonna be split in words and examined to find out if it's one
             of the given commands in the program. If it's not the needed form or writting, the function will show on
             the screen a warning message
    """
    command = command.strip()
    command = command.lower()   #make all strings lower

    if command == 'list':
        list_all(dict)
        return

    token = command.split(maxsplit=1) #split the command by the first word

    if token[0] == 'add':
        try:
            new_str = token[1].split(maxsplit=2)
            add(dict, int(new_str[0]), new_str[1], int(new_str[2]))
        except KeyError as ke:
            print(ke)

    elif token[0] == 'remove':
        if 'to' in token[1]:
            try:
                new_str = token[1].split(maxsplit=2)
                remove_to(dict, int(new_str[0]), int(new_str[2]))
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)


        elif token[1][0] >='0' and token[1][0]<='9':
            try:
                remove_ap(dict,int(token[1]))
            except ValueError as ve:
                 print(ve)

        else:
            remove_type(dict,token[1])

    elif token[0] == 'replace':
        try:
            new_str = token[1].split(maxsplit=3)
            replace(dict, int(new_str[0]), new_str[1], int(new_str[3]))
        except ValueError as ve:
            print(ve)

    elif token[0] == 'list':
        if token[1][0] >= '0' and token[1][0] <= '9':
             try:
                list_ap(dict,int(token[1]))
             except ValueError as ve:
                  print(ve)


        elif ('>' in token[1]) or ('<' in token[1]) or ('=' in token[1]):
            try:
                new_str=token[1].split(maxsplit=1)
                list_am(dict, new_str[0], int(new_str[1]))
            except Exception as ex:
                print(ex)
        else:
            raise Exception

    else:
        raise Exception("invalid input")

"""
  Write the command-driven UI below
"""
def menu():

    print("1. Add a number (add <apartment> <type> <amount>) ")
    print("2. Remove:")
    print("\ta.Remove expenses from an apartment (remove <apartment>)")
    print("\tb.Remove all expenses from start to final apartment (remove <start apartment> to <final apartment>)")
    print("\tc.Remove a type of expense from all apartments(remove <type>)")
    print("3.Replace an amount for an expense in an apartment (replace <apartment> <type> with <amount>)")
    print("4.List:")
    print("\ta. List all (list)")
    print("\tb.List all data for an apartment(list <apartment>)")
    print("\tc.List apartment with an amount '<', '=' or '>' than a given value (list [ < | = | > ] <amount>)")

def list_all(dict):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :return: display on the screen all the apartment's, inclund the expenses from each one
    """
    for i in range(0,len(dict['apartment'])):
        print(dict['apartment'][i]," ",dict['amount'][i]," ",dict['water'][i]," ",dict['heating'][i]," ",dict['electricity'][i]," ",dict['gas'][i]," ",dict['other'][i])


def list_am(dict, sign, am:int):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :param sign: a sign from ('>','=','<')
    :param am: the value with which are compared the elements from the total amount of money list
    :return: display on the screen all the apartments that have the total amount of money that need to be paid on
            expenses '>', '='  or '<' than a given value represented by am
    """
    if sign == '>':
        for i in range(0,len(dict['apartment'])):
            if get_amount(dict,i) > am:
                print('Apartment: ', get_apartment(dict,i))
    elif sign == '<':
        for i in range(0,len(dict['apartment'])):
            if get_amount(dict,i) < am:
                print('Apartment: ', get_apartment(dict,i))
    elif sign == '=':
        for i in range(0,len(dict['apartment'])):
            if get_amount(dict,i) == am:
                print('Apartment: ', get_apartment(dict,i))
    else:
        raise Exception("searched sign not found,try again")


def list_ap(dict,ap:int):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :param ap: number of an apartment
    :return: the function display on the screen all data about a given apartment from the dictionary. In case there is
             no such an apartment in dictionary, it will pe put on the screen a warning message
    """
    if ap in dict['apartment']:
        for i in range(0,len(dict['apartment'])):
            if get_apartment(dict,i) == ap:
                print('Apartment: ',get_apartment(dict,i))
                print('Amount: ',get_amount(dict,i))
                print('Types:')
                print("\tWater: ",get_water(dict,i))
                print("\tGas: ",get_gas(dict,i))
                print('\tElectricity: ',get_electricity(dict,i))
                print('\tHeating: ',get_heating(dict,i))
                print('\tOther: ',get_other(dict,i))
    else:
        raise ValueError("invalid input,no data to be listed")

def console(dict):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :return: read the text
    """
    while True:
        menu()
        command=str(input("How can I help you?"))
        try:
            if command.lower() == "exit":
                return
            split_command(dict, command)
        except Exception as ex:
            print(ex)



def main():
    dict = {
        'apartment': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'amount': [1, 10, 100, 200, 20, 2, 3, 30, 300, 333],
        'water': [1,2,12,24,2,0,0,10,100,3],
        'heating': [0,3,8,16,2,0,3,7,0,150],
        'electricity': [0,1,30,60,2,0,0,5,0,30],
        'gas': [0,3,24,48,6,0,0,2,200,0],
        'other': [0,1,26,52,10,0,0,3,0,150]
          }

    test_getter(dict)
    test_setter(dict)
    console(dict)

main()
