from typing import Dict
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None: # Quando eu tipo "PeopleRepositoryInterface" eu consigo fazer com que os métodos do "PeopleRepositoryInterface" sejam aplicaveis ao people_repository
        self.__people_repository = people_repository # Essa linha, junto com a tipagem acima, traz os metodos do "PeopleRepositoryInterface"

    def find(self, person_id: int) -> Dict: # Buscar as pessoas por ID e retornar um dicionario
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> PeopleTable: # Vou procurar um person ID e retornar uma info de PeopleTable
        person = self.__people_repository.get_person(person_id)
        if not person: # Se não tem pessoa
            raise HttpNotFoundError("Pessoa não encontrada!")
        
        return person

    def __format_response(self, person: PeopleTable) -> Dict: # Pegar uma info da People Table e retornar um Dict
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": { # como eu estou puxando um json, preciso me adequar ao formato dele para trazer as informações
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type
                }
            }
        }
