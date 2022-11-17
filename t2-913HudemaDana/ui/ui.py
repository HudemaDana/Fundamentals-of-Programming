class UI:
    def __init__(self, serv):
        self.st = serv

    def menu(self):
        print("\nTAXI SIMULATOR\n")
        print("------------------\n")
        print("1.ADD A RIDE")
        print("2.SIMULATE RIDE")
        print("0.WANT TO EXIT")
        print("------------------\n")

    def taxi_display(self):
        """
        displays taxis id and coordinates
        :return:
        """
        print("ID\tX_POINT\tY_POINT\tFARE")
        for i in range(len(self.st.get_repo)):
            print(str(self.st.get_repo[i].id_taxi) + "\t" + str(self.st.get_repo[i].x_point) + "\t\t" + str(
                self.st.get_repo[i].y_point)+"\t\t" + str(self.st.get_repo[i].fare_taxi))

    def controller(self):
        while True:
            self.menu()
            self.taxi_display()
            nr = input("choose what you want to do = ")
            if nr == '1':
                x1 = input("start point x = ")
                y1 = input("start point y = ")
                x2 = input("end point x = ")
                y2 = input("end point y = ")
                self.st.add_ride(int(x1), int(y1), int(x2), int(y2))
            elif nr == '2':
                nr =int(input("How many ride do you want to simulate = "))
                list =self.st.generate_rides(nr)
                for i in range(nr):
                   # self.st.add_ride(list[i][1], list[i][2], list[i][3], list[i][4])
                    self.taxi_display()
            else:
                return
