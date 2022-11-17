from src.exceptions.Exception import ValidPersonException

class ValidPerson:
    def __init__(self, person_id, name, phone_number):
        self._person_id = person_id
        self._name = name
        self._phone_number = phone_number

    def valid_name(self):
        """

        :return: the method finds the cases in which a name is considered to be incorrect
        """

        self._name.strip()
        name = self._name.split(" ", maxsplit=1)

        if name[0] == self._name:
            raise ValidPersonException("First name doesn't exist")

        if not name[0].isalpha():
            raise ValidPersonException("Last name is incorrect written")

        if not name[1].isalpha():
            raise ValidPersonException("First name is incorrect written")

        for i in range(0, len(name[1])):
            if i > 0 and name[1][i].isupper():
                raise ValidPersonException("Upper case letters found in first name")

        for i in range(0, len(name[0])):
            if i > 0 and name[0][i].isupper():
                raise ValidPersonException("Upper case letters found in last name")

        if name[1][0].islower():
            raise ValidPersonException("First name can't start with lower case")

        if name[0][0].islower():
            raise ValidPersonException("Last name can't start with lower case")

        return True

    def valid_phone_number(self):
        """

        :return: the method finds the cases in which a phone number is considered to be incorrect
        """

        if self._phone_number.isdigit() == False:
            raise ValidPersonException("This is not a phone number")
        elif len(str(self._phone_number)) != 10:
            raise ValidPersonException("Number has too many/few digits")

        return True


def test_valid_person():
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


test_valid_person()
