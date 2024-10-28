from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface
from src.validators.person_creator_validator import person_creator_validator 
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PersonCreatorView(ViewInterface): # Trouxe a interface que obriga as views a implementar o método "handle"

    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_creator_validator(http_request) # Validar o Body, pra ver se ele esta atendendo o que esá sendo pedido
        
        person_info = http_request.body # As informações "person_info" vão vir do "http_request.body"
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
