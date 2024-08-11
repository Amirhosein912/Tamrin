from tkinter import *

def fillfirstName():
    myName.set(nameinput.get())
    myAge.set(familyinput.get())
    print(myName.get())
    print(myAge.get())

root = Tk()
root.title("from1")

myName = StringVar()
myAge = IntVar()

lbl = Label(root,text= "نام")
lbl.place(x=10 , y=20)

lbl = Label(root,text= "نام خانوادگی")
lbl.place(x=10 , y=50)

btn = Button(text="click me!!" , command=fillfirstName)
btn.place(x=10,y=80)

nameinput = Entry(root)
nameinput.place(x=30,y=20)

familyinput = Entry(root)
familyinput.place(x=80,y=50)

root.geometry("444x334")
root.resizable(width= False, height= False)
color = 'yellow'
root.configure(bg= color)
root.mainloop()
