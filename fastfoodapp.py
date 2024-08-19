from tkinter import * 
from tkinter import messagebox
import sqlite3

def connect_db():
    try:
        con = sqlite3.connect("fastfood.db")
    except:
        print("can not connect to database")
        return False
    else:
        return con

def create_file():
    try:
        con = connect_db()
        cur = con.cursor()
        sql = '''
            CREATE TABLE IF NOT EXISTS menu(
            sandwich varchar(30),
            pizza varchar(30),
            drink varchar(30),
            sandwich_price float,
            pizza_price float,
            drink_price float
            )
        '''
        cur.execute(sql)
        con.commit()
        con.close()
    except:
        print("can not create table!")
    else:
        print("table has been created suxxssfully")

def new_menu(sandwich, pizza, drink, sandwich_price, pizza_price, drink_price):
    try:
        con = connect_db()
        cur = con.cursor()
        SQL ='''
            INSERT INTO menu
                (sandwich, pizza, drink, sandwich_price, pizza_price, drink_price)
            VALUES
                (''' + sandwich + ''',"'''+ pizza +'''","'''+ drink +'''",''' + str(sandwich_price) + ''',''' + str(pizza_price) + ''',''' + str(drink_price) + ''')
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

def edit_menu(sandwich, pizza, drink, sandwich_price, pizza_price, drink_price):   
    try:
        con = connect_db()
        cur = con.cursor()
        SQL='''
            UPDATE menu
                SET sandwich = "''' + sandwich + '''",
                    pizza = "''' + pizza + '''",
                    pizza = "''' + drink + '''",
                    score1 = ''' + str(sandwich_price) + ''',
                    score2 = ''' + str(pizza_price) + ''',
                    score3 = ''' + str(drink_price) + '''
            WHERE menu = ''' "menu"
                
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        print("can not update record!")
    else:
        print("one record has been updated") 
        show_table() 


def delete_menu(number):
    try:
        con = connect_db()
        cur = con.cursor()
        SQL='''
            DELETE FROM menu
            WHERE number = '''+ str(number)
        cur.execute(SQL)
        con.commit()
        con.close()
    except:
        messagebox.showwarning("warning","can not delete record!")
    else:
        messagebox.showinfo("delete","delete record successfully")
        show_table() 


def show_table(where = "1"):
    con = connect_db()
    cur = con.cursor()
    sql = '''
        SELECT * FROM fastfood
        WHERE ''' + where
    cur.execute(sql)
    list1.delete(0, END)
    for i in cur:
        list1.insert(END, i)
    con.close()

def fill():
    sandwich = sandwich.get()
    pizza = pizza.get()
    drink = drink.get()
    sandwich_price = price1.get()
    pizza_price = price2.get()
    drink_price = price3.get()
    new_menu(sandwich, pizza, drink, sandwich_price, pizza_price, drink_price)


def update_menu():
    sandwich = sandwich.get()
    pizza = pizza.get()
    drink = drink.get()
    sandwich_price = price1.get()
    pizza_price = price2.get()
    drink_price = price3.get()
    edit_menu(sandwich, pizza, drink, sandwich_price, pizza_price, drink_price)


def exit():
    root.destroy()

def getselectedrow(event):
    if list1.curselection():
        i = list1.curselection()[0]
        row = list1.get(i)
        sandwich.set(row[0])
        pizza.set(row[1])
        drink.set(row[2])
        price1.set(row[3])
        price2.set(row[4])
        price3.set(row[5])
        print(row)

def delete():
    if list1.curselection():
        menu = menu.get()
        q = messagebox.askquestion("delete","do you want delete student" + menu)
        if q == "yes":            
            delete_menu(menu)

root = Tk()
root.title("fastfood.db")

sandwich = StringVar()
pizza = StringVar()
drink = IntVar()
price1 = IntVar()
price2 = IntVar()
price3 = IntVar()

lbl = Label(root,text= "ساندویچ")
lbl.grid(row=0,column=0)

lbl2 = Label(root,text= "پیتزا")
lbl2.grid(row=1,column=0)

lbl3 = Label(root,text= "نوشیدنی")
lbl3.grid(row=2,column=0)

lbl4 = Label(root,text= "قیمت")
lbl4.grid(row=3,column=0)

btnSave = Button(root,text="ذخیره",command=fill)
btnSave.place(x=265,y=1)

btnEdit = Button(root,text="ویرایش",command=update_menu)
btnEdit.place(x=309,y=1)

btnDelete = Button(root,text="حذف",command=delete)
btnDelete.place(x=360,y=1)

btnExit = Button(root,text="خروج",command=exit)
btnExit.place(x=400,y=1)

nameinput = Entry(root,textvariable= sandwich)
nameinput.grid(row=0,column=1)

familyinput = Entry(root,textvariable= pizza)
familyinput.grid(row=1,column=1)

ageinput = Entry(root,textvariable= drink)
ageinput.grid(row=2,column=1)

courseinput1 = Entry(root,textvariable= price1)
courseinput1.grid(row=3,column=1)

courseinput2 = Entry(root,textvariable= price2)
courseinput2.grid(row=4,column=1)

courseinput3 = Entry(root,textvariable= price3)
courseinput3.grid(row=5,column=1)

list1 =Listbox(root,width=40,height=10)
list1.grid(row=10,column=4)

sb1 = Scrollbar(root,)
sb1.grid(row=10,column=5,sticky= N+S+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", getselectedrow)

root.geometry("450x260")
root.resizable(width= False, height= False)
color= "pink"
root.configure(bg=color)
root.mainloop()