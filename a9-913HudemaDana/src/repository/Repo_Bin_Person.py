from src.repository.Repo_Person import RepoPerson
from src.repository.Repo_TextFile_Activity import RepoFileTextActivity
import pickle
import os

class RepoBinPerson(RepoPerson):
    def __init__(self,repo_activity):
        super().__init__(repo_activity)
        self.file_name = "person.bin"
        self._load_file()
        self.repo_activity = repo_activity

    def _load_file(self):
        if os.path.getsize(self.file_name)>0:
            f = open(self.file_name, "rb")
            self._pers_data = pickle.load(f)
            f.close()

    def _save_file(self):
        f = open(self.file_name, "wb")
        pickle.dump(self._pers_data, f)
        f.close()

    def add_new_person(self, p_id, name, phone_number):
        super(RepoBinPerson, self).add_new_person(p_id, name, phone_number)
        self._save_file()


    def remove_person(self, p_id):
        super(RepoBinPerson, self).remove_person(p_id)
        self._save_file()
        self.repo_activity._save_file()



    def update_person(self, p_id, name="None", phone_number="None"):
        super(RepoBinPerson, self).update_person(p_id, name, phone_number)
        self._save_file()


    def random_generate(self):
        pass
