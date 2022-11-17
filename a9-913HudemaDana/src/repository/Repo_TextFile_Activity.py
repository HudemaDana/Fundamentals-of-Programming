from src.repository.Repo_Activity import RepoActivity
from src.domain.Activity import Activity


class RepoFileTextActivity(RepoActivity):
    def __init__(self):
        super().__init__()
        self.file_name = "activity.txt"
        self.load_file()

    def load_file(self):
        f = open(self.file_name, "rt")
        for line in f.readlines():
            a_id, date, time, descr_and_id_person = line.split(' ', maxsplit=3)
            descr, aproape_id_person = descr_and_id_person.rsplit('[', maxsplit=1)
            id_person = []
            for i in range(len(aproape_id_person)):
                if aproape_id_person[i].isdigit():
                    id_person.append(int(aproape_id_person[i]))

            self.add_activity(Activity(a_id, date, time, descr, id_person))
        f.close()

    def _save_file(self):
        f = open(self.file_name, "wt")
        for i in range(len(self._act_data)):
            f.write(str(self._act_data[i][0]) + " " + str(self._act_data[i][1]) + " " + str(
                self._act_data[i][2]) + " " + str(self._act_data[i][3]) + " " + str(
                self._act_data[i][4]) + '\n')
        f.close()

    def add_activity1(self, activity_id, date, time, description, person_id, person):
        super(RepoFileTextActivity, self).add_activity1(activity_id, date, time, description, person_id, person)
        self._save_file()

    def remove_activity(self, activity_id):
        super(RepoFileTextActivity, self).remove_activity(activity_id)
        self._save_file()

    def update_activity(self, person, activity_id, date="None", time="None", description="None", person_id="None"):
        super(RepoFileTextActivity, self).update_activity(person, activity_id, date, time,
                                                          description, person_id)
        self._save_file()

    def add_activity_to_person(self, activity_id, person_id):
        super(RepoFileTextActivity, self).add_activity_to_person(activity_id, person_id)
        self._save_file()

    def remove_activity_from_person(self, activity_id, person_id):
        super(RepoFileTextActivity, self).remove_activity_from_person(activity_id, person_id)
        self._save_file()

    def random_generate_activity(self):
        pass
