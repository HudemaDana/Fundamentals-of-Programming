class Person:

    def __init__(self, person_id, name, phone_number):
        self._person_id = person_id
        self._name = name
        self._phone_number = phone_number

    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @property
    def phone_number(self):
        return self._phone_number

    @name.setter
    def name(self, val):
        self._name = val

    @phone_number.setter
    def phone_number(self, val):
        self._phone_number = val

