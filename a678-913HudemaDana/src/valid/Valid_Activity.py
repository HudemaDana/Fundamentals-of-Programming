from src.exceptions.Exception import ValidActivityException


class ValidActivity:
    def __init__(self, activity_id, date, time, description, person_id):
        self._activity_id = activity_id
        self._date = date
        self._time = time
        self._description = description
        self._person_id = person_id

    def valid_date(self):
        """

        :return: the method finds the cases in which a date is considered to be incorrect
        """
        token = self._date.split("-", maxsplit=2)
        if token[2].isdigit():
            if int(token[2]) <= 2020:
                raise ValidActivityException("User can't plan activities for precedent years")
        else:
            raise ValidActivityException("Incorrect input for year")

        if token[1].isdigit():
            if int(token[1]) > 12:
                raise ValidActivityException("The month doesn't exist")
        else:
            raise ValidActivityException("Incorrect input for month. Please try to write the number of the month")

        if token[0].isdigit():
            if int(token[0]) > 31:
                raise ValidActivityException("A month doesn't have so many days")
            if int(token[1]) == 2 and int(token[0]) > 29:
                raise ValidActivityException("February is a special month. It has less days then you entered")
        else:
            raise ValidActivityException("Incorrect input for day")

        return True

    def valid_time(self):
        """

        :return: the method finds the cases in which a time is considered to be incorrect
        """
        interval = self._time.split("-", maxsplit=1)
        if len(interval[0]) > 5:
            raise ValidActivityException("Invalid input for start time")
        else:
            token = interval[0].split(".", maxsplit=1)
            if not token[0].isdigit() or not token[1].isdigit():
                raise ValidActivityException("Incorrect values introduced for start time")

        if len(interval[1]) > 5:
            raise ValidActivityException("Invalid input for end time")
        else:
            token = interval[1].split(".", maxsplit=1)
            if not token[0].isdigit() or not token[1].isdigit():
                raise ValidActivityException("Incorrect values introduced for end time")

        return True




def test_valid_activity():

    valid = ValidActivity(1, "11-02-2021", "1t.00-14.30", "tennis club", [1, 2, 3, 5])
    try:
        assert valid.valid_time() == True
    except ValidActivityException as ve:
        assert str(ve) == "Incorrect values introduced for start time"

    valid = ValidActivity(1, "11-02-2021", "12.00-14.S0", "tennis club", [1, 2, 3, 5])
    try:
        assert valid.valid_time() == True
    except ValidActivityException as ve:
        assert str(ve) == "Incorrect values introduced for end time"

    valid = ValidActivity(1, "11-02-2021", "12.00-14.356", "tennis club", [1, 2, 3, 5])
    try:
        assert valid.valid_time() == True
    except ValidActivityException as ve:
        assert str(ve) == "Invalid input for end time"

    valid = ValidActivity(1, "30-02-2021", "12.00-14.30", "tennis club", [1, 2, 3, 5])
    try:
        assert valid.valid_date() == True
    except ValidActivityException as ve:
        assert str(ve) == "February is a special month. It has less days then you entered"


test_valid_activity()
