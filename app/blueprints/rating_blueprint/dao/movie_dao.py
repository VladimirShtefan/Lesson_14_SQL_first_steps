import sqlite3

from app.db.db_query import DataBase


class Rating(DataBase):
    @staticmethod
    def get_dict_result(data: list[sqlite3.Row]) -> list[dict]:
        result = []
        for film in data:
            value = {}
            for key in film.keys():
                value[key] = film[key]
            result.append(value)
        return result

    def get_movie_g_rating(self) -> list[dict]:
        return self.get_dict_result(self.get_films_by_children_rating())

    def get_movie_family_rating(self) -> list[dict]:
        return self.get_dict_result(self.get_films_by_family_rating())

    def get_movie_adult_rating(self) -> list[dict]:
        return self.get_dict_result(self.get_films_by_adult_rating())
