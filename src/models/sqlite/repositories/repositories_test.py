''' Só estamos vendo qual é o retorno dos elementos, para usar em ambiente empresarial, não precisaremos dele'''

import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='interação com o banco')
def test_list_pets():
    ''' Teste para ver se o método list_pets() conecta com o banco e traz a informação correta'''
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

@pytest.mark.skip(reason='interação com o banco')
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason='interação com o banco')
def test_insert_person():
    first_name = "test_name"
    last_name = "test last"
    age = 77
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason='interação com o banco')
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
    print(response.pet_name) # Mostrar o nome do animal
