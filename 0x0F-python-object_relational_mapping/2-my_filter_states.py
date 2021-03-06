#!/usr/bin/python3
"""
    Filter states by user input
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name=%s ORDER BY id ASC".format(),
        (argv[4],)
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
