import sqlite3 as sq

with sq.connect('animal.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS outcome (
    id INTEGER,
    age_upon_outcome TEXT,
    date_of_birth TEXT,
    outcome_subtype TEXT,
    outcome_type TEXT,
    outcome_month INTEGER,
    outcome_year INTEGER
    )''')

    outcome = list(cur.execute('''SELECT rowid, age_upon_outcome, date_of_birth, outcome_subtype, outcome_type, 
    outcome_month, outcome_year FROM animals ORDER BY rowid'''))
    animals = list(cur.execute('''SELECT rowid, animal_id, animal_type, name, breed, 
    color1, color2 FROM animals ORDER BY rowid'''))

    cur.execute('''DROP TABLE IF EXISTS animals''')
    cur.execute('''CREATE TABLE IF NOT EXISTS animals (
        id INTEGER,
        animal_id TEXT,
        animal_type TEXT,
        name TEXT,
        breed TEXT,
        color1 TEXT,
        color2 TEXT
        )''')

    for item in outcome:
        cur.execute('''INSERT INTO outcome (id, age_upon_outcome, date_of_birth, outcome_subtype, outcome_type, 
        outcome_month, outcome_year) VALUES(?, ?, ?, ?, ?, ?, ?)''', (item[0]-1, item[1], item[2], item[3], item[4],
                                                                      item[5], item[6]))
    for item in animals:
        cur.execute('''INSERT INTO animals (id, animal_id, animal_type, name, breed, color1, color2) 
        VALUES(?, ?, ?, ?, ?, ?, ?)''', (item[0] - 1, item[1], item[2], item[3], item[4],
                                         item[5], item[6]))
