from src.exceptions.Exception import ServiceActivityException, RepoActivityException
from datetime import datetime


class ServiceActivity:
    def __init__(self, repo_act, repo_pers):
        self.repo_activity = repo_act
        self.repo_person = repo_pers

    def person_in_activity(self, p_id):
        item = []
        for i in range(len(self.repo_activity.repo_activity)):
            if p_id in self.repo_activity.repo_activity[i][4]:
                item.append(self.repo_activity.repo_activity[i][0])
        return item

    def get_data_activity(self, a_id):
        for i in range(len(self.repo_activity.repo_activity)):
            if int(a_id) == int(self.repo_activity.repo_activity[i][0]):
                return self.repo_activity.repo_activity[i][1], self.repo_activity.repo_activity[i][2], \
                       self.repo_activity.repo_activity[i][3], self.repo_activity.repo_activity[i][4]
        raise ServiceActivityException("No id found")

    # methods for 1

    def add_activity(self, activity_id, date, time, description, person_id):
        try:
            self.repo_activity.add_activity1(activity_id, date, time, description, person_id,
                                             self.repo_person.person_repo)
        except RepoActivityException as ra:
            raise ServiceActivityException(ra)

    def remove_activity(self, activity_id):
        try:
            self.repo_activity.remove_activity(activity_id)
        except RepoActivityException as ra:
            raise ServiceActivityException(ra)

    def update_activity(self, activity_id, date="None", time="None", description="None", person_id="None"):
        try:
            self.repo_activity.update_activity(self.repo_person.person_repo, activity_id, date, time, description,
                                               person_id)
        except RepoActivityException as ra:
            raise ServiceActivityException(ra)

    @property
    def prepare_to_list_activities(self):
        """

        :return: it makes access to the repository through services, without having to import repository in UI
        """
        return self.repo_activity.repo_activity

    # methods for 2

    def add_activity_to_person(self, activity_id, person_id):
        """

        :param activity_id: activity in which we want to add a person
        :param person_id: person we want to add
        :return: if the person and activity id are valid, try to add the person to the activity if is not
                 intersecting with other one
        """
        try:
            self.repo_activity.add_activity_to_person(activity_id,person_id)
        except RepoActivityException as ra:
            raise ServiceActivityException(ra)

    def remove_activity_from_person(self, activity_id, person_id):
        """

        :param activity_id: id of an activity we want to remove
        :param person_id: the person from which we want to remove the activity
        :return: the method verifies if person and activity id are valid and if so it removes the perosn prin the
                 activity list
        """
        try:
            self.repo_activity.remove_activity_from_person(activity_id,person_id)
        except RepoActivityException as ra:
            raise ServiceActivityException(ra)

    # methods for 3

    def search_activity_date(self, text):
        """

        :param text: the text added by user
        :return: it appends in a list all the activities which contain the text in date segment
        """
        list = []
        for i in range(len(text)):
            if text[i].isalpha():
                raise ServiceActivityException("Date can't have letters")
        for i in range(len(self.repo_activity.repo_activity)):
            if text in self.repo_activity.repo_activity[i][1]:
                list.append(self.repo_activity.repo_activity[i])

        return list

    def search_activity_time(self, text):
        """

        :param text: the text added by user
        :return: it appends in a list all the activities which contain the text in time segment
        """
        list = []
        for i in range(len(text)):
            if text[i].isalpha():
                raise ServiceActivityException("Time can't have letters")
        for i in range(len(self.repo_activity.repo_activity)):
            if text in self.repo_activity.repo_activity[i][2]:
                list.append(self.repo_activity.repo_activity[i])

        return list

    def search_activity_description(self, text):
        """

        :param text: the text added by user
        :return: it appends in a list all the activities which contain the text in description segment
        """
        list = []
        for i in range(len(self.repo_activity.repo_activity)):
            if text in self.repo_activity.repo_activity[i][3]:
                list.append(self.repo_activity.repo_activity[i])

        return list

    # methods for 4

    def transform_st_time(self, str_time):
        """

        :param str_time: a string that represents an interval of time
        :return: returns starting time of an activity, having the type of datetime
        """
        time = str_time.split('-', maxsplit=1)
        start_time = datetime.strptime(time[0], '%H.%M')

        return start_time

    def sort_activities_by_st_time(self, list):
        """

        :param list: a list of activities in format of a repo
        :return: it returns a list which is sorted by the starting time of the activities
        """
        i = 0
        while i < len(list) - 1:
            poz = i
            j = i + 1
            while j < len(list):
                if self.transform_st_time(list[j][2]) < self.transform_st_time(list[poz][2]):
                    poz = j
                j += 1
            aux = list[i]
            list[i] = list[poz]
            list[poz] = aux
            i += 1
        return list

    def transform_end_time(self, str_time):
        """

        :param str_time: a string that represents an interval of time
        :return: returns ending time of an activity, having the type of datetime
        """
        time = str_time.split('-', maxsplit=1)
        end_time = datetime.strptime(time[1], '%H.%M')

        return end_time

    def busiest_days(self):
        """

        :return: it returns a list in which are uniquely added activities dates and the total amount of busy time in
                 that day
        """
        list = []
        for i in range(len(self.repo_activity.repo_activity)):
            if self.transform_date_time(self.repo_activity.repo_activity[i][1],
                                        self.repo_activity.repo_activity[i][2]) > datetime.now():
                ok = 0
                for j in range(len(list)):
                    if self.repo_activity.repo_activity[i][1] in list[j]:
                        ok = 1
                        list[j][1] += self.transform_end_time(
                            self.repo_activity.repo_activity[i][2]) - self.transform_st_time(
                            self.repo_activity.repo_activity[i][2])
                if ok == 0:
                    list.append([self.repo_activity.repo_activity[i][1], self.transform_end_time(
                        self.repo_activity.repo_activity[i][2]) - self.transform_st_time(
                        self.repo_activity.repo_activity[i][2])])

        return list

    def sort_after_free_time(self, list):
        """

        :param list: contains a list of dates and how much time take for all activities to be performed in that day
        :return: it returns a list which is sorted by time
        """
        i = 0
        while i < len(list) - 1:
            poz = i
            j = i + 1
            while j < len(list):
                if list[j][1] < list[poz][1]:
                    poz = j
                j += 1
            aux = list[i]
            list[i] = list[poz]
            list[poz] = aux
            i += 1

        return list

    def transform_date_time(self, act_date, act_time):
        """

        :param act_date: a date of an activity
        :param act_time: interval of time of an activity
        :return: returns the date and time when the activity starts as an datetime value
        """
        time = act_time.split('-', maxsplit=1)
        date_time = act_date + ' ' + time[0]
        date_of_activity = datetime.strptime(date_time, '%d-%m-%Y %H.%M')

        return date_of_activity

    def activities_for_a_person(self, person_id):
        """

        :param person_id: a person we want to find in activity list
        :return: returns a list of upcoming activities in which the person is involved
        """
        list = []
        for i in range(len(self.repo_activity.repo_activity)):
            if int(person_id) in self.repo_activity.repo_activity[i][4]:
                if self.transform_date_time(self.repo_activity.repo_activity[i][1],
                                            self.repo_activity.repo_activity[i][2]) > datetime.now():
                    list.append(self.repo_activity.repo_activity[i])
        return list
