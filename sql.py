import sqlite3
def connect_db():
    try:
        con = sqlite3.connect("amir.db") 
    except:
        print("Can not connect to db!!!")
        return False
    else:
        return con

def create_table():
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            CREATE TABLE IF NOT EXISTS student(
                id INTEGER,
                name VARCHAR(20),
                family VARCHAR(30),
                birthdate DATETIME
            )
        '''
        cur.execute(SQL)
        con.commit()
        con.close()
    except:        
        print("Can not create table!!!")        
    else:
        print("Table has been created successfully")

def insert_table():
    ids = input("plz enter your id: ")
    name = input("plz enter name: ")
    family = input("plz enter a family: ")
    birthdate = input("plz enter age 2000-11-21 : ")
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            INSERT INTO student 
                (id,name,family,birthdate)
            VALUES
                (''' + ids + ''',"''' + name + '''", "''' + family + '''", "''' + birthdate+ '''")
        '''
        cur.execute(SQL)
        con.commit()
        con.close()
    except:        
        print("Can not insert into table!!!")        
    else:
        print("one Record has been created Added")


def show_table(ids=0):
    if ids:
        where = " WHERE id=" + ids
    else:
        where = " WHERE 1"
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            SELECT * FROM student
        ''' + where
        cur.execute(SQL)        
        con.commit()
        for data in cur:
            print(data)
        con.close()
    except:        
        print("table can not be showed!!!")        
    else:
        print("________ *** __________")


def edit_table():
    ids = input("plz enter your id: ")
    name = input("plz enter name: ")
    family = input("plz enter a family: ")
    birthdate = input("plz enter age 2000-11-21 : ")
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            UPDATE student
                set name = "'''+ name +'''",
                    family = "'''+ family +'''",
                    birthdate = "''' + birthdate +'''"
            WHERE id = ''' + ids
        cur.execute(SQL)        
        con.commit()        
        con.close()
    except:        
        print("can not update record")
    else:
        print("one record has been updated")

def delete_table():
    try:
        con = connect_db()
        cur = con.cursor()
        SQL='''
            DELETE FROM student
            where id=12
        '''
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not delete record")
    else:
        print("delete record successfully")

#insert_table()
# edit_table()
show_table()
ids = input("Please enter your id:")
show_table(ids)

# edit_table()
# delete_table()