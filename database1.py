import sqlite3
cone= None
try:
    conn = sqlite3.connect("E:/SHARMA/python language/library.db")
    print ("connection done!")
except sqlite3.DatabaseError:
    print("sorry !cannot connect to db")
finally:
    if cone is not None:
        conn.close()
        print("disconnected to db!")