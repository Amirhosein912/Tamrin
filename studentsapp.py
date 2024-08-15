from tkinter import *

def fill():
    studentname.set(nameinput.get())
    studentfamily.set(familyinput.get())
    studentage.set(ageinput.get())
    print(studentname.get())
    print(studentfamily.get())
    print(studentage.get())

def exit():
    root.destroy()

def getselectedrow(event):
    if list1.curselection():
        i = list1.curselection()[0]
        row = list1.get(i)
        studentname.set(row[0])
        studentfamily.set(row[2])
        studentage.set(row[4])
        print(row)

def delete(event):
    if list1.curselection():
        i = list1.curselection()[0]
        row = list1.get(i)        
        studentname.set(row[0])
        studentfamily.set(row[2])
        studentage.set(row[4])
        list1.delete(i,i)
        print(row)

root = Tk()
root.title("StudentDB")

studentname = StringVar()
studentfamily = StringVar()
studentage = IntVar()

lbl = Label(root,text= "نام")
lbl.grid(row=0,column=0)

lbl2 = Label(root,text= "نام خانوادگی")
lbl2.grid(row=1,column=0)

lbl3 = Label(root,text= "سن")
lbl3.grid(row=2,column=0)

btn = Button(root,text="ذخیره",command=fill)
btn.place(x=265,y=1)

btn = Button(root,text="ویرایش",command=getselectedrow)
btn.place(x=309,y=1)

btn = Button(root,text="حذف",command=delete)
btn.place(x=360,y=1)

btn = Button(root,text="خروج",command=exit)
btn.place(x=400,y=1)

nameinput = Entry(root,textvariable= studentname)
nameinput.grid(row=0,column=1)

familyinput = Entry(root,textvariable= studentfamily)
familyinput.grid(row=1,column=1)

ageinput = Entry(root,textvariable= studentage)
ageinput.grid(row=2,column=1)

list1 =Listbox(root,width=40,height=10)
list1.grid(row=10,column=3)

sb1 = Scrollbar(root,)
sb1.grid(row=10,column=3,sticky= N+S+W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",getselectedrow)

root.geometry("435x230")
root.resizable(width= False, height= False)
color= "orange"
root.configure(bg=color)
root.mainloop()