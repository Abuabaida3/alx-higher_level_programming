#!/usr/bin/python3
"""
script that list all states with a name starting with (upper N)
form the database
"""
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,user=argv[1]passwd=argv[2])

    cur = db.cursor()


    cur.execute("SELECT * FROM states WHERE name\
            LIKE BINARY 'N%' ORDER BY id ASC")

    row = cur.fetchall()
    for i in row:
        print(i)
        #clean up process
        cur.close()
        db.close()
