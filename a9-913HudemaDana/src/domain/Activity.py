class Activity:
    def __init__(self, activity_id, date, time, description="n/a", person_id=[]):
        self._activity_id = activity_id
        self._person_id = person_id
        self._date = date
        self._time = time
        self._description = description

    # getter
    @property
    def activity_id(self):
        return self._activity_id

    @property
    def person_id(self):
        return self._person_id

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._time

    @property
    def description(self):
        return self._description

    # setter
    @person_id.setter
    def person_id(self, val):
        self._person_id = val

    @date.setter
    def date(self, val):
        self._date = val

    @time.setter
    def time(self, val):
        self._time = val

    @description.setter
    def description(self, val):
        self._description = val

