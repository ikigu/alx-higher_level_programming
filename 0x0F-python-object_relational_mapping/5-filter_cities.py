#!/usr/bin/python3

"""
This module lists all states from the hbtn_0e_0_usa database
whose name is what the user passes as the fourth argument.
The user input is validated to guard against SQL injections.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb  # type: ignore

    USER = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    STATE_NAME = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=USER, passwd=PASSWORD, db=DATABASE_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities \
                    WHERE state_id = (SELECT id FROM states \
                    WHERE name = %(state)s) \
                    ORDER BY cities.id ASC", {'state': STATE_NAME})

    query_rows = cursor.fetchall()

    if query_rows is not None:
        print(", ".join([row[0] for row in query_rows]))

    cursor.close()
    db.close()
