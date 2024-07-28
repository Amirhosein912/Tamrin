import sqlite3
def connect_db():
    try:
        con = sqlite3.connect("students.db")
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
                score5 float,
                sum int,
                avg float
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
    s = 0
    score1 = float(input("plz enter student score:"))
    s+= score1
    score2 = float(input("plz enter student score:"))
    s+= score2
    score3 = float(input("plz enter student score:"))
    s+= score3
    score4 = float(input("plz enter student score:"))
    s+= score4
    score5 = float(input("plz enter student score:"))
    s+= score5
    avg = s / 5
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            INSERT INTO student
                (id,name,family,score1,score2,score3,score4,score5,sum,avg)
            VALUES
                (''' + ids + ''',"'''+ name +'''","'''+ family +'''",''' + str(score1) + ''',''' + str(score2) + ''',''' + str(score3) + ''',''' + str(score4) + ''',''' + str(score5) + ''',''' + str(s) + ''',''' + str(avg) + ''')
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
    s = 0
    score1 = float(input("plz enter student score:"))
    s+= score1
    score2 = float(input("plz enter student score:"))
    s+= score2
    score3 = float(input("plz enter student score:"))
    s+= score3
    score4 = float(input("plz enter student score:"))
    s+= score4
    score5 = float(input("plz enter student score:"))
    s+= score5
    avg = s / 5
    try:
        con = connect_db()
        cur = con.cursor()
        SQL='''
            UPDATE student
                SET name = "''' + name + '''",
                    family = "''' + family + '''",
                    score1 = ''' + str(score1) + ''',
                    score2 = ''' + str(score2) + ''',
                    score3 = ''' + str(score3) + ''',
                    score4 = ''' + str(score4) + ''',
                    score5 = ''' + str(score5) + ''',
                    sum = ''' + str(s) + ''',
                    avg = ''' + str(avg) + '''
            WHERE id = ''' + ids
                
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

def show_table():
    ids = input("plz enter student id")
    con = connect_db()
    cur = con.cursor()
    SQL = '''
        SELECT * FROM student
        WHERE id = ''' + ids
    cur.execute(SQL)
    for i in cur:
        print(i)
    con.close()

def menu():
    while True:
        print("\nMENU:")
        print("1. Create Table")
        print("2. Insert Information")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5  Show Table")
        print("6. Exit")
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
            show_table()
        elif choice == "6":
            print("Goodbye See you later")
            break
        else:
            print("Please choice from the MENU")
menu()