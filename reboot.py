#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",        # your host, usually localhost
                     user="Marwanibrahim",    # your username
                     passwd="eshtaholdings",  # your password
                     db="eshta")              # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
# printing all the photo paths
cur.execute("SELECT photo_path FROM subject2")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
