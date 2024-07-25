import sqlite3
def connect_db():
    try:
        con = sqlite3.connect("student.db")
    except:
        print("can not connect to database!")
        return False
    else:
        return con
    
def create_file():
    try:
        con = connect_db()
        cur = con.cursor()
        SQL = '''
            CREATE TABLE student(
                id int,
                name varchar(25),
                family varchar(25),
                score1 float,
                score2 float,
                score3 float,
                score4 float,
                score5 float
            )
        '''
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not create table!")
    else:
        print("table has been created succssfully")
    
def new_student():
    ids = input("plz enter student id:")
    name = input("plz enter student name:")
    family = input("plz enter student family:")
    score1 = input("plz enter student score:")
    score2 = input("plz enter student score:")
    score3 = input("plz enter student score:")
    score4 = input("plz enter student score:")
    score5 = input("plz enter student score:")
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            INSERT INTO student
                (id,name,family,score1,score2,score3,score4,score5)
            VALUES
                (''' + ids + ''',"'''+ name +'''","'''+ family +'''",'''+score1+''','''+score2+''','''+score3+''','''+score4+''','''+score5+''')
        '''
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not insert into table!")
    else:
        print("one record has been create added")

def edit_student():
    ids = input("plz enter student id:")
    name = input("plz enter student name:")
    family = input("plz enter student family:")
    score1 = input("plz enter student score")
    score2 = input("plz enter student score")
    score3 = input("plz enter student score")
    score4 = input("plz enter student score")
    score5 = input("plz enter student score")
    try:
        con = connect_db()
        cur = con.cursor()
        SQL='''
            UPDATE student
                set name = "'''+name+'''",
                    family = "'''+family+'''",
                    score1 = "'''+score1+'''",
                    score2 = "'''+score2+'''",
                    score3 = "'''+score3+'''",
                    score4 = "'''+score4+'''",
                    score5 = "'''+score5+'''"
            WHERE id = '''+ids
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not update record!")
    else:
        print("one record has been updated")  

def delete_student():
    ids = input("plz enter student id")
    try:
        con = connect_db()
        cur = con.cursor()
        SQL='''
            DELETE FROM student
            WHERE id = '''+ids
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not delete record!")
    else:
        print("delete record successfully")

def menu():
    while True:
        print("\nMENU:")
        print("1. Create Table")
        print("2. Insert Information")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Select your choice ?: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            new_student()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye See you later")
            break
        else:
            print("Please choose from the MENU")

menu()