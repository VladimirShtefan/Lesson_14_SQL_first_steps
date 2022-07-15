import sqlite3

from app.db.db_query import DataBase


class Genre(DataBase):
    @staticmethod
    def get_dict_result(data: list[sqlite3.Row]) -> list[dict]:
        result = []
        for film in data:
            value = {}
            for key in film.keys():
                value[key] = film[key]
            result.append(value)
        return result

    def get_movie_by_genre(self, genre: str) -> list[dict]:
        return self.get_dict_result(self.get_films_by_genre(genre))
