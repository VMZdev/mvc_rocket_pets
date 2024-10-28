import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def test_create():
    person_infor = {
        "first_name": "Fulano",
        "last_name": "deTal",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_infor)

    assert response["data"]["type"] == "Person" # Assert (verificando se) o type da resposta é Person
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infor

def test_create_error(): # Importo a biblioteca Pytest para poder levantar as Exceptions
    person_infor = {
        "first_name": "Fulano123", # Ele vai passar se tiver erro (123), se eu tirar esse "123", ele vai dar erro
        "last_name": "deTal",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPeopleRepository)
    with pytest.raises(Exception):
        controller.create(person_infor)
