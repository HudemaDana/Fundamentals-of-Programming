from src.exceptions.Exception import RepoPersonException, ServicePersonException


class ServicePerson:

    def __init__(self, repo_pers, repo_actv):
        self.repo_person = repo_pers
        self.repo_activity = repo_actv

    def get_data_person(self, p_id):
        for i in range(len(self.repo_person.person_repo)):
            if int(p_id) == int(self.repo_person.person_repo[i][0]):
                return self.repo_person.person_repo[i][1], self.repo_person.person_repo[i][2]
        raise ServicePersonException("No id found")


    # methods for 1

    def add_new_person(self, p_id, name, phone_number):
        try:
            self.repo_person.add_new_person(p_id, name, phone_number)
        except RepoPersonException as rp:
            raise ServicePersonException(rp)

    def remove_person(self, p_id):
        try:
            self.repo_person.remove_person(p_id)
        except RepoPersonException as rp:
            raise ServicePersonException(rp)

    def update_person(self, p_id, name="None", phone_number="None"):
        try:
            self.repo_person.update_person(p_id, name, phone_number)
        except RepoPersonException as rp:
            raise ServicePersonException(rp)

    @property
    def prepare_to_list_persons(self):
        """

        :return: it makes access to the repository through services, without having to import repository in UI
        """
        return self.repo_person.person_repo

    # methods for 3

    def search_person_name(self, text):
        """

        :param text: the text added by user
        :return: it appends in a list all the people which contain the text in name segment
        """
        list = []
        for i in range(len(text)):
            if text[i].isdigit():
                raise ServicePersonException("Name can't have digits")
        for i in range(len(self.repo_person.person_repo)):
            if text.lower() in self.repo_person.person_repo[i][1].lower():
                list.append(self.repo_person.person_repo[i])
        return list

    def search_person_phone_number(self, text):
        """

        :param text: the text added by user
        :return: it appends in a list all the people which contain the text in phone number segment
        """
        list = []
        for i in range(len(text)):
            if text[i].isalpha():
                raise ServicePersonException("Phone number can't have letters")
        for i in range(len(self.repo_person.person_repo)):
            if text in self.repo_person.person_repo[i][2]:
                list.append(self.repo_person.person_repo[i])
        return list
