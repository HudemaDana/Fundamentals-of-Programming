from src.exceptions.Exception import ServicePersonException, ServiceActivityException, ServiceUndoRedoException
from functools import *


class UI:
    def __init__(self, serv_person, serv_activity, serv_undo_redo):
        self.sp = serv_person
        self.sa = serv_activity
        self.ur = serv_undo_redo

    def general_menu(self):
        print("------------------------------------")
        print("THIS IS AN ACTIVITY PLANNER\n\n")
        print("What would you like to do?")
        print("\t1. Manage persons and activities.")
        print("\t2. Add/Remove activities")
        print("\t3. Search for a person/activity")
        print("\t4. Create statistics")
        print("\t5. Undo/Redo")
        print()
        print("\t0. Nothing. I want to exit.\n")
        print("------------------------------------")

    def menu_1(self):
        print("------------------------------------")
        print("1. Add a person")
        print("2. Remove a person")
        print("3. Update a person")
        print("4. List all people")
        print()
        print("5. Add an activity")
        print("6. Remove an activity")
        print("7. Update an activity")
        print("8. List an activity")
        print()
        print("0. Exit this menu")
        print("------------------------------------")

    def menu_2(self):
        print("------------------------------------\n")
        print("1. Add an activity to a person")
        print("2. Remove an activity from a person")
        print()
        print("0. Exist this menu\n")
        print("------------------------------------")

    def menu_3(self):
        print("------------------------------------\n")
        print("Search: ")
        print("\t1.For a person")
        print("\t2.For an activity")
        print()
        print("0. Exist this menu\n")
        print("------------------------------------")

    def menu_3_1(self):
        print("------------------------------------\n")
        print("1. Search by name ")
        print("2. Search by phone number")
        print()
        print("0. Exist this menu\n")
        print("------------------------------------")

    def menu_3_2(self):
        print("------------------------------------\n")
        print("1. Search by date ")
        print("2. Search by time")
        print("3. Search by description")
        print()
        print("0. Exist this menu\n")
        print("------------------------------------")

    def menu_4(self):
        print("------------------------------------\n")
        print("1.List activities for a given date by their start time")
        print("2.List the busiest days")
        print("3.List upcoming activities in which a person is involved")
        print()
        print("0.Exit this menu\n")
        print("------------------------------------")

    def menu_5(self):
        print("------------------------------------\n")
        print("1.Undo")
        print("2.Redo")
        print()
        print("0. exit this menu\n")
        print("------------------------------------")

    def controller1(self):
        while True:
            self.menu_1()
            cmd1 = str(input("Here we go again deciding something ="))
            if cmd1 == '0':
                return
            elif cmd1 == '1':
                id = input("Enter id = ")
                name = input("Enter name = ")
                phone_number = input("Enter phone number = ")

                try:
                    self.sp.add_new_person(id, name, phone_number)
                    self.ur.add_to_undo_list(
                        [partial(self.sp.add_new_person, id, name, phone_number), partial(self.sp.remove_person, id)])
                except ServicePersonException as sp:
                    print(sp)

            elif cmd1 == '2':
                id = input("Enter id = ")

                try:
                    item = self.sa.person_in_activity(id)
                    name, phone = self.sp.get_data_person(id)

                    self.sp.remove_person(id)
                    self.ur.add_to_undo_list(
                        [partial(self.sp.remove_person, id), partial(self.sp.add_new_person, id, name, phone), item,
                         id])
                except ServicePersonException as sp:
                    print(sp)

            elif cmd1 == '3':
                id = input("Enter id = ")
                name = input("Enter name = ")
                phone_number = input("Enter phone number = ")

                try:
                    name_init, phone_init = self.sp.get_data_person(id)

                    self.sp.update_person(id, name, phone_number)
                    self.ur.add_to_undo_list([partial(self.sp.update_person, id, name, phone_number),
                                              partial(self.sp.update_person, id, name_init, phone_init)])
                except ServicePersonException as sp:
                    print(sp)

            elif cmd1 == '4':
                self.list_persons()

            elif cmd1 == '5':
                id = input("Enter id = ")
                date = input("Enter date = ")
                time = input("Enter time = ")
                description = input("Enter description =")
                person_id = input("Enter list of person id = ")
                try:

                    self.sa.add_activity(id, date, time, description, person_id)
                    self.ur.add_to_undo_list([partial(self.sa.add_activity, id, date, time, description, person_id),
                                              partial(self.sa.remove_activity, id)])
                except ServiceActivityException as ss:
                    print(ss)

            elif cmd1 == '6':
                id = input("Enter id = ")
                try:
                    date, time, description, person_id = self.sa.get_data_activity(id)

                    self.sa.remove_activity(id)
                    self.ur.add_to_undo_list([partial(self.sa.remove_activity, id),
                                              partial(self.sa.add_activity, id, date, time, description, person_id)])
                except ServiceActivityException as ss:
                    print(ss)

            elif cmd1 == '7':
                id = input("Enter id = ")
                date = input("Enter date = ")
                time = input("Enter time = ")
                description = input("Enter description =")
                person_id = input("Enter list of person id = ")
                try:
                    date_init, time_init, description_init, person_id_init = self.sa.get_data_activity(id)

                    self.sa.update_activity(id, date, time, description, person_id)
                    self.ur.add_to_undo_list([partial(self.sa.update_activity, id, date, time, description, person_id),
                                              partial(self.sa.update_activity, id, date_init, time_init,
                                                      description_init, person_id_init)])
                except ServiceActivityException as ss:
                    print(ss)

            elif cmd1 == '8':
                self.list_activities()
            else:
                print("invalid input")
                return

    def controller2(self):
        while True:
            self.menu_2()
            cmd2 = str(input("Here we go making another decision = "))
            if cmd2 == '0':
                return
            elif cmd2 == '1':
                activity_id = input("Enter activity id = ")
                person_id = input("Enter person id = ")
                try:

                    self.sa.add_activity_to_person(activity_id, person_id)
                    self.ur.add_to_undo_list([partial(self.sa.add_activity_to_person, activity_id, person_id),
                                              partial(self.sa.remove_activity_from_person, activity_id, person_id)])
                except ServiceActivityException as ss:
                    print(ss)

            elif cmd2 == '2':
                activity_id = input("Enter activity id = ")
                person_id = input("Enter person id = ")
                try:

                    self.sa.remove_activity_from_person(activity_id, person_id)
                    self.ur.add_to_undo_list([partial(self.sa.remove_activity_from_person, activity_id, person_id),
                                              partial(self.sa.add_activity_to_person, activity_id, person_id)])
                except ServiceActivityException as ss:
                    print(ss)
            else:
                print("invalid input")
                return

    def controller3(self):
        while True:
            self.menu_3()
            cmd3 = str(input("Here we go making another decision = "))
            if cmd3 == '0':
                return
            elif cmd3 == '1':
                self.controller3_1()
            elif cmd3 == '2':
                self.controller3_2()
            else:
                print("invalid input")
                return

    def controller3_1(self):
        while True:
            self.menu_3_1()
            cmd3_1 = str(input("Here we go making another decision = "))
            if cmd3_1 == '0':
                return
            elif cmd3_1 == '1':
                text = str(input("Enter text = "))
                try:
                    l = self.sp.search_person_name(text)
                    if len(l) > 0:
                        print("PERSON_ID\t\tNAME\t\tPHONE NUMBER")
                        for i in range(len(l)):
                            print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2])
                    else:
                        print("No person found")
                except ServicePersonException as ss:
                    print(ss)

            elif cmd3_1 == '2':
                text = str(input("Enter text = "))
                try:
                    l = self.sp.search_person_phone_number(text)
                    if len(l) > 0:
                        print("PERSON_ID\t\tNAME\t\tPHONE NUMBER")
                        for i in range(len(l)):
                            print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2])
                    else:
                        print("No person found")
                except ServicePersonException as ss:
                    print(ss)
            else:
                print("invalid input")
                return

    def controller3_2(self):
        while True:
            self.menu_3_2()
            cmd3_2 = str(input("Here we go making another decision = "))
            if cmd3_2 == '0':
                return
            elif cmd3_2 == '1':
                text = str(input("Enter text = "))
                try:
                    l = self.sa.search_activity_date(text)
                    if len(l) > 0:
                        print("ACTIVITY ID\t\tDATE\t\tTIME\t\tDESCRIPTION\t\tPERSON LIST")
                        for i in range(len(l)):
                            print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2], '\t\t', l[i][3], '\t\t', l[i][4])
                    else:
                        print("No activity found")
                except ServiceActivityException as ss:
                    print(ss)

            elif cmd3_2 == '2':
                text = str(input("Enter text = "))
                try:
                    l = self.sa.search_activity_time(text)
                    if len(l) > 0:
                        print("ACTIVITY ID\t\tDATE\t\tTIME\t\tDESCRIPTION\t\tPERSON LIST")
                        for i in range(len(l)):
                            print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2], '\t\t', l[i][3], '\t\t', l[i][4])
                    else:
                        print("No activity found")
                except ServiceActivityException as ss:
                    print(ss)

            elif cmd3_2 == '3':
                text = str(input("Enter text = "))
                l = self.sa.search_activity_description(text)
                if len(l) > 0:
                    print("ACTIVITY ID\t\tDATE\t\tTIME\t\tDESCRIPTION\t\tPERSON LIST")
                    for i in range(len(l)):
                        print(l[i][0], '\t\t', l[i][1], '\t\t', l[i][2], '\t\t', l[i][3], '\t\t', l[i][4])
                else:
                    print("No activity found")
            else:
                print("invalid input")
                return

    def controller4(self):
        while True:
            self.menu_4()
            cmd4 = str(input("Here we go making another decision = "))
            if cmd4 == '0':
                return
            elif cmd4 == '1':
                date = str(input("Enter date = "))
                l = self.sa.sort_activities_by_st_time(self.sa.search_activity_date(date))
                if len(l) > 0:
                    print("ACTIVITY ID\t\tDATE\t\tTIME\t\tDESCRIPTION\t\tPERSON LIST")
                    for i in range(len(l)):
                        print(l[i][0], '\t\t', l[i][1], '\t', l[i][2], '\t', l[i][3], '\t\t', l[i][4])
                else:
                    print("No activity found")

            elif cmd4 == '2':
                l = self.sa.sort_after_free_time(self.sa.busiest_days())
                if len(l) > 0:
                    print("DATE\t\tBUSY TIME")
                    for i in range(len(l)):
                        print(l[i][0], '\t\t', l[i][1])
                else:
                    print("No activity found")

            elif cmd4 == '3':
                person_id = str(input("Enter person ID = "))
                l = self.sa.activities_for_a_person(person_id)
                if len(l) > 0:
                    print("ACTIVITY ID\t\tDATE\t\tTIME\t\tDESCRIPTION\t\tPERSON LIST")
                    for i in range(len(l)):
                        print(l[i][0], '\t\t', l[i][1], '\t', l[i][2], '\t', l[i][3], '\t\t', l[i][4])
                else:
                    print("No activity found")
            else:
                print("invalid input")
                return

    def controller5(self):
        while True:
            self.menu_5()
            cmd = str(input("Do you want to make undo or redo?"))
            if cmd == '0':
                return
            if cmd == '1':
                try:
                    self.ur.undo_operation()
                except ServiceUndoRedoException as su:
                    print(su)
            elif cmd == '2':
                try:
                    self.ur.redo_operation()
                except ServiceUndoRedoException as su:
                    print(su)
            else:
                print("invalid command")
                return

    def controller(self):
        while True:
            self.general_menu()
            cmd = str(input("Now what = "))
            if cmd == '0':
                return
            elif cmd == '1':
                self.controller1()
            elif cmd == '2':
                self.controller2()
            elif cmd == '3':
                self.controller3()
            elif cmd == '4':
                self.controller4()
            elif cmd == '5':
                self.controller5()
            else:
                print("invalid command")

    # methods associated with the assignment

    # methos for 1
    def list_persons(self):
        print("PERSON\t\tNAME\t\tPHONE NUMBER")
        if len(self.sp.prepare_to_list_persons) > 0:
            for i in range(0, len(self.sp.prepare_to_list_persons)):
                print(str(self.sp.prepare_to_list_persons[i][0]) + "\t\t" +
                      str(self.sp.prepare_to_list_persons[i][1]) + "\t\t " + str(self.sp.prepare_to_list_persons[i][2]))
        else:
            print("There are no more persons to be listed")

    def list_activities(self):
        print("ACTIVITY\t\tDATE\t\tTIME\t\tDESCRIPTION\t\tPEOPLE")
        if len(self.sa.prepare_to_list_activities) > 0:
            for i in range(len(self.sa.prepare_to_list_activities)):
                print(str(self.sa.prepare_to_list_activities[i][0]) + "\t\t" + str(
                    self.sa.prepare_to_list_activities[i][1]) + "\t\t" + str(
                    self.sa.prepare_to_list_activities[i][2]) + "\t\t" + str(
                    self.sa.prepare_to_list_activities[i][3]) + "\t\t" + str(self.sa.prepare_to_list_activities[i][4]))
