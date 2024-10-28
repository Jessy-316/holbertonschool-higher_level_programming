#!/user/bin/python3
"""
Return all table values (tables 'states')
Parameters given to the script:
mysql username, mysql password, database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connect to the database
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               password=argv[2],
                               db=argv[3])

    # Create cursor to exec queries using SQL
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
