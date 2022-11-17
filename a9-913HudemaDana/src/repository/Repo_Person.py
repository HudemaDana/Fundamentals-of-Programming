from src.domain.Person import Person
from src.valid.Valid_Person import ValidPerson
from src.exceptions.Exception import ValidPersonException, RepoPersonException
import random


class RepoPerson:

    def __init__(self,repo_activity):
        self._pers_data = []
        self.activity = repo_activity
        self.random_generate()

    def add_person(self, person):
        """
        :return: adds data about a person into a list that is used as repository
        """
        self._pers_data.append([person.person_id, person.name, person.phone_number][:])

    @property
    def person_repo(self):
        return self._pers_data

    def __getitem__(self, item):
        return self._pers_data[item]

    @person_repo.setter
    def person_repo(self, new_list):
        self._pers_data = new_list

    """
    from here we have the code for a random generated repo
    """

    def create_people_names(self):
        """

        :return: returns a list which is used as a generator of names for people in the repository
        """
        people_names = ["Joe Madison", "Jordan Doris", "Billy Abigail", "Bruce Julia", "Albert Judy", "Willie Grace",
                        "Gabriel Denise", "Logan Amber", "Alan Marilyn", "Juan Beverly", "Wayne Danielle",
                        "Roy Theresa",
                        "Ralph Sophia", "Randy Marie", "Eugene Diana", "Vincent Brittany", "Russell Natalie",
                        "Elijah Isabella", "Louis Charlotte", "Bobby Rose", "Philip Alexis", "Johnny Kayla",
                        "Kyle Lauren",
                        "Walter Joan", "Ethan Evelyn", "Jeremy Judith", "Harold Megan", "Keith Cheryl",
                        "Christian Andrea",
                        "Roger Hannah", "Noah Martha", "Gerald Jacqueline", "Carl Frances", "Terry Gloria", "Sean Ann",
                        "Austin Teresa", "Arthur Kathryn", "Lawrence Sara", "Jesse Janice", "Dylan Jean", "Bryan Alice",
                        "Bob Suricata"]
        return people_names

    def create_people_phone_number(self):
        """

        :return: returns a list which is used as a generator of phone numbers for the repo
        """
        phone_numbers = ["0711222333", "0712345678", "0745678901", "0744555999", "0725486791", "0744689513",
                         "0715344783", "0732654987", "0789899045", "0746651048", "0700139788", "0705056056",
                         "0798088099", "0701011010", "0718922066", "0712034056", "0704606012", "0746464664",
                         "0707077070", "0791056473", "0740039206", "0744591284", "0735166958", "0722502037",
                         "0765895937", "0744239232", "0722617818", "0744587883", "0744595006", "0741623541",
                         "0740824433", "0751552174"]
        return phone_numbers

    def random_generate(self):
        """

        :return: creates 20 objects in the repo with random values extracted from some generators
        """
        for i in range(20):
            phone = random.choice(self.create_people_phone_number())
            ok = 1
            while ok:
                ok = 0
                for j in range(0, len(self._pers_data)):
                    if self._pers_data[j][2] == phone:
                        ok = 1
                        phone = random.choice(self.create_people_phone_number())

            self.add_person(
                Person(i, random.choice(self.create_people_names()), phone))

    def save_person(self,p_id, name, phone_number):
        self.person_repo.append([p_id, name, phone_number][:])

    def add_new_person(self, p_id, name, phone_number):
        """

        :param p_id: a person id
        :param name: name for the person added
        :param phone_number: a phone number for the person added
        :return: in case the id does not already exists and the name and phone number are valid, we add
                 the person in the repository
        """
        try:
            validity = ValidPerson(p_id, name, phone_number)
            for i in range(0, len(self.person_repo)):
                if p_id == self.person_repo[i][0]:
                    raise RepoPersonException("This ID already exist")

            if validity.valid_name() and validity.valid_phone_number():
                 self.save_person(p_id, name, phone_number)
        except ValidPersonException as vp:
            raise RepoPersonException(vp)

    def remove_person(self, p_id):
        """

        :param p_id: the id of the person we want to remove
        :return: In case the id is valid, the method removes the person from the person list. Otherwise it raises
                  an exception
        """

        if int(p_id) >= 0:

            for i in range(len(self.activity.repo_activity)):
                if int(p_id) in self.activity.repo_activity[i][4]:
                    self.activity.repo_activity[i][4].remove(int(p_id))

            for i in range(len(self.person_repo)):
                if int(self.person_repo[i][0]) == int(p_id):
                    self.person_repo.pop(i)
                    break

        else:
            raise RepoPersonException("ID to be removed out of range")

    def update_person(self, p_id, name="None", phone_number="None"):
        """

        :param p_id: id of the person we want to change data about
        :param name: the new name for an existing person
        :param phone_number: the new phone_number for an existing person
        :return: In case we have valid and not null data, we put it in the place of the old one. Otherwise we raise an
                 exception
        """
        try:
            if int(p_id) >= 0:
                validity = ValidPerson(p_id, name, phone_number)
                ok = 0
                if name != "None" and validity.valid_name():
                    for i in range(0, len(self.person_repo)):
                        if int(self.person_repo[i][0]) == int(p_id):
                            self.person_repo[i][1] = name
                            ok = 1

                if phone_number != "None" and validity.valid_phone_number():
                    for i in range(0, len(self.person_repo)):
                        if int(self.person_repo[i][0]) == int(p_id):
                            self.person_repo[i][2] = phone_number
                            ok = 1

                if ok == 0:
                    raise RepoPersonException("ID doesn't exist")

            else:
                raise RepoPersonException("ID to be updated out of range")
        except ValidPersonException as vp:
            raise RepoPersonException(vp)
