import sqlite3

from app.db.db_query import DataBase


class Movie(DataBase):
    @staticmethod
    def get_dict_result(data: list[sqlite3.Row]) -> list[dict]:
        result = []
        for film in data:
            value = {}
            for key in film.keys():
                value[key] = film[key]
            result.append(value)
        return result

    def get_movie_by_title(self, search_title: str) -> dict:
        return self.get_dict_result(self.get_film_by_title(search_title))[0]

    def get_movies_year_by_year(self, start_year: int, end_year: int):
        return self.get_dict_result(self.get_film_year_to_year(start_year, end_year))
