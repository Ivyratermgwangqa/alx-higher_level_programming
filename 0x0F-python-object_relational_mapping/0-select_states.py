#!/usr/bin/python3

"""
MySQL Database Query Script

This script connects to a MySQL database and retrieves all records from the 'states' table, displaying them in ascending order of the 'id' column.

Usage:
    python script.py <username> <password> <database>

Parameters:
    - username (str): MySQL database username
    - password (str): MySQL database password
    - database (str): Name of the MySQL database

Dependencies:
    - MySQLdb module (install using: pip install MySQL-python)

Example:
    python script.py myuser mypassword mydatabase
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall()]
