from src.domain.Activity import Activity
from src.valid.Valid_Activity import ValidActivity
from src.exceptions.Exception import RepoActivityException, ValidActivityException
from src.iterator_struct.Iterator_module import IteratorStructure
import random
from datetime import datetime

class RepoActivity:

    def __init__(self):
        self._act_data = IteratorStructure()
        self.random_generate_activity()

    def add_activity(self, activity):
        """
        :return: verifies if any unique data repeats and if so, it generates a new list of people until it finds it as
                 unique
        """
        for i in range(0, len(self._act_data.list)):
            if activity.date == self._act_data.list[i][1] and activity.time == self._act_data.list[i][2]:
                for j in range(0, len(self._act_data.list[i][4])):
                    while self._act_data.list[i][4][j] in activity.person_id:
                        activity.person_id = random.choice(self.generate_list_person())

        self._act_data.list.append(
            [activity.activity_id, activity.date, activity.time, activity.description, activity.person_id])

    @property
    def repo_activity(self):
        return self._act_data.list

    """
    generate a random list of activities
    """

    def generate_date(self):
        """

        :return:returns a list which is used as a generator of date for the repo
        """
        date = ["01-01-2021", "07-03-2021", "11-05-2021", "21-05-2021", "22-06-2021", "27-02-2021", "31-08-2021",
                "11-02-2021", "19-06-2022", "13-03-2022", "17-10-2022", "26-12-2022", "20-11-2022", "21-07-2021",
                "02-02-2022", "03-03-2022", "10-10-2022", "24-12-2021", "08-12-2022", "09-04-2022", "17-04-2021",
                "16-08-2022"]
        return date

    def generate_time(self):
        """

        :return: returns a list which is used as a generator of time for the repo
        """
        time = ["05.30-07.00", "06.00-07.30", "06.00-08.00", "06.30-08.00", "06.30-08.30", "07.00-08.30", "07.00-09.00",
                "7.30-9.00",
                "07.30-9.30", "08.00-9.30", "08.00-10.00", "08.30-10.00", "08.30-10.30", "09.00-10.30", "09.00-11.00",
                "09.30-11.30", "09.30-12.00",
                "10.00-11.30", "10.00-12.00", "10.30-12.00", "10.30-12.30", "11.00-12.30", "11.00-13.00", "11.30-13.00",
                "11.30-13.30", "12.00-13.30", "14.00-15.30", "16.00-17.30", "13.00-14.30", "15.00-16.30", "17.00-18.30",
                "19.00-20.30"]
        return time

    def generate_description(self):
        """

        :return: returns a list which is used as a generator of description for the repo
        """
        description = ["going to dinner    ", "running in the park", "starving myself    ", "paintball          ",
                       "going to gym       ", "cleaning the room  ", "tennis club        ", "dance club         ",
                       "theatre club       ", "take a nap         ", "study group        ", "climb a mountain   ",
                       "skating            "]
        return description

    def generate_list_person(self):
        """

        :return: returns a list which is used as a generator of groups of people for the repo
        """
        list = [[2, 4, 5], [1, 3, 4], [7, 8], [2, 7, 11, 19], [9, 10], [1, 2, 3, 4, 5], [5, 6, 7, 8, 9],
                [3, 5, 7, 9],
                [13, 15, 16, 19], [10, 12, 13], [18], [18, 19], [1, 11, 16], [2, 3], [4, 6, 8], [0, 1, 7],
                [0, 11, 13],
                [0, 3, 10, 16]]
        return list

    def random_generate_activity(self):
        """

        :return: creates 20 objects in the repo with random values extracted from some generators
        """
        for i in range(20):
            date = random.choice(self.generate_date())
            time = random.choice(self.generate_time())
            description = random.choice(self.generate_description())

            for j in range(len(self._act_data.list)):
                if self._act_data.list[j][1] == date and self._act_data.list[j][2] == time and self._act_data.list[j][
                    3] == description:
                    description = random.choice(self.generate_description())

            self.add_activity(Activity(i, date, time, description, random.choice(self.generate_list_person())))

    def add_activity1(self, activity_id, date, time, description, person_id, person):
        """

        :param activity_id: the id of the activity in data base
        :param date: the date in which the event takes place
        :param time:  the time in which the event takes place
        :param description: it shows to the person what is about to do at that activity
        :param person_id: a list of people that are going to participate to the activity
        :return: in order to add a new activity, we are looking if there isn't already one with the same id. If not we
                 are trying to add all data in associated repository. I case one of the data is invalid, an exception
                 will be raised.
        """

        for i in range(len(self.repo_activity)):
            if int(self.repo_activity[i][0]) == int(activity_id):
                raise RepoActivityException("This activity already exists")

        token = person_id.split(" ")
        for i in range(len(token)):
            token[i] = int(token[i])
            ok = 0
            for j in range(len(person)):
                if int(person[j][0]) == int(token[i]):
                    ok = 1
            if ok == 0:
                raise RepoActivityException("Person added in activity doesn't exist")

        valid = ValidActivity(activity_id, date, time, description, person_id)
        if valid.valid_time() and valid.valid_date():
            self.repo_activity.append([activity_id, date, time, description, token][:])
        else:
            raise RepoActivityException("Incorrect date/time")

        try:

            assert valid.valid_time() == True
            assert valid.valid_date() == True

        except ValidActivityException as vp:
            raise RepoActivityException(vp)

    def remove_activity(self, activity_id):
        """

        :param activity_id: the method receive an id of an activity
        :return: the method will try to find the id in the list of activities and remove it if exists. Otherwise it will
                 raise an exception
        """
        if int(activity_id) >= 0:
            ok = 0
            for i in range(len(self.repo_activity)):
                if int(self.repo_activity[i][0]) == int(activity_id):
                    self.repo_activity.pop(i)
                    ok = 1
                    break
            if ok == 0:
                raise RepoActivityException("ID doesn't exist")

        else:
            raise RepoActivityException("ID to be removed out of range")

    def update_activity(self, person, activity_id, date="None", time="None", description="None", person_id="None"):
        """

        :param activity_id: an id for activity where we want to make changes
        :param date: new date for an existing activity
        :param time: new time for an existing activity
        :param description: new description for an existing activity
        :param person_id: a new list of people that are going to perform an activity
        :return: the method is looking which one of the parameters is not null and replace the value in the list with
                a new one, added be user
        """

        try:
            if int(activity_id) >= 0:
                validity = ValidActivity(activity_id, date, time, description, person_id)
                if date != "None" and validity.valid_date():
                    for i in range(len(self.repo_activity)):
                        if int(self.repo_activity[i][0]) == int(activity_id):
                            self.repo_activity[i][1] = date

                if time != "None" and validity.valid_time():
                    for i in range(len(self.repo_activity)):
                        if int(self.repo_activity[i][0]) == int(activity_id):
                            self.repo_activity[i][2] = time

                if description != "None":
                    for i in range(len(self.repo_activity)):
                        if int(self.repo_activity[i][0]) == int(activity_id):
                            self.repo_activity[i][3] = description

                if person_id != "None":
                    token = person_id.split(" ")
                    for i in range(len(token)):
                        token[i] = int(token[i])
                        ok = 0
                        for j in range(len(person)):
                            if int(person[j][0]) == int(token[i]):
                                ok = 1
                        if ok == 0:
                            raise RepoActivityException("Person added in activity doesn't exist")

                    for i in range(len(self.repo_activity)):
                        if int(self.repo_activity[i][0]) == int(activity_id):
                            self.repo_activity[i][4] = token
            else:
                raise RepoActivityException("Incorrect input for ID")
        except ValidActivityException as va:
            raise RepoActivityException(va)


    def time_in_time(self, activity_time, fixed_time):
        """

        :param activity_time: interval in which an activity is performed
        :param fixed_time: time of an activity that we want to add to a person
        :return: the method verifies if the time of the new activity in a person schedule does not intersect other ones
        """

        token_activity_time = activity_time.split("-")
        token_fixed_time = fixed_time.split("-")
        time1 = datetime.strptime(token_activity_time[0], '%H.%M')
        time2 = datetime.strptime(token_activity_time[1], '%H.%M')
        time3 = datetime.strptime(token_fixed_time[0], '%H.%M')
        time4 = datetime.strptime(token_fixed_time[1], '%H.%M')

        if (time3 < time1 and time1 < time4) or (time3 < time2 and time2 < time4):
            return False
        return True

    def look_for_date_time(self, activity_id, person_id, date, time):
        """

        :param activity_id: activity id we want to add to a person
        :param person_id: a person form person list
        :param date: the date of the activity
        :param time: the time of the activity
        :return: it goes through activities and if the person is in one of them it verifies if it's at the same date and
                 time with the one we want to add
                      if True -> person can be added to the activity
                      if False -> person already is doing something else
        """
        verify = True
        for i in range(len(self.repo_activity)):
            if int(self.repo_activity[i][0]) != int(activity_id) and int(person_id) in \
                    self.repo_activity[i][4]:
                if self.repo_activity[i][1] == date:
                    verify = verify and self.time_in_time(self.repo_activity[i][2], time)

        return verify

    def add_activity_to_person(self, activity_id, person_id):
        """

        :param activity_id: activity in which we want to add a person
        :param person_id: person we want to add
        :return: if the person and activity id are valid, try to add the person to the activity if is not
                 intersecting with other one
        """
        ok = 0
        verify = True
        for i in range(len(self.repo_activity)):
            if int(self.repo_activity[i][0]) == int(activity_id):
                ok = 1
                if int(person_id) not in self.repo_activity[i][4]:
                    verify = self.look_for_date_time(activity_id, person_id, self.repo_activity[i][1],
                                                     self.repo_activity[i][2])
                    pos = i
                else:
                    raise RepoActivityException("Person already in activity")
        if ok == 0:
            raise RepoActivityException("Activity ID invalid")

        if verify == True:
            self.repo_activity[pos][4].append(int(person_id))
        else:
            raise RepoActivityException("Person has already other activity in this time interval")


    def remove_activity_from_person(self, activity_id, person_id):
        """

        :param activity_id: id of an activity we want to remove
        :param person_id: the person from which we want to remove the activity
        :return: the method verifies if person and activity id are valid and if so it removes the perosn prin the
                 activity list
        """
        ok = 0
        for i in range(len(self.repo_activity)):
            if int(self.repo_activity[i][0]) == int(activity_id):
                ok = 1
                if int(person_id) in self.repo_activity[i][4]:
                    self.repo_activity[i][4].remove(int(person_id))
                else:
                    raise RepoActivityException("Person ID is not in this activity")

        if ok == 0:
            raise RepoActivityException("Activity ID invalid")

