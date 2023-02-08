import sqlite3

def search_by_title(title):
    with sqlite3.connect('netflix.db') as connaction:
        cursor = connaction.cursor()

        sqlite_quary = """
            SELECT title, country, release_year, listed_in, description 
            FROM netflix
            WHERE title = ?
            ORDER BY release_year DESC
            LIMIT 1
        """

        cursor.execute(sqlite_quary, (title,))
        result = cursor.fetchall()
        result = result[0]
        return {
            "title": result[0],
            "country": result[1],
            "release_year": result[2],
            "genre": result[3],
            "description": result[4]
        }


def search_by_year(from_, to_):
    with sqlite3.connect('netflix.db') as connaction:
        cursor = connaction.cursor()

        sqlite_quary = """
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN ? AND ?
            ORDER BY release_year
            LIMIT 100
        """

        cursor.execute(sqlite_quary, (from_, to_,))
        result = cursor.fetchall()
        info_list = []
        for i in range(len(result)):
            info_list.append(
                {"title": result[i][0],
                 "release_year": result[i][1]},
            )
        return info_list


def search_by_rating(something):
    with sqlite3.connect('netflix.db') as connaction:
        cursor = connaction.cursor()

        sqlite_quary = """
            SELECT title, rating, description
            FROM netflix
            WHERE rating = ?
        """
        cursor.execute(sqlite_quary, (something,))
        result = cursor.fetchall()
        rating_list = []
        for i in range(len(result)):
            rating_list.append(
                {"title": result[i][0],
                "rating": result[i][1],
                "description": result[i][2]},
            )
        return rating_list


def search_by_janr(janr):
    with sqlite3.connect('netflix.db') as connaction:
        cursor = connaction.cursor()

        sqlite_quary = """
            SELECT title, description
            FROM netflix
            WHERE listed_in = ?
            ORDER BY release_year DESC 
            LIMIT 10
        """
        cursor.execute(sqlite_quary, (janr,))
        result = cursor.fetchall()
        janr_list = []
        for i in range(len(result)):
            janr_list.append(
                {"title": result[i][0],
                 "description": result[i][1]}
            )
        return janr_list


def search_by_actor(name_1, name_2):
    with sqlite3.connect('netflix.db') as connaction:
        cursor = connaction.cursor()

        sqlite_quary = """
            SELECT netflix.cast
            FROM netflix
            WHERE netflix.cast LIKE ?
            AND netflix.cast LIKE ?
        """

        cursor.execute(sqlite_quary, ('%'+name_1+'%', '%'+name_2+'%',))
        results = cursor.fetchall()
        actors_dict = {}
        for result in results:
            for actors in result:
                for actor in actors.split(', '):
                    if actor in actors_dict.keys():
                        actors_dict[actor] += 1
                    elif actor != name_1 and actor != name_2:
                        actors_dict[actor] = 1

        finish_result = []
        for key, value in actors_dict.items():
            if value >= 2:
                finish_result.append(key)
        return finish_result


def serch_by_info(typic, year, gеnre):
    with sqlite3.connect('netflix.db') as connaction:
        cursor = connaction.cursor()

        sqlite_quary = """
            SELECT title, description
            FROM netflix
            WHERE type LIKE ?
            AND release_year LIKE ?
            AND listed_in LIKE ?
        """

        cursor.execute(sqlite_quary, (typic, year, gеnre,))
        results = cursor.fetchall()

        info_list = []
        for i in range(len(results)):
            info_list.append(
                {"title": results[i][0],
                 "description": results[i][1]}
            )

    return info_list


print(serch_by_info('Movie', 2010, 'Dramas'))

