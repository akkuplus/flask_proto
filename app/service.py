from flask import Blueprint
from flask_restplus import Namespace, Resource
from flask import abort
from http import HTTPStatus

from app.model import Loader

ld = Loader()

# API
#api_blueprint = Blueprint('jokes_bp', __name__)
api_namespace = Namespace('jokes_rp')




@api_namespace.route('/get_jokes/<int:number_of_jokes>')
class Joke(Resource):
    """Model a collection of jokes"""
    def get(self, number_of_jokes):
        """Get some jokes by a given number of jokes"""
        ld.request_data(number_of_jokes)
        ld.number_jokes()
        joke_list = []
        joke_list = ld.get_all_jokes()

        if joke_list:
            for item in joke_list:
                print(f"{item}")

            return joke_list, HTTPStatus.OK

        else:
            abort(HTTPStatus.NOT_FOUND, "Jokes not found.")

@api_namespace.route('/get_jokes/')
class JokeWelcome(Resource):
    def get(self):
        """Testing."""
        return "OK Restplus", HTTPStatus.OK


"""
@api_blueprint.route('/', defaults={'number_of_jokes': 1})
@api_blueprint.route('/get_jokes2/<int:number_of_jokes>')
def get_jokes(number_of_jokes: int = 1):
    try:
        if number_of_jokes:
            ld.run()
            jokes = ld.request_data(number_of_jokes)
            for idx in jokes:
                print(f"<idx>")

            return jokes, "OK"
    except Exception as ex:
        abort(404, f"{ex}")

@api_blueprint.route('/get_jokes2')
def welcome_bp():
    return "OK Blueprint"
"""