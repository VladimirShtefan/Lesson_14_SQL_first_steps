from flask import Blueprint, jsonify

from app.blueprints.movie_blueprint.dao.movie_dao import Movie


title_blueprint = Blueprint('movie_blueprint', __name__, url_prefix='/movie')


@title_blueprint.route('/<string:title>/', methods=['GET'])
def search_film_by_title(title: str):
    film = Movie()
    return jsonify(film.get_movie_by_title(title))


@title_blueprint.route('/<int:start_year>/to/<int:end_year>/', methods=['GET'])
def search_films_year_to_year(start_year: int, end_year: int):
    film = Movie()
    return jsonify(film.get_movies_year_by_year(start_year, end_year))
