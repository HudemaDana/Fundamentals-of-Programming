from domain.taxi import Taxi
import random


class Service:
    def __init__(self, repo_taxi):
        self.rt = repo_taxi

    @property
    def get_repo(self):
        return self.rt.get_list_taxi

    def add_ride(self, x1, y1, x2, y2):
        """

        :param x:
        :param y:
        :return: find the min distance and put the taxi there
        """
        min = 1000000
        for i in range(len(self.rt.get_list_taxi)):
            if (abs(self.rt.get_list_taxi[i].x_point - x1) + abs(self.rt.get_list_taxi[i].y_point - y1)) < min:
                min = abs(self.rt.get_list_taxi[i].x_point - x1) + abs(self.rt.get_list_taxi[i].y_point - y1)
                taxi = i
                fare = abs(x1 - x2) + abs(y1 - y2)
        self.rt.get_list_taxi[taxi] = Taxi(self.rt.get_list_taxi[taxi].id_taxi, x2, y2)
        self.rt.get_list_taxi[taxi].fare_taxi = self.rt.get_list_taxi[taxi].fare_taxi + fare

    def generate_rides(self, nr_rides):
        """

        :param nr_rides:
        :return: generates the random rides for simulation
        """
        new_list = []
        i = 0
        while i < nr_rides:
            taxi_x1 = random.randint(0, 100)
            taxi_y1 = random.randint(0, 100)
            taxi_x2 = random.randint(0, 100)
            taxi_y2 = random.randint(0, 100)

            while (abs(taxi_x1 - taxi_x2) + abs(taxi_y1 - taxi_y2)) < 10:
                taxi_x1 = random.randint(0, 100)
                taxi_y1 = random.randint(0, 100)
                taxi_x2 = random.randint(0, 100)
                taxi_y2 = random.randint(0, 100)
            new_list.append([i, taxi_x1, taxi_y1, taxi_x2, taxi_y2])
            i = i + 1

            return new_list

    def simulate_rides(self, nr_rides):
        list = []
        list = self.generate_rides(nr_rides)
        for i in range(nr_rides):
            self.add_ride(list[i][1], list[i][2], list[i][3], list[i][4])
