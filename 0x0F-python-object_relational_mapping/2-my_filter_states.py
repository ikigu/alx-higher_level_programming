#!/usr/bin/python3

"""
This module lists all states from the
hbtn_0e_0_usa database whose name is what
the user passes as the fourth argument
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
    cursor.execute('SELECT * FROM states WHERE name LIKE BINARY "{}" \
                    ORDER BY id ASC'.format(STATE_NAME))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
