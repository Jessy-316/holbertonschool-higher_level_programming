#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                WHERE Binary name LIKE '{}' ORDER BY name ASC".format(argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print("{}".format(row))

    cursor.close()
    db.close()
