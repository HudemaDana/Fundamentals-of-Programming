import unittest

from src.exceptions.Exception import *
from src.domain.Activity import Activity
from src.domain.Person import Person
from src.repository.Repo_Activity import RepoActivity
from src.repository.Repo_Person import RepoPerson
from src.services.Service_Person import ServicePerson
from src.services.Service_Activity import ServiceActivity
from src.services.Service_Undo_Redo import ServiceUndoRedo
from src.valid.Valid_Activity import ValidActivity
from src.valid.Valid_Person import ValidPerson
import datetime


class TestActivity(unittest.TestCase):
    def test_activity_id(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        self.assertEqual(new_activity.activity_id, 10)

    def test_person_id(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        self.assertEqual(new_activity.person_id, [2, 3, 4])

    def test_date(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        self.assertEqual(new_activity.date, "10.02.2021")

    def test_time(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        self.assertEqual(new_activity.time, '12.00-16.00')

    def test_description(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        self.assertEqual(new_activity.description, "tennis club")

    def test_person_id_setter(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        new_activity.person_id = [1, 2, 3]
        self.assertEqual(new_activity.person_id, [1, 2, 3])

    def test_date_setter(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        new_activity.date = "11.03.1111"
        self.assertEqual(new_activity.date, "11.03.1111")

    def test_time_setter(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        new_activity.time = '13.30-14.00'
        self.assertEqual(new_activity.time, '13.30-14.00')

    def test_description_setter(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        new_activity.description = 'concert'
        self.assertEqual(new_activity.description, "concert")


class TestPerson(unittest.TestCase):
    def test_person_id(self):
        new_person = Person(5, "Gica Hagi", "0712345678")
        self.assertEqual(new_person.person_id, 5)

    def test_test_name(self):
        new_person = Person(5, "Gica Hagi", "0712345678")
        self.assertEqual(new_person.name, "Gica Hagi")

    def test_phone_number(self):
        new_person = Person(5, "Gica Hagi", "0712345678")
        self.assertEqual(new_person.phone_number, '0712345678')

    def test_test_name_setter(self):
        new_person = Person(5, "Gica Hagi", "0712345678")
        new_person.name = "Elon Musk"
        self.assertEqual(new_person.name, "Elon Musk")

    def test_phone_number_setter(self):
        new_person = Person(5, "Gica Hagi", "0712345678")
        new_person.phone_number = "0700000008"
        self.assertEqual(new_person.phone_number, "0700000008")


class TestRepoActivity(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = RepoActivity()
        self.repo_pers = RepoPerson()

    def tearDown(self) -> None:
        pass

    def test_add_activity1(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo.add_activity1(1, '01-01-2022', '12.00-15.00', "tennis club", '1', self.repo_pers.person_repo)
        self.assertRaises(RepoActivityException, self.repo.add_activity1, 1, '01-01-2022', '12.00-15.00', "tennis club",
                          '1', self.repo_pers.person_repo)
        self.assertRaises(RepoActivityException, self.repo.add_activity1, 2, '01-01-2022', '12.00-15.00', "tennis club",
                          '3', self.repo_pers.person_repo)

    def test_remove_activity(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo.add_activity1(1, '01-01-2022', '12.00-15.00', "tennis club", '1', self.repo_pers.person_repo)
        self.assertRaises(RepoActivityException,self.repo.remove_activity,-7)

    def test_update_activity(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo.add_activity1(1, '01-01-2022', '12.00-15.00', "tennis club", '1', self.repo_pers.person_repo)
        self.assertRaises(RepoActivityException, self.repo.update_activity, self.repo_pers.person_repo,1, '01-01-2022', '12.00-15.00', "tennis club", '7')
        self.assertRaises(RepoActivityException, self.repo.update_activity, self.repo_pers.person_repo, -3, '01-01-2022',
                          '12.00-15.00', "tennis club", '1')

    def test_repo_activity(self):
        new_activity = Activity(10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4])
        self.repo.add_activity(new_activity)
        self.assertEqual(len(self.repo.repo_activity), 1)

        self.assertEqual(self.repo.repo_activity[0], [10, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4]])

        self.repo.repo_activity = [[2, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4]]]
        self.assertEqual(self.repo.repo_activity, [[2, "10.02.2021", '12.00-16.00', "tennis club", [2, 3, 4]]])

        self.assertEqual(self.repo.generate_date(),
                         ["01-01-2021", "07-03-2021", "11-05-2021", "21-05-2021", "22-06-2021", "27-02-2021",
                          "31-08-2021",
                          "11-02-2021", "19-06-2022", "13-03-2022", "17-10-2022", "26-12-2022", "20-11-2022",
                          "21-07-2021",
                          "02-02-2022", "03-03-2022", "10-10-2022", "24-12-2021", "08-12-2022", "09-04-2022",
                          "17-04-2021",
                          "16-08-2022"])
        self.assertEqual(self.repo.generate_time(),
                         ["05.30-07.00", "06.00-07.30", "06.00-08.00", "06.30-08.00", "06.30-08.30", "07.00-08.30",
                          "07.00-09.00",
                          "7.30-9.00",
                          "07.30-9.30", "08.00-9.30", "08.00-10.00", "08.30-10.00", "08.30-10.30", "09.00-10.30",
                          "09.00-11.00",
                          "09.30-11.30", "09.30-12.00",
                          "10.00-11.30", "10.00-12.00", "10.30-12.00", "10.30-12.30", "11.00-12.30", "11.00-13.00",
                          "11.30-13.00",
                          "11.30-13.30", "12.00-13.30", "14.00-15.30", "16.00-17.30", "13.00-14.30", "15.00-16.30",
                          "17.00-18.30",
                          "19.00-20.30"])

        self.assertEqual(self.repo.generate_description(),
                         ["going to dinner    ", "running in the park", "starving myself    ", "paintball          ",
                          "going to gym       ", "cleaning the room  ", "tennis club        ", "dance club         ",
                          "theatre club       ", "take a nap         ", "study group        ", "climb a mountain   ",
                          "skating            "])
        self.assertEqual(self.repo.generate_list_person(),
                         [[2, 4, 5], [1, 3, 4], [7, 8], [2, 7, 11, 19], [9, 10], [1, 2, 3, 4, 5], [5, 6, 7, 8, 9],
                          [3, 5, 7, 9],
                          [13, 15, 16, 19], [10, 12, 13], [18], [18, 19], [1, 11, 16], [2, 3], [4, 6, 8], [0, 1, 7],
                          [0, 11, 13],
                          [0, 3, 10, 16]])

        self.repo.random_generate_activity()
        self.assertEqual(len(self.repo.repo_activity), 21)


class RepoPersonTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = RepoPerson()

    def tearDown(self) -> None:
        pass

    def test_repo_person(self):
        new_person = Person(5, "Gica Hagi", "0712345678")
        self.repo.add_person(new_person)

        self.assertEqual(len(self.repo.person_repo), 1)
        self.assertEqual(self.repo.person_repo[0], [5, "Gica Hagi", "0712345678"])

        self.repo.person_repo = [[6, "Bob TheBuilder", "0712345678"]]
        self.assertEqual(self.repo.person_repo, [[6, "Bob TheBuilder", "0712345678"]])

        self.assertEqual(self.repo.create_people_names(),
                         ["Joe Madison", "Jordan Doris", "Billy Abigail", "Bruce Julia", "Albert Judy", "Willie Grace",
                          "Gabriel Denise", "Logan Amber", "Alan Marilyn", "Juan Beverly", "Wayne Danielle",
                          "Roy Theresa",
                          "Ralph Sophia", "Randy Marie", "Eugene Diana", "Vincent Brittany", "Russell Natalie",
                          "Elijah Isabella", "Louis Charlotte", "Bobby Rose", "Philip Alexis", "Johnny Kayla",
                          "Kyle Lauren",
                          "Walter Joan", "Ethan Evelyn", "Jeremy Judith", "Harold Megan", "Keith Cheryl",
                          "Christian Andrea",
                          "Roger Hannah", "Noah Martha", "Gerald Jacqueline", "Carl Frances", "Terry Gloria",
                          "Sean Ann",
                          "Austin Teresa", "Arthur Kathryn", "Lawrence Sara", "Jesse Janice", "Dylan Jean",
                          "Bryan Alice",
                          "Bob Suricata"])

        self.assertEqual(self.repo.create_people_phone_number(),
                         ["0711222333", "0712345678", "0745678901", "0744555999", "0725486791", "0744689513",
                          "0715344783", "0732654987", "0789899045", "0746651048", "0700139788", "0705056056",
                          "0798088099", "0701011010", "0718922066", "0712034056", "0704606012", "0746464664",
                          "0707077070", "0791056473", "0740039206", "0744591284", "0735166958", "0722502037",
                          "0765895937", "0744239232", "0722617818", "0744587883", "0744595006", "0741623541",
                          "0740824433", "0751552174"])

        self.repo.random_generate()
        self.assertEqual(len(self.repo.person_repo), 21)


class ServiceActivityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_act = RepoActivity()
        self.repo_pers = RepoPerson()
        self.serv = ServiceActivity(self.repo_act, self.repo_pers)

    def tearDown(self) -> None:
        pass

    def test_create_list(self):
        self.serv.create_list()
        self.assertEqual(len(self.repo_act.repo_activity), 20)

    def test_person_in_activity(self):
        new_activity = Activity(1, '01-01-2022', '12.00-15.00', "tennis club", [1])
        self.repo_act.add_activity(new_activity)
        self.assertEqual(self.serv.person_in_activity(1), [1])

    def test_get_data_activity(self):
        new_activity = Activity(1, '01-01-2022', '12.00-15.00', "tennis club", [1])
        self.repo_act.add_activity(new_activity)
        self.assertRaises(ServiceActivityException, self.serv.get_data_activity, 2)
        self.assertEqual(self.serv.get_data_activity(1), ('01-01-2022', '12.00-15.00', "tennis club", [1]))

    def test_add_activity(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1')
        self.assertEqual(self.repo_act.repo_activity[0], [1, '01-01-2022', '12.00-15.00', "tennis club", [1]])
        self.assertRaises(ServiceActivityException, self.serv.add_activity, 1, '32-01-2022', '12.00-15.00',
                          "tennis club", '1')

    def test_remove_activity(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1')
        self.serv.add_activity(2, '01-01-2022', '16.00-18.00', "tennis club", '1')
        self.assertRaises(ServiceActivityException, self.serv.remove_activity, 3)
        self.serv.remove_activity(1)
        self.assertEqual(self.repo_act.repo_activity[0], [2, '01-01-2022', '16.00-18.00', "tennis club", [1]])

    def test_update_activity(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1')
        self.serv.update_activity(1, '02-02-2022', '11.00-11.30', 'sleep pls', '1')
        self.assertEqual(self.repo_act.repo_activity[0], [1, '02-02-2022', '11.00-11.30', 'sleep pls', [1]])

    def test_time_in_time(self):
        time1 = '12.00-13.00'
        time2 = '12.30-13.30'
        time3 = '14.00-15.00'

        self.assertEqual(self.serv.time_in_time(time1, time2), False)
        self.assertEqual(self.serv.time_in_time(time1, time3), True)

    def test_look_for_date_time(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1')
        self.assertEqual(self.serv.look_for_date_time(1, 2, '01-01-2022', '12.00-15.00'), True)

    def test_add_activity_to_person(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1')
        self.assertRaises(ServiceActivityException, self.serv.add_activity_to_person, 1, 1)
        self.assertRaises(ServiceActivityException, self.serv.add_activity_to_person, 3, 1)
        self.assertEqual(self.serv.add_activity_to_person(1, 2), None)

    def test_remove_activity_from_person(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1 2')
        self.assertRaises(ServiceActivityException, self.serv.remove_activity_from_person, 1, 3)
        self.assertRaises(ServiceActivityException, self.serv.remove_activity_from_person, 3, 1)
        self.serv.remove_activity_from_person(1, 1)
        self.assertEqual(self.repo_act.repo_activity[0], [1, '01-01-2022', '12.00-15.00', "tennis club", [2]])

    def test_search_activity_date(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1 2')
        self.assertRaises(ServiceActivityException, self.serv.search_activity_date, 'abcd')
        self.assertEqual(self.serv.search_activity_date('01'),
                         [[1, '01-01-2022', '12.00-15.00', "tennis club", [1, 2]]])

    def test_search_activity_time(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1 2')
        self.assertRaises(ServiceActivityException, self.serv.search_activity_time, 'abcd')
        self.assertEqual(self.serv.search_activity_time('12'),
                         [[1, '01-01-2022', '12.00-15.00', "tennis club", [1, 2]]])

    def test_search_activity_description(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '12.00-15.00', "tennis club", '1 2')
        self.assertEqual(self.serv.search_activity_description('te'),
                         [[1, '01-01-2022', '12.00-15.00', "tennis club", [1, 2]]])

    def test_transform_st_time(self):
        self.assertEqual(self.serv.transform_st_time('12.00-13.00'), datetime.datetime(1900, 1, 1, 12, 0))

    def test_sort_activities_by_st_time(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '13.00-15.00', "tennis club", '1')
        self.serv.add_activity(2, '01-01-2022', '14.00-16.00', "tennis club", '2')

        self.assertEqual(self.serv.sort_activities_by_st_time(self.repo_act.repo_activity),
                         [[1, '01-01-2022', '13.00-15.00', "tennis club", [1]],
                          [2, '01-01-2022', '14.00-16.00', "tennis club", [2]]])

    def test_transform_end_time(self):
        self.assertEqual(self.serv.transform_end_time('12.00-13.00'), datetime.datetime(1900, 1, 1, 13, 0))

    def test_busiest_days(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '13.00-16.00', "tennis club", '1')
        self.serv.add_activity(2, '01-01-2022', '12.00-16.00', "tennis club", '2')
        self.assertEqual(len(self.serv.busiest_days()), 1)

    def test_sort_after_free_time(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '13.00-15.00', "tennis club", '1')
        self.serv.add_activity(2, '01-01-2022', '13.00-16.00', "tennis club", '2')

        self.assertEqual(self.serv.sort_after_free_time(self.repo_act.repo_activity),
                         [[1, '01-01-2022', '13.00-15.00', "tennis club", [1]],
                          [2, '01-01-2022', '13.00-16.00', "tennis club", [2]]])

    def test_activities_for_a_person(self):
        new_person = Person(1, "Gica Hagi", "0712345678")
        self.repo_pers.add_person(new_person)
        self.repo_pers.add_person(Person(2, "Bob TheBuilder", '0700000008'))
        self.serv.add_activity(1, '01-01-2022', '13.00-15.00', "tennis club", '1')
        self.serv.add_activity(2, '01-01-2022', '16.00-18.00', "tennis club", '1')

        self.assertEqual(self.serv.activities_for_a_person(1), [[1, '01-01-2022', '13.00-15.00', 'tennis club', [1]],
                                                                [2, '01-01-2022', '16.00-18.00', 'tennis club', [1]]])


class ServicePersonTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_act = RepoActivity()
        self.repo_pers = RepoPerson()
        self.serv = ServicePerson(self.repo_pers, self.repo_act)

    def tearDown(self) -> None:
        pass

    def test_create_list(self):
        self.serv.create_list()
        self.assertEqual(len(self.repo_pers.person_repo), 20)

    def test_get_data_person(self):
        self.serv.add_new_person(1, "Gica Hagi", "0712345678")
        self.assertEqual(self.serv.get_data_person(1), ("Gica Hagi", "0712345678"))
        self.assertRaises(ServicePersonException, self.serv.get_data_person, 3)

    def test_add_person(self):
        self.serv.add_new_person(1, "Gica Hagi", "0712345678")
        self.assertEqual(self.repo_pers.person_repo, [[1, "Gica Hagi", "0712345678"]])
        self.assertRaises(ServicePersonException, self.serv.add_new_person, 1, "Vreau Somn", '0712112112')

    def test_remove_person(self):
        self.serv.add_new_person(1, "Gica Hagi", "0712345678")
        self.serv.add_new_person(2, "Bob Thebuilder", "0700000008")
        self.serv.remove_person(1)
        self.assertRaises(ServicePersonException, self.serv.remove_person, -3)
        self.assertEqual(self.repo_pers.person_repo, [[2, "Bob Thebuilder", "0700000008"]])

    def test_update_person(self):
        self.serv.add_new_person(1, "Gica Hagi", "0712345678")
        self.serv.add_new_person(2, "Bob Thebuilder", "0700000008")
        self.assertRaises(ServicePersonException, self.serv.update_person, 3, "Vreau Somn", '0712112112')
        self.serv.update_person(1, "Anton Maria", '0700000001')
        self.assertEqual(self.repo_pers.person_repo[0], [1, "Anton Maria", '0700000001'])

    def test_search_person_name(self):
        self.serv.add_new_person(1, "Gica Hagi", "0712345678")
        self.assertEqual(self.serv.search_person_name('gi'), [[1, "Gica Hagi", "0712345678"]])
        self.assertRaises(ServicePersonException, self.serv.search_person_name, '12')

    def test_search_person_phone_number(self):
        self.serv.add_new_person(1, "Gica Hagi", "0712345678")
        self.assertEqual(self.serv.search_person_phone_number('12'), [[1, "Gica Hagi", "0712345678"]])
        self.assertRaises(ServicePersonException, self.serv.search_person_phone_number, 'ab')


class ServiceUndoRedoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_act = RepoActivity()
        self.repo_pers = RepoPerson()
        self.serv = ServiceUndoRedo(self.repo_act, self.repo_pers)

    def tearDown(self) -> None:
        pass

    def test_add_to_undo_list(self):
        self.serv.add_to_undo_list([1, 2])
        self.assertEqual(len(self.serv.undo), 1)

    def test_undo_operation(self):
        self.assertRaises(ServiceUndoRedoException, self.serv.undo_operation)

    def test_redo_operation(self):
        self.assertRaises(ServiceUndoRedoException, self.serv.redo_operation)


class ValidActivityTest(unittest.TestCase):

    def test_valid_activity_time(self):
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

    def test_valid_activity_date(self):

        valid = ValidActivity(1, "30-02-2021", "12.00-14.30", "tennis club", [1, 2, 3, 5])
        try:
            assert valid.valid_date() == True
        except ValidActivityException as ve:
            assert str(ve) == "February is a special month. It has less days then you entered"


class ValidPersonTest(unittest.TestCase):

    def test_valid_person_name(self):
        new_person = ValidPerson(0, "Mitica", "0712340678")
        try:
            assert new_person.valid_name() == True
        except ValidPersonException as vp:
            assert str(vp) == "First name doesn't exist"

        new_person = ValidPerson(0, "Mitica GiCa", "0712340678")
        try:
            assert new_person.valid_name() == True
        except ValidPersonException as vp:
            assert str(vp) == "Upper case letters found in first name"

        new_person = ValidPerson(0, "MitIca Gica", "0712340678")
        try:
            assert new_person.valid_name() == True
        except ValidPersonException as vp:
            assert str(vp) == "Upper case letters found in last name"

        new_person = ValidPerson(0, "mitica Gica", "0712340678")
        try:
            assert new_person.valid_name() == True
        except ValidPersonException as vp:
            assert str(vp) == "Last name can't start with lower case"

        new_person = ValidPerson(0, "Mitica gica", "0712340678")
        try:
            assert new_person.valid_name() == True
        except ValidPersonException as vp:
            assert str(vp) == "First name can't start with lower case"

        new_person = ValidPerson(0, "Mitica Gica1", "0712340678")
        try:
            assert new_person.valid_name() == True
        except ValidPersonException as vp:
            assert str(vp) == "First name is incorrect written"

        new_person = ValidPerson(0, "Mi-tica Gica", "0712340678")
        try:
            assert new_person.valid_name() == True
        except ValidPersonException as vp:
            assert str(vp) == "Last name is incorrect written"

    def test_valid_person_phone_number(self):

        new_person = ValidPerson(0, "Mitica Gica", "07123406789")
        try:
            assert new_person.valid_phone_number() == True
        except ValidPersonException as vp:
            assert str(vp) == "Number has too many/few digits"

        new_person = ValidPerson(0, "Mitica Gica", "071A340678")
        try:
            assert new_person.valid_phone_number() == True
        except ValidPersonException as vp:
            assert str(vp) == "This is not a phone number"
