from app.connectapp.models import Person  # noqa
from app.connectapp.schemas import PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from app.connectapp.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
