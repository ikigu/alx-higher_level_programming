#!/usr/bin/python3

"""
This module lists all states from the hbtn_0e_0_usa database
whose name is what the user passes as the fourth argument.
The user input is validated to guard against SQL injections.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    USER = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    state_name = sys.argv[4]

    print(state_name)

    state_name = state_name.replace("'", "")

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=USER, passwd=PASSWORD, db=DATABASE_NAME)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE name LIKE BINARY "{}" \
                    ORDER BY id ASC'.format(state_name))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
