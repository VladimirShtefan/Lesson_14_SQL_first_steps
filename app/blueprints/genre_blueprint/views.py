from flask import Blueprint, jsonify

from app.blueprints.genre_blueprint.dao.genre_dao import Genre


genre_blueprint = Blueprint('genre_blueprint', __name__, url_prefix='/genre')


@genre_blueprint.route('/<string:genre>/', methods=['GET'])
def children_page(genre: str):
    film = Genre()
    return jsonify(film.get_movie_by_genre(genre))
