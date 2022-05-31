import sqlite3 as sq


def get_object(item_id):
    with sq.connect('animal.db') as con:
        cur = con.cursor()
        animal = list(cur.execute('''SELECT * FROM animals WHERE id = ?''', (item_id,)))[0] + \
                 list(cur.execute('''SELECT * FROM outcome WHERE id = ?''', (item_id,)))[0][1:]
        return {
            'index': animal[0],
            'animal_id': animal[1],
            'animal_type': animal[2],
            'name': animal[3],
            'breed': animal[4],
            'color1': animal[5],
            'color2': animal[6],
            'age_upon_outcome': animal[7],
            'date_of_birth': animal[8],
            'outcome_subtype': animal[9],
            'outcome_type': animal[10],
            'outcome_month': animal[11],
            'outcome_year': animal[12]
        }
