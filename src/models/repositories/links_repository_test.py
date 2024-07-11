import uuid
import pytest
from .links_repository import LinksRepository
from src.models.settings.db_conection_handler import db_connection_handler

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="Interaccion con el banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "solamentelink.com",
        "title": "Hotel"
    }
    link_repository.registry_link(link_infos)


@pytest.mark.skip(reason="Interaccion con el banco")
def test_find_links_from_trips():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    response = link_repository.find_link_from_trip(trip_id)
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], tuple)
