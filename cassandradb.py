from cassandra.cluster import Cluster
from tkinter import *

cluster = Cluster(['localhost'])
session = cluster.connect()


def insert_data():
    name = name_entry.get()
    prn = prn_entry.get()
    year = year_entry.get()
    email = email_entry.get()
    results = session.execute("select max(id) as id from demo.details")
    id = results.one().id
    # print(id)
    stmt = session.prepare(
        "INSERT INTO demo.details (id,name,prn,year,email) values (?,?,?,?,?)")
    results = session.execute(stmt, [id+1, name, prn, year, email])
    name_entry.delete(0, END)
    prn_entry.delete(0, END)
    year_entry.delete(0, END)
    email_entry.delete(0, END)


def read_data():
    listbox.delete(0, END)
    rows = session.execute("Select * from demo.details")
    for row in rows:
        item_str = f"{row.name}, {row.prn}, {row.year}, {row.email}"
        listbox.insert(END, item_str)


def update_data():
    name = name_entry.get()
    prn = prn_entry.get()
    year = year_entry.get()
    email = email_entry.get()
    dict = {}
    if(prn != ''):
        dict.update({'prn': prn})
    if(year != ''):
        dict.update({'year': year})
    if(email != ''):
        dict.update({'prn': email})
    # print(dict['prn'])
    query = {"name": name}
    update = {"$set": dict}
    # collection.update_one(query,update)
    name_entry.delete(0, END)
    prn_entry.delete(0, END)
    year_entry.delete(0, END)
    email_entry.delete(0, END)


def delete_data():
    name = name_entry.get()
    session.execute("use demo")
    stmt = session.prepare("select id from details where name=(?)")
    results = session.execute(stmt, [name])
    id = results.one().id
    print(id)
    stmt = session.prepare("DELETE from demo.details where id=(?)")
    results = session.execute(stmt, [id])
    name_entry.delete(0, END)


root = Tk()
root.geometry("500x500")

name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

prn_label = Label(root, text="Prn:")
prn_label.pack()
prn_entry = Entry(root)
prn_entry.pack()

year_label = Label(root, text="Year:")
year_label.pack()
year_entry = Entry(root)
year_entry.pack()

email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

insert_button = Button(root, text="Insert", command=insert_data)
insert_button.pack()


update_button = Button(root, text="Update", command=update_data)
update_button.pack()

delete_button = Button(root, text="Delete", command=delete_data)
delete_button.pack()

listbox = Listbox(root, width=100)
listbox.pack()

read_button = Button(root, text="Read", command=read_data)
read_button.pack()

root.mainloop()
