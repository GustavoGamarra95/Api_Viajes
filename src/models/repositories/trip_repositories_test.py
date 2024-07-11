import sqlite3
import uuid
from datetime import datetime, timedelta
import pytest

from src.models.repositories.trips_repository import TripsRepository


@pytest.mark.skip(reason="Interaccion con el banco")
def test_create_trip():
    db_file = "/home/gustavo/Escritorio/curso python/storage.db"
    conn = sqlite3.connect(db_file)
    trips_repository = TripsRepository(conn)

    trip_id = str(uuid.uuid4())
    print()
    print(f"Id : {trip_id}")
    trips_infos = {
        "id": trip_id,
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com"
    }
    trips_repository.create_trip(trips_infos)

    trip = trips_repository.find_trip_by_id(trip_id)
    assert trip[1] == "Osasco"
    assert trip[2] == "2024-01-02"
    assert trip[3] == "2024-01-07"
    assert trip[4] == "Osvaldo"
    assert trip[5] == "osvaldo@email.com"


@pytest.mark.skip(reason="Interaccion con el banco")
def test_find_trip_by_id():
    db_file = "/home/gustavo/Escritorio/curso python/storage.db"
    conn = sqlite3.connect(db_file)
    trips_repository = TripsRepository(conn)

    trip_id = str(uuid.uuid4())
    trips_infos = {
        "id": trip_id,
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com"
    }
    trips_repository.create_trip(trips_infos)

    trip = trips_repository.find_trip_by_id(trip_id)

    assert trip is not None, "El viaje no se encontró en la base de datos."
    assert trip[1] == "Osasco"
    assert trip[2] == "2024-01-02"
    assert trip[3] == "2024-01-07"
    assert trip[4] == "Osvaldo"
    assert trip[5] == "osvaldo@email.com"


@pytest.mark.skip(reason="Interaccion con el banco")
def test_update_trip_status():
    db_file = "/home/gustavo/Escritorio/curso python/storage.db"
    conn = sqlite3.connect(db_file)
    trips_repository = TripsRepository(conn)

    trip_id = str(uuid.uuid4())
    print(f"Generated trip_id for test_update_trip_status: {trip_id}")

    trips_infos = {
        "id": trip_id,
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com"
    }
    trips_repository.create_trip(trips_infos)

    # Actualiza el estado del viaje
    new_status = "Completed"
    trips_repository.update_trip_status(trip_id, new_status)  # Only pass trip_id and new_status

    # Verifica que el estado se haya actualizado correctamente
    trip = trips_repository.find_trip_by_id(trip_id)
    assert trip is not None, "El viaje no se encontró en la base de datos."
    assert trip[6] == new_status, f"Expected status to be {new_status} but got {trip[6]}"

    conn.close()
