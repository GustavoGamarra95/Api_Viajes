from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint("trip_routes", __name__)

#importacion de controles

from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participant_creator import ParticipantsCreator
from src.controllers.activity_finder import ActivityFinder
from src.controllers.activity_creator import ActivityCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer

#importacion de repositorios

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_reposiitory_test import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository
#importando el gerente de conexiones

from src.models.settings.db_conection_handler import db_connection_handler


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trip_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_rip(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantsCreator(participants_repository, emails_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activities_repository)

    response = controller.create(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/participant", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)
    response = controller.find_participants_from_trip(tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityFinder(activities_repository)
    response = controller.find_from_trip(tripId)
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(participants_repository)

    response = controller.confirm(participantId)


    print("Response:", response)

    if not isinstance(response, dict) or "body" not in response or "status_code" not in response:
        print("Invalid response format:", response)
        return jsonify({"error": "Invalid response format"}), 500

    return jsonify(response["body"]), response["status_code"]