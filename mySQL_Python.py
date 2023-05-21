from tkinter import *

import mysql.connector
expression = ""

connection = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="2020btecs00040")

curser = connection.cursor()


root = Tk()
root.geometry('500x400')
root.title("Student Registration System")


def add_course():  # new window definition
    def add_query():
        global root
        statement = "INSERT INTO STUDENT VALUES ('" + \
            E1.get()+"','"+E2.get()+"')"
        curser.execute(statement)
        connection.commit()
        add.config(state=NORMAL)
        update.config(state=NORMAL)
        show.config(state=NORMAL)
        delete.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('400x300')
    add.config(state=DISABLED)
    newwin.title("Add New Student")
    L1 = Label(newwin, text="Student Name")
    L1.place(x=10, y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100, y=50)
    L2 = Label(newwin, text="PRN")
    L2.place(x=10, y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=100, y=100)
    button = Button(newwin, text="Add", command=add_query)
    button.place(x=120, y=200)


def update_data():  # new window definition
    def update_query():
        global root
        statement = "UPDATE STUDENT SET NAME = '" + \
            E1.get()+"' WHERE PRN ='"+E2.get()+"'"
        curser.execute(statement)
        connection.commit()
        add.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('400x300')
    newwin.title("Update Student")
    add.config(state=NORMAL)
    L1 = Label(newwin, text="Student Name")
    L1.place(x=10, y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100, y=50)
    L2 = Label(newwin, text="PRN")
    L2.place(x=10, y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=100, y=100)
    button = Button(newwin, text="Update", command=update_query)
    button.place(x=120, y=200)


def del_data():
    def delete_query():
        global root
        statement = "DELETE FROM STUDENT WHERE PRN='"+E1.get()+"'"
        curser.execute(statement)
        connection.commit()
        add.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('400x300')
    newwin.title("Delete Student")
    add.config(state=NORMAL)
    L1 = Label(newwin, text="PRN")
    L1.place(x=10, y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100, y=50)
    sub = Button(newwin, text="Delete Student", command=delete_query)
    sub.place(x=120, y=200)


def display():
    newwin = Toplevel(root)
    newwin.geometry('400x300')
    newwin.title("Student Details")
    statement = "SELECT * FROM STUDENT"
    curser.execute(statement)
    L1 = Label(newwin, text="Student Name")
    L1.grid(row=0, column=0)
    L2 = Label(newwin, text="PRN")
    L2.grid(row=0, column=1)

    i = 1
    for row in curser:
        L1 = Label(newwin, text=row[0])
        L1.grid(row=i, column=0)
        L2 = Label(newwin, text=row[1])
        L2.grid(row=i, column=1)
        i += 1


add = Button(root, text='Add New Student', command=add_course)
delete = Button(root, text='Delete Student', command=del_data)
update = Button(root, text='Update Student', command=update_data)
show = Button(root, text='View Details', command=display)
add.place(x=80, y=80)
delete.place(x=80, y=150)
update.place(x=250, y=80)
show.place(x=250, y=150)

root.mainloop()
