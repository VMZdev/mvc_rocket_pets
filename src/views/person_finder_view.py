from src.controllers.interfaces.person_finder_controller import PersonFinderControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PersonFinderView(ViewInterface): # Trouxe a interface que obriga as views a implementar o método "handle"

    def __init__(self, controller: PersonFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["person_id"]
        body_response = self.__controller.find(person_id)

        return HttpResponse(status_code=200, body=body_response)
