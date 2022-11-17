import random
from domain.taxi import Taxi


class RepoTaxi:
    def __init__(self):
        self.list_taxi = []
        self.random_generate()

    @property
    def get_list_taxi(self):
        return self.list_taxi

    def random_generate(self):
        """

        :return: generates the random taxis
        """
        nr_taxi = random.randint(1, 10)
        for i in range(nr_taxi):
            taxi_x = random.randint(0, 100)
            taxi_y = random.randint(0, 100)
            for j in range(len(self.list_taxi)):
                while abs(self.list_taxi[j].x_point - taxi_x) + abs(self.list_taxi[j].y_point - taxi_y) <= 5:
                    taxi_x = random.randint(0, 100)
                    taxi_y = random.randint(0, 100)
            self.list_taxi.append(Taxi(i, taxi_x, taxi_y))
