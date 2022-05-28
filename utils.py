import sqlite3 as sq


def get_movie_by_title(title):
    with sq.connect('netflix.db') as con:
        cur = con.cursor()
        movie = list(cur.execute('''SELECT title, country, release_year, listed_in, description FROM netflix 
        WHERE title=?''', (title,)))
        if len(movie) > 0:
            return {
                'title': movie[0][0],
                'country': movie[0][1],
                'release_year': movie[0][2],
                'genre': movie[0][3],
                'description': movie[0][4]
            }


def get_movies_by_year_range(start_year, end_year):
    with sq.connect('netflix.db') as con:
        cur = con.cursor()
        movies_json = []
        movies = list(cur.execute('''SELECT title, release_year FROM netflix WHERE release_year>=? 
        and release_year<=?''', (start_year, end_year,)))
        if len(movies) > 0:
            for movie in movies:
                movies_json.append({
                    'title': movie[0],
                    'release_year': movie[1]
                })
        return movies_json


def get_movies_by_rating(rating):
    with sq.connect('netflix.db') as con:
        cur = con.cursor()
        movies_by_rating = []
        if rating == 'children':
            movies = list(cur.execute('''SELECT title, rating, description FROM netflix WHERE rating 
            IN ('G', 'TV-G')'''))
        elif rating == 'family':
            movies = list(cur.execute('''SELECT title, rating, description FROM netflix WHERE rating 
            IN ('G', 'PG', 'TV-PG', 'PG-13')'''))
        elif rating == 'adult':
            movies = list(cur.execute('''SELECT title, rating, description FROM netflix WHERE rating 
            IN ('R', 'NR', 'NC-17')'''))
        for movie in movies:
            movies_by_rating.append({
                'title': movie[0],
                'rating': movie[1],
                'description': movie[2]
            })
        return movies_by_rating


def get_movie_by_genre(genre):
    with sq.connect('netflix.db') as con:
        cur = con.cursor()
        movies_by_genre = []
        movies = cur.execute('''SELECT title, description FROM netflix WHERE listed_in LIKE '%' || ? || '%' 
        ORDER BY release_year DESC''', (genre,))
        movies = movies.fetchmany(10)
        for movie in movies:
            movies_by_genre.append({
                'title': movie[0],
                'description': movie[1]
            })
        return movies_by_genre


def get_actors_in_pair(actor1, actor2):
    with sq.connect('netflix.db') as con:
        cur = con.cursor()
        actors = cur.execute('''SELECT * FROM netflix''')
        actors = [actor[4].split(', ') for actor in actors]
        actors_in_pair = []
        for actor in actors:
            if actor1 in actor and actor2 in actor:
                actors_in_pair.extend(actor)
        result_list = []
        for actor in actors_in_pair:
            if actors_in_pair.count(actor) > 2 and actor not in result_list and actor not in [actor1, actor2]:
                result_list.append(actor)
        return result_list


def get_movies_by_type_year_genre(pic_type, year, genre):
    with sq.connect('netflix.db') as con:
        cur = con.cursor()
        movies = cur.execute('''SELECT title, description FROM netflix WHERE type=? and release_year=? and listed_in 
        LIKE '%' || ? || '%' ''', (pic_type, year, genre))
        return [{'title': movie[0], 'description': movie[1]} for movie in list(movies)]
