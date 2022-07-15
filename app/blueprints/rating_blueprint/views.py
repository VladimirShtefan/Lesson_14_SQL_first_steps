from flask import Blueprint, jsonify

from app.blueprints.rating_blueprint.dao.movie_dao import Rating


rating_blueprint = Blueprint('rating_blueprint', __name__, url_prefix='/rating')


@rating_blueprint.route('/children/', methods=['GET'])
def children_page():
    film = Rating()
    return jsonify(film.get_movie_g_rating())


@rating_blueprint.route('/family/', methods=['GET'])
def family_page():
    film = Rating()
    return jsonify(film.get_movie_family_rating())


@rating_blueprint.route('/adult/', methods=['GET'])
def adult_page():
    film = Rating()
    return jsonify(film.get_movie_adult_rating())
