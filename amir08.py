from tkinter import *
import sqlite3

def connect_db():
    try:
        con = sqlite3.connect("frmstudents.db")
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
            CREATE TABLE IF NOT EXISTS student(
                id int,
                name varchar(25),
                family varchar(25),
                score1 float,
                score2 float,
                score3 float,               
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
    
def new_student(ids, name, family, score1, score2, score3):
    s = 0    
    s+= score1    
    s+= score2    
    s+= score3    
    avg = s / 3
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            INSERT INTO student
                (id,name,family,score1,score2,score3,sum,avg)
            VALUES
                (''' + str(ids) + ''',"'''+ name +'''","'''+ family +'''",''' + str(score1) + ''',''' + str(score2) + ''',''' + str(score3) + ''',''' + str(s) + ''',''' + str(avg) + ''')
        '''
        print(SQL)
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not insert into table!")
    else:
        print("one record has been create added")
        show_table()

def edit_student(ids, name, family, score1, score2, score3):   
    s = 0
    s+= score1
    s+= score2
    s+= score3
    avg = s / 3
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
                    sum = ''' + str(s) + ''',
                    avg = ''' + str(avg) + '''
            WHERE id = ''' + str(ids)
                
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not update record!")
    else:
        print("one record has been updated") 
        show_table() 

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
    #ids = input("plz enter student id")
    con = connect_db()
    cur = con.cursor()
    SQL = '''
        SELECT * FROM student
        WHERE 1 '''
    cur.execute(SQL)
    list1.delete(0, END)
    for i in cur:
        list1.insert(END, i)
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
# menu()



def fill():
    ids = studentId.get()
    name = nameinput.get()
    family = familyinput.get()
    score1 = course1.get()
    score2 = course2.get()
    score3 = course3.get()
    new_student(ids, name, family, score1, score2, score3)

def updateStudent():
    ids = studentId.get()
    name = nameinput.get()
    family = familyinput.get()
    score1 = course1.get()
    score2 = course2.get()
    score3 = course3.get()

    edit_student(ids, name, family, score1, score2, score3)


def exit():
    root.destroy()

def getselectedrow(event):
    if list1.curselection():
        i = list1.curselection()[0]
        row = list1.get(i)
        studentId.set(row[0])
        studentname.set(row[1])
        studentfamily.set(row[2])        
        course1.set(row[3])
        course2.set(row[4])
        course3.set(row[5])
        print(row)

def delete(event):
    if list1.curselection():
        i = list1.curselection()[0]
        row = list1.get(i)        
        studentname.set(row[0])
        studentfamily.set(row[2])
        studentId.set(row[4])
        list1.delete(i,i)
        print(row)

root = Tk()
root.title("StudentDB")

studentname = StringVar()
studentfamily = StringVar()
studentId = IntVar()
course1 = IntVar()
course2 = IntVar()
course3 = IntVar()

lbl = Label(root,text= "نام")
lbl.grid(row=0,column=0)

lbl2 = Label(root,text= "نام خانوادگی")
lbl2.grid(row=1,column=0)

lbl3 = Label(root,text= "کد")
lbl3.grid(row=2,column=0)

lbl4 = Label(root,text= "درس ها")
lbl4.grid(row=3,column=0)

btnSave = Button(root,text="ذخیره",command=fill)
btnSave.place(x=265,y=1)

btnEdit = Button(root,text="ویرایش",command=updateStudent)
btnEdit.place(x=309,y=1)

btnDelete = Button(root,text="حذف",command=delete)
btnDelete.place(x=360,y=1)

btnExit = Button(root,text="خروج",command=exit)
btnExit.place(x=400,y=1)

nameinput = Entry(root,textvariable= studentname)
nameinput.grid(row=0,column=1)

familyinput = Entry(root,textvariable= studentfamily)
familyinput.grid(row=1,column=1)

ageinput = Entry(root,textvariable= studentId)
ageinput.grid(row=2,column=1)

courseinput1 = Entry(root,textvariable= course1)
courseinput1.grid(row=3,column=1)

courseinput2 = Entry(root,textvariable= course2)
courseinput2.grid(row=3,column=2)

courseinput3 = Entry(root,textvariable= course3)
courseinput3.grid(row=3,column=3)



list1 =Listbox(root,width=40,height=10)
list1.grid(row=10,column=4)

sb1 = Scrollbar(root,)
sb1.grid(row=10,column=5,sticky= N+S+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", getselectedrow)

# create_file()
show_table()
root.geometry("755x260")
root.resizable(width= False, height= False)
color= "orange"
root.configure(bg=color)
root.mainloop()