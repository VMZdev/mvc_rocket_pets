from typing import Dict
import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None: # Quando eu tipo "PeopleRepositoryInterface" eu consigo fazer com que os métodos do "PeopleRepositoryInterface" sejam aplicaveis ao people_repository
        self.__people_repository = people_repository # Essa linha, junto com a tipagem acima, traz os metodos do "PeopleRepositoryInterface"

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name) # Estou jogando meu método privado no meu método público para validar se não contém caracteres especiais
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formated_response = self.__format_response(person_info)
        return formated_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressão regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise HttpBadRequestError("Nome da pessoa inválido!")
        
    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id) # Inserindo pessoas com o método "insert_person" CRIADO NO PEOPLE REPOSITORY

    def __format_response(self, person_info:Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
