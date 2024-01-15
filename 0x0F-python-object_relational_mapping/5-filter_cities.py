#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )
    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s ORDER BY cities.id", (state_name,))
    cities = cursor.fetchall()

    for city in cities:
        print(city[1], end=', ')

    print()

    cursor.close()
    db.close()
