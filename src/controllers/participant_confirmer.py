from typing import Dict


class ParticipantConfirmer:
    def __init__(self, participants_repository) -> None:
        self.__participants_repository = participants_repository

    def confirm(self, participant_id) -> Dict:
        try:
            self.__participants_repository.update_participants_status(
                participant_id)  # Asegúrate de que el nombre del método es correcto
            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }
