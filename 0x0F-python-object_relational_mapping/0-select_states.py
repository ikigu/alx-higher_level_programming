"""This module lists all states from the hbtn_0e_0_usa database"""

import sys
import MySQLdb

USER = sys.argv[0]
PASSWORD = sys.argv[1]
DATABASE_NAME = sys.argv[2]

db = MySQLdb.connect(host="localhost", port=3306,
                     user=USER, passwd=PASSWORD, db=DATABASE_NAME)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")

query_rows = cursor.fetchall()

for row in query_rows:
    print(f"({row.id}, '{row.name}')")

cursor.close()
db.close()
