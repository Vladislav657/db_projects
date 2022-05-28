from flask import Flask, jsonify
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def movie_by_title(title):
    return jsonify(get_movie_by_title(title))


@app.route('/movie/<start_year>/to/<end_year>')
def movie_by_year_range(start_year, end_year):
    return jsonify(get_movies_by_year_range(start_year, end_year))


@app.route('/rating/children')
def movie_for_children():
    return jsonify(get_movies_by_rating('children'))


@app.route('/rating/family')
def movie_for_family():
    return jsonify(get_movies_by_rating('family'))


@app.route('/rating/adult')
def movie_for_adult():
    return jsonify(get_movies_by_rating('adult'))


@app.route('/genre/<genre>')
def movie_by_genre(genre):
    return jsonify(get_movie_by_genre(genre))


if __name__ == '__main__':
    app.run()
