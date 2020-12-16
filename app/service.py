from flask import Blueprint
from flask_restplus import Namespace, Resource
from flask import abort
from http import HTTPStatus

from model import Loader

ld = Loader()

# API
api_namespace = Namespace('jokes_rp')


@api_namespace.route('/get_jokes/')
class Testing(Resource):
    def get(self):
        """Testing."""
        return "OK Restplus", HTTPStatus.OK


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