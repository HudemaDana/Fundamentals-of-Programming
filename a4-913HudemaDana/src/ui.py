"""
  User interface module
"""
from functions import *



def list_all(dict):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :return: display on the screen all the apartment's, inclund the expenses from each one
    """
    for i in range(0,len(dict['apartment'])):
        print("APARTMENT: ",dict['apartment'][i]," AMOUNT: ",dict['amount'][i]," WATER: ",dict['water'][i],\
              " HEATING: ",dict['heating'][i]," ELECTRICITY: ",dict['electricity'][i]," GAS: ",dict['gas'][i],\
              " OTHER: ",dict['other'][i])


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
                print('\nAPARTMENT:     ',get_apartment(dict,i))
                print('AMOUNT:        ',get_amount(dict,i))
                print('TYPES:')
                print("\tWATER:       ",get_water(dict,i))
                print('\tHEATING:     ',get_heating(dict,i))
                print('\tELECTRICITY: ',get_electricity(dict,i))
                print("\tGAS:         ",get_gas(dict,i))
                print('\tOTHER:       ',get_other(dict,i))
    else:
        raise ValueError("invalid input,no data to be listed")

def list_max_expense(list_max,i):
    """

    :param list_max: list in which we keep the max amount for expenses
    :param i: the position in which we find the wanted apartment
    :return: display on the screen the maximum amount for each type of expense
    """
    print("MAXIMUM AMOUNT FOR EACH EXPENSE TYPE:\n")
    print("WATER:      ", list_max[i][1])
    print("HEATING:    ", list_max[i][2])
    print("ELECRICITY: ", list_max[i][3])
    print("GAS:        ", list_max[i][4])
    print("OTHER:      ", list_max[i][5])

def list_sort_ap(l,a):
    """

    :param l: the list in which we have the amount of money
    :param a: the list in which we have the numbers of the apartments
    :return: display on the screen the apartment and the amount of money from the expenses sorted
    """
    for i in range(0,len(l)):
        print(a[i]," ",l[i])


def sort_ap(dict):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :return: sorted lists, according to the total amount of money that need to be paid
    """
    ap=dict['apartment'][:]
    am=dict['amount'][:]

    sort_app(am,ap)
    list_sort_ap(am,ap)


def list_sort_type(l):
    """

    :param l: list in which we keep the total amount of money for each type of expense
    :return: display on the screen the name of the expence and the amount of money for it
    """
    for i in range(0,4):
        print(l[i][0],': ',l[i][1])


def sort_type(dict):
    """

    :param dict: dictionary in which we keep all data about expenses of an apartment
    :return: it makes the sum for each type of expenses, saving it into a list and then we sort it according to the sums
    """
    l=[['WATER',0],['HEATING',0],['ELECTRICITY',0],['GAS',0],['OTHER',0]]

    for i in range(2,len(dict)):
        for j in range(0,len(dict['apartment'])):
            l[i-2][1] += dict[number_expense(i-1)][j]

    sort_typee(l)
    list_sort_type(l)


def menu():

    print("\n\n1. Add a number (add <apartment> <type> <amount>) ")
    print("2. Remove:")
    print("\ta.Remove expenses from an apartment (remove <apartment>)")
    print("\tb.Remove all expenses from start to final apartment (remove <start apartment> to <final apartment>)")
    print("\tc.Remove a type of expense from all apartments(remove <type>)")
    print("3.Replace an amount for an expense in an apartment (replace <apartment> <type> with <amount>)")
    print("4.List:")
    print("\ta. List all (list)")
    print("\tb.List all data for an apartment(list <apartment>)")
    print("\tc.List apartment with an amount '<', '=' or '>' than a given value (list [ < | = | > ] <amount>)")
    print("5. Sum the total amount of a specified type of expense (sum <type>)")
    print("6.Maximum amount per each expense type for a specified apartment (max <apartment>)")
    print("7.Sort:")
    print("\ta.Sort the apartments corresponding to the total amount of expenses (sort apartment)")
    print("\tb.Sort the types of expenses according to the total amount of each one (sort type)")
    print("8.Filter:")
    print("\ta.Filter a type of expense (filter <type>)")
    print("\tb.Filter keeping only expenses having an amount of money smaller than the given one (filter <value>)")
    print("8.Undo what it was already done (undo)")


def split_command(dict, list_max, history, command):
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
            add(dict, list_max, int(new_str[0]), new_str[1], int(new_str[2]))
            list = []
            convert_dict_list(dict, list)
            set_dict(history, list)
        except KeyError as ke:
            print(ke)

    elif token[0] == 'remove':
        if 'to' in token[1]:
            try:
                new_str = token[1].split(maxsplit=2)
                remove_to(dict, int(new_str[0]), int(new_str[2]))
                list=[]
                convert_dict_list(dict, list)
                set_dict(history, list)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)


        elif token[1][0] >='0' and token[1][0]<='9':
            try:
                remove_ap(dict,int(token[1]))
                list = []
                convert_dict_list(dict, list)
                set_dict(history, list)
            except ValueError as ve:
                 print(ve)

        else:
            try:
                remove_type(dict,token[1],1)
                list = []
                convert_dict_list(dict, list)
                set_dict(history, list)
            except KeyError as ke:
                print(ke)

    elif token[0] == 'replace':
        try:
            new_str = token[1].split(maxsplit=3)
            replace(dict, int(new_str[0]), new_str[1], int(new_str[3]))
            list = []
            convert_dict_list(dict, list)
            set_dict(history, list)
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

    elif token[0] == 'sum': #display the total amount for the expenses having type mentioned
        try:
            print("TOTAL "+token[1].upper()+': ',sum(dict,token[1]), "\n\n")
        except KeyError as ke:
            print(ke)

    elif token[0] == 'max':
        try:
            a = max(dict, list_max, int(token[1]))
            list_max_expense(list_max, a)
        except ValueError as ve:
            print(ve)

    elif token[0] == 'sort': #sort ap or type
        if token[1] == 'apartment':
            sort_ap(dict)
        elif token[1] == 'type':
            sort_type(dict)
        else:
            print("invalid value for sort")

    elif token[0] == 'filter':
        if (token[1][0] >= '0' and token[1][0] <= '9') or token[1][0] == '-':
            filter_am(dict,int(token[1]))
            list = []
            convert_dict_list(dict, list)
            set_dict(history, list)
        else:
            try:
                filter_type(dict,token[1])
                list = []
                convert_dict_list(dict, list)
                set_dict(history, list)
            except KeyError as ke:
                print(ke)

    elif token[0] == 'undo':
        try:
            undo(dict, history)
        except Exception as ex:
            print(ex)

    else:
        raise Exception("invalid input")


def console(dict,list_max,history):
    """

    :param dict: dictionary in which we keep all data about an apartment expenses
    :return: read the text
    """
    list = []
    convert_dict_list(dict, list)
    set_dict(history, list)

    while True:
        menu()
        command=str(input("How can I help you?"))
        try:
            if command.lower() == "exit":
                return
            split_command(dict, list_max, history, command)
        except Exception as ex:
            print(ex)
