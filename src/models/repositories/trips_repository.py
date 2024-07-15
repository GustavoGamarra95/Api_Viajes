from typing import Dict, Tuple
from sqlite3 import Connection
import datetime


class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_trip(self, trips_infos: Dict) -> None:
        cursor = self.__conn.cursor()

        start_date = datetime.datetime.strptime(trips_infos["start_date"], '%d-%m-%Y')
        end_date = datetime.datetime.strptime(trips_infos["end_date"], '%d-%m-%Y')

        cursor.execute(
            '''
                INSERT INTO trips
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES
                    (?, ?, ?, ?, ?, ?)
            ''', (
                trips_infos["id"],
                trips_infos["destination"],
                start_date.strftime('%Y-%m-%d'),
                end_date.strftime('%Y-%m-%d'),
                trips_infos["owner_name"],
                trips_infos["owner_email"],
            )
        )
        self.__conn.commit()

    def find_trip_by_id(self, trip_id: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM trips WHERE id = ?''', (trip_id,)
        )
        trip = cursor.fetchone()
        return trip

    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''UPDATE trips 
               SET status = 1 
               WHERE id = ?
            ''', (trip_id,)
        )
        self.__conn.commit()
