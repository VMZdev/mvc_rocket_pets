from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable # Para puxar informações de pets table tambem

class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_conncetion = db_connection

    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.__db_conncetion as database:
            try:
                person_data = PeopleTable(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    pet_id=pet_id
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def get_person(self, person_id:int) -> PeopleTable:
        with self.__db_conncetion as database:
            try:
                person = (
                    database.session
                    .query(PeopleTable)
                    .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id) # Join serve para pegar uma pessoa e trazer as infos do pet dela. O Outer Join serve para trazer as infos da Pessoa mesmo que ela não tenha um pet associado
                    .filter(PeopleTable.id == person_id) # Apenas o person id que estamos isnerindo
                    .with_entities( # Definir quais colunas retornar
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PetsTable.name.label("pet_name"), # Label serve apenas para diferenciar o "first_name" do "name"
                        PetsTable.type.label("pet_type")
                    )
                    .one() # Buscar apenas 1 pessoa
                )
                return person
            except NoResultFound:
                return None
