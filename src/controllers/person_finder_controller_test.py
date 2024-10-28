#pylint: disable=unused-argument
from .person_finder_controller import PersonFinderController # Quem eu quero testar

class MockPerson():
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockPerson(
            first_name="John",
            last_name="Doe",
            pet_name="Fluffy",
            pet_type="cat"
        )

def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(123)

    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": { # como eu estou puxando um json, preciso me adequar ao formato dele para trazer as informações
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Fluffy",
                "pet_type": "cat"
                }
            }
        }
    
    assert response == expected_response
