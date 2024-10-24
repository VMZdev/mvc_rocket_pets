import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

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
