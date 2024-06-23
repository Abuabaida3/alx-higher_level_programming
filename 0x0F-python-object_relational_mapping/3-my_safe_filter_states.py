#!/usr/bin/python3
"""
Scrpt that in an argument
"""
import Mysqldb
from sys import argv

if __name__ == '__main__':
    db = MYSQLdb.connect(host="localhost", port=3306, user=arg[1], passwd=argv[2], db=argv[3]
            cur = db.cursor()
            cur.excute("SELECT * form states WHERE BINARY name = %s, [argv]])

            row = cur.fetechall
            for i in row:
            print(i)
            #Clean up process
            cur.close()
            db.close()
