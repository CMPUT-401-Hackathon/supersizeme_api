import csv
import sqlite3
import re

csv_file = "menu.csv"

connection = sqlite3.connect('db.sqlite3')
c = connection.cursor()
n_id = 0
with open(csv_file, 'r') as fin:
    for line in csv.DictReader(fin):

        query = '''insert into backend_item (id, name, category, serving_size, calories,
                                        calories_from_fat, total_fat, saturated_fat,
                                        trans_fat, cholesterol, sodium, carbohydrates,
                                        fiber, sugars, protein)
                values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                '''
        values = (n_id, line["Item"], line["Category"], line["Serving Size"],
        float(line["Calories"]), float(line["Calories from Fat"]), float(line["Total Fat"]),
        float(line["Saturated Fat"]), float(line["Trans Fat"]), float(line["Cholesterol"]), float(line["Sodium"]), 
        float(line["Carbohydrates"]), float(line["Dietary Fiber"]), float(line["Sugars"]), float(line["Protein"]))
        
        c.execute(query, values)
        n_id += 1
    connection.commit()