import sqlite3

def connectdata():
    conn=sqlite3.connect('library1.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE library IF NOT EXISTS (id INTEGER PRIMARY KEY, Member_Type TEXT, PRN TEXT, Title TEXT, First_Name TEXT, Last_Name TEXT, Book_ID TEXT, Book_Title TEXT, Book_Author TEXT, Date_Borrow TEXT, Date_Due TEXT, Late_Fine TEXT, Date_Over_Due TEXT)")
    conn.commit()
    conn.close()

def adddatarec(mtype, idc, title, firstname, lastname, bookid, booktitle, bookauthor, dateborrow, datedue, latefine, dateoverdue):
    conn=sqlite3.connect('library1.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO library VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                (mtype, idc, title, firstname, lastname, bookid, booktitle, bookauthor, dateborrow, datedue, latefine, dateoverdue))
    conn.commit()
    conn.close()

def viewdata():
    conn=sqlite3.connect('library1.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM library")
    rows=cur.fetchall()
    conn.close()
    return rows

def deleterec(id):
    conn=sqlite3.connect('library1.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?", (id, ))
    conn.commit()
    conn.close()

def dataupdate(id, mtype="", idc="", title="", fisrtname="", lastname="", bookid="", booktitle="", bookauthor="", dateborrow="", datedue="", latefine="", dateoverdue=""):
	conn=sqlite3.connect('library1.db')
	cur=conn.cursor()
	cur.execute("UPDATE library SET Member_Type=?, PRN=?, Title=?, First_Name=?, Last_Name=?, Book_ID=?, Book_Title=?, Book_Author=?, Date_Borrow=?, Date_Due=?, Late_Fine=?, Date_Over_Due=? WHERE id=?", \
	(mtype, idc, title, firstname, lastname, bookid, booktitle, bookauthor, dateborrow, datedue, latefine, dateoverdue, id))
	conn.commit()
	conn.close()
