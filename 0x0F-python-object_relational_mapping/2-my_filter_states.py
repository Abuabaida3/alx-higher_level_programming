#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    print(__import__("my_module").__doc_)'MySQLdb)

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, cursor = db.cursor()

            query = "SELECT * FOROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
            for row in cursor.fetchall()
            print(row)
            cursor.close()
            db.close
