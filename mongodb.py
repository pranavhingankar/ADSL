import pymongo
from tkinter import *

client = pymongo.MongoClient(
    "mongodb+srv://Pranav:Pranav@cluster0.sthl8b2.mongodb.net/?retryWrites=true&w=majority")
# print(client)

mydb=client['student']
collection=mydb['details']

def insert_data():
    name=name_entry.get()
    prn=prn_entry.get()
    year=year_entry.get()
    email=email_entry.get()
    dict={'name':name,'prn':prn,'year':year,'email':email}
    collection.insert_one(dict)
    name_entry.delete(0, END)
    prn_entry.delete(0, END)
    year_entry.delete(0, END)
    email_entry.delete(0, END)

def read_data():
    items = collection.find()
    listbox.delete(0,END)
    # print(type(items[0]))
    for item in items:
        item_str = f"{item['name']}, {item['prn']}, {item['year']}, {item['email']}"
        listbox.insert(END, item_str)

def update_data():
    name=name_entry.get()
    prn=prn_entry.get()
    year=year_entry.get()
    email=email_entry.get()
    dict={}
    if(prn!=''):
        dict.update({'prn':prn})
    if(year!=''):
        dict.update({'year':year})
    if(email!=''):
        dict.update({'email':email})
    query={"name":name}
    update={"$set":dict}
    collection.update_one(query,update)
    name_entry.delete(0, END)
    prn_entry.delete(0, END)
    year_entry.delete(0, END)
    email_entry.delete(0, END)

def delete_data():
    listbox.delete(0,END)
    name=name_entry.get()
    query={"name":name}
    collection.delete_one(query)
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