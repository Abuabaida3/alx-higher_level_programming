#!/usr/bin/python3
import MySQLdb
import sys
"""
script that list all states with a name starting with (upper N)
form the database
"""
if __name__ == '__main__':
    def list_states_starting_with_n(username, password, database)
    db = MySQLdb.connect(host="localhost", port=3306,user=username passwd=password db = database cursor = db.cursor()

    cur = db.cursor()


    cur.execute("SELECT * FROM states WHERE name\
            LIKE BINARY 'N%' ORDER BY id ASC")

    row = cur.fetchall()
    for i in row:
        print(i)
        #clean up process
        cur.close()
        db.close()
