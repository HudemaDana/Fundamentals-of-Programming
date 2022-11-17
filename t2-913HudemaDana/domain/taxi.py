class Taxi:
    def __init__(self, id, x, y):
        self.id = id
        self.fare = 0
        self.x = x
        self.y = y

    @property
    def id_taxi(self):
        return self.id

    @property
    def x_point(self):
        return self.x

    @property
    def y_point(self):
        return self.y

    @property
    def fare_taxi(self):
        return self.fare

    @x_point.setter
    def x_point(self, val):
        self.x = val

    @y_point.setter
    def y_point(self, val):
        self.y = val

    @fare_taxi.setter
    def fare_taxi(self, val):
        self.fare = val
