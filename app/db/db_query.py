import sqlite3

from app.paths import DB_PATH


class DataBase:
    def __init__(self):
        self.db_path = DB_PATH

    def get_film_by_title(self, search_title: str) -> list[sqlite3.Row]:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            query = """
                    SELECT title, country, release_year, listed_in as 'genre', description
                    FROM netflix
                    WHERE netflix.title
                    LIKE :user_title
                    ORDER BY release_year DESC
                    LIMIT 1
                    """
            cursor.execute(query, {'user_title': f'%{search_title}%'})
            data = cursor.fetchall()
            return data

    def get_film_year_to_year(self, start_year: int, end_year: int) -> list[sqlite3.Row]:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            query = """
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year
                    BETWEEN :year_start AND :year_end
                    ORDER BY release_year DESC
                    LIMIT 100
                    """
            cursor.execute(query, {
                'year_start': start_year,
                'year_end': end_year
            })
            data = cursor.fetchall()
            return data

    def get_films_by_children_rating(self) -> list[sqlite3.Row]:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            query = """
                   SELECT title, rating, description
                   FROM netflix
                   WHERE rating = 'G' OR rating = 'TV-G'
                   """
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    def get_films_by_family_rating(self) -> list[sqlite3.Row]:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            query = """
                   SELECT title, rating, description
                   FROM netflix
                   WHERE netflix.rating
                   LIKE '%G%'
                   """
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    def get_films_by_adult_rating(self) -> list[sqlite3.Row]:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            query = """
                   SELECT title, rating, description
                   FROM netflix
                   WHERE netflix.rating
                   LIKE '%NC-17%' OR rating LIKE '%R%'
                   """
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    def get_films_by_genre(self, genre: str) -> list[sqlite3.Row]:
        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            query = """
                   SELECT title, description
                   FROM netflix
                   WHERE netflix.listed_in
                   LIKE :film_genre
                   ORDER BY release_year DESC
                   LIMIT 10
                   """
            cursor.execute(query, {
                'film_genre': f'%{genre}%'
            })
            data = cursor.fetchall()
            return data

    def get_actors(self, actor_1: str, actor_2: str) -> set[str]:
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = """
                   SELECT netflix.cast
                   FROM netflix
                   WHERE netflix.cast
                   LIKE :actor_num_1 AND netflix.cast LIKE :actor_num_2
                   """
            cursor.execute(query, {
                'actor_num_1': f'%{actor_1}%',
                'actor_num_2': f'%{actor_2}%',
            })
            data = cursor.fetchall()

            list_with_sets_actors = []
            start_set = {actor_1, actor_2}
            for row in data:
                list_with_sets_actors.append(set(row[0].split(', ')))
            if len(list_with_sets_actors) > 2:
                actors_test = set.intersection(*list_with_sets_actors)
                return actors_test - start_set
            return set('нет таких фильмов')

    def get_films_by_params(self, type_movie: str, year: int, genre: str) -> list[tuple]:
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            query = """
                   SELECT netflix.type, netflix.release_year, netflix.listed_in
                   FROM netflix
                   WHERE netflix.type
                   LIKE :film_type AND netflix.release_year LIKE :film_year AND netflix.listed_in LIKE :film_genre
                   """
            cursor.execute(query, {
                'film_type': f'%{type_movie}%',
                'film_year': f'%{year}%',
                'film_genre': f'%{genre}%',
            })
            data = cursor.fetchall()
            return data


if __name__ == '__main__':
    test = DataBase()
    print(test.get_actors('Rose McIver', 'Ben Lamb'))
    print(test.get_films_by_params('TV Show', 2020, 'TV Shows'))
