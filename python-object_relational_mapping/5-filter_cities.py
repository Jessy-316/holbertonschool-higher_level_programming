#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""


from MySQLdb import connect
from sys import argv


if __name__ == "__main__":

    db = connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id WHERE BINARY states.name\
                LIKE %s ORDER BY cities.id ASC"

    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()
    print(', '.join([row[0] for row in rows]))

    cursor.close()
    db.close()
