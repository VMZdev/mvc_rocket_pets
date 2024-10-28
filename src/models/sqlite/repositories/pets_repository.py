from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetsRepository(PetsRepositoryInterface): # Essa dependência do pai faz com que obrigue a classe a definir os metodos de "list" e "delete"
    def __init__(self, db_connection) -> None:
        self.__dbconnection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__dbconnection as database:
            try:
                pets = (database
                        .session
                        .query(PetsTable)
                        .all())
                return pets
            except NoResultFound:
                return []
            
    def delete_pets(self, name: str) -> None:
        with self.__dbconnection as database:
            try:
                (
                database.session
                .query(PetsTable)
                .filter(PetsTable.name == name)
                .delete()
                )
                database.session.commit() # Fazer um commit no banco de dados. FUNCIONA PARA ALTERAÇÕES DE DADOS (CUD)
            except Exception as exception:
                database.session.rollback() # Se algo der errado, volte o banco para o mesmo estado que ele estava antes
                raise exception
