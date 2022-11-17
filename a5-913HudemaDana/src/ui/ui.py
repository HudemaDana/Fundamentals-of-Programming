from src.services.services import Services
from src.services.test import Test


class UI:
    def write_list(self, list):
        """

        :param list: the list of complex numbers
        :return:
        if Re and Im is 0, means the number is 0
        if Re is 0, means we have just the Im part
        if Im is 0, means we have just the Re part
        otherwise we have a complex number which contains Re and Im
        """
        for i in range(0, len(list)):
            if list[i][0] == 0 and list[i][1] == 0:
                print(0)

            elif list[i][0] == 0:
                print(list[i][1], 'i')

            elif list[i][1] == 0:
                print(list[i][0])

            else:
                print(list[i][0], '+ ', list[i][1], 'i')

    def write_menu(self):
        print("----------------------------------------")
        print("\nChoose one of the following features:")
        print("\t1. Add a number")
        print("\t2. Display all the numbers")
        print(
            "\t3. Filter the list so that it contains only the numbers between indices start and end, where these values are read from the console ")
        print("\t4. Undo the last operation")
        print("\t5. To exit the program\n")
        print("----------------------------------------")

    def console(self, list, backup):
        """

        :param list: list of complex numbers
        :param backup: a list which contains the history of all operations
        :return: reads a text and based on it, program is going to solve a certain requirement
        """
        while True:
            self.write_menu()
            command = str(input("How can I help you?"))
            if command == '1':
                re = input("Re = ")
                im = input("Im = ")

                try:
                    re = int(re)
                    im = int(im)

                    s.add(list, int(re), int(im))
                    s.set_list(backup, list)
                except Exception:
                    print("Invalid value")


            elif command == '2':
                self.write_list(list)

            elif command == '3':
                try:
                    start = input("Start = ")
                    end = input("End = ")
                    try:
                        start = int(start)
                        end = int(end)
                        list = s.filter(list, start, end)
                        s.set_list(backup, list)
                    except Exception:
                        print("Invalid value")

                except ValueError as ve:
                    print(ve)

            elif command == '4':
                try:
                    backup, list = s.undo(backup)
                except Exception as ex:
                    print(ex)

            elif command == '5':
                return
            else:
                print("Invalid value")

    def main(self):
        backup = []
        list = s.get_nums()
        s.set_list(backup, list)

        Test().tests()
        self.console(list, backup)


s = Services()
u = UI()
u.main()
