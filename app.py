from flask import Flask
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def film_by_title(title):
    film_info = search_by_title(title)
    return film_info


@app.route('/movie/<from_year>/to/<to_year>')
def films_by_years(from_year, to_year):
    films_info = search_by_year(from_year, to_year)
    return films_info


@app.route('/rating/children')
def films_for_children():
    films_child = search_by_rating('G')
    return films_child


@app.route('/rating/family')
def films_for_family():
    family_list = []
    for i in ['G', 'PG', 'PG-13']:
        family_list.append(search_by_rating(i))
    return family_list


@app.route('/rating/adult')
def films_for_adult():
    adult_list = []
    for i in ['R', 'NC-17']:
        adult_list.append(search_by_rating(i))
    return adult_list

@app.route('/genre/<genre>')
def films_for_janr(genre):
    films_janr = search_by_janr(genre)
    return films_janr


app.run()
