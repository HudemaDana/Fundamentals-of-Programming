from src.repository.Repo_Activity import RepoActivity
from src.domain.Activity import Activity
import pickle
import os

class RepoBinActivity(RepoActivity):
    def __init__(self):
        super().__init__()
        self.file_name = "activity.bin"
        self._load_file()

    def _load_file(self):
        if os.path.getsize(self.file_name)>0:
            f = open(self.file_name, "rb")  # rt -> read, binary
            self._act_data = pickle.load(f)
            f.close()

    def _save_file(self):
        f = open(self.file_name, "wb")  # wb -> write, binary
        pickle.dump(self._act_data, f)
        f.close()

    def add_activity1(self, activity_id, date, time, description, person_id, person):
        super(RepoBinActivity, self).add_activity1(activity_id, date, time, description, person_id, person)
        self._save_file()

    def remove_activity(self, activity_id):
        super(RepoBinActivity, self).remove_activity(activity_id)
        self._save_file()

    def update_activity(self, person, activity_id, date="None", time="None", description="None", person_id="None"):
        super(RepoBinActivity, self).update_activity(person, activity_id, date, time,
                                                     description, person_id)
        self._save_file()

    def add_activity_to_person(self, activity_id, person_id):
        super(RepoBinActivity, self).add_activity_to_person(activity_id, person_id)
        self._save_file()

    def remove_activity_from_person(self, activity_id, person_id):
        super(RepoBinActivity, self).remove_activity_from_person(activity_id, person_id)
        self._save_file()

    def random_generate_activity(self):
        pass
