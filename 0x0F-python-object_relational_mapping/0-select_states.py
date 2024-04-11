#!/usr/bin/python3

"""This module lists all states from the hbtn_0e_0_usa database"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    USER = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]

    print(USER)

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=USER, passwd=PASSWORD, db=DATABASE_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(f"({row.id}, '{row.name}')")

    cursor.close()
    db.close()
