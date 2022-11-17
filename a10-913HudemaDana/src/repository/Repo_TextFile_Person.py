from src.repository.Repo_Person import RepoPerson
from src.repository.Repo_TextFile_Activity import RepoFileTextActivity


class RepoFileTextPerson(RepoPerson):
    def __init__(self,repo_activity):
        super().__init__(repo_activity)
        self.file_name = "person.txt"
        self._load_file()
        self.repo_activity = repo_activity

    def _load_file(self):
        f = open(self.file_name, "rt")
        for line in f.readlines():
            p_id, sname, name, phone_number = line.split(' ', maxsplit=3)
            total_name = str(sname) + " " + str(name)
            self.add_new_person(p_id, total_name, phone_number.rstrip())
        f.close()

    def _save_file(self):
        f = open(self.file_name, "wt")
        for i in range(len(self._pers_data)):
            f.write(str(self._pers_data[i][0]) + " " + str(self._pers_data[i][1]) + " " + str(
                self._pers_data[i][2]) + '\n')
        f.close()

    def add_new_person(self, p_id, name, phone_number):
        super(RepoFileTextPerson, self).add_new_person(p_id, name, phone_number)
        self._save_file()


    def remove_person(self, p_id):
        super(RepoFileTextPerson, self).remove_person(p_id)
        self._save_file()
        self.repo_activity._save_file()



    def update_person(self, p_id, name="None", phone_number="None"):
        super(RepoFileTextPerson, self).update_person(p_id, name, phone_number)
        self._save_file()

#save person

    def random_generate(self):
        pass
