import pymongo
from tkinter import *
import tkinter.messagebox as Messagebox
if __name__ ==   "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db=client['Customers']
    collection =db['Customer Details']

    def insert():
        id = c_id.get();
        name = c_name.get();
        phone = c_phone.get();
        gender = c_gender.get();
        mode = c_mode.get();
        if (id == "" or name == "" or phone == "" or gender == "" or mode == ""):
            Messagebox.showinfo("Insert Status", "All fields are required")
        else:
            dictionary = {'Id': id, 'Name': name ,'Phone' : phone , 'Gender' : gender , 'Mode' : mode}
            collection.insert_one(dictionary)
            Messagebox.showinfo("Insert Status", "Inserted Successfully")
            c_id.delete(0, 'end')
            c_name.delete(0, 'end')
            c_phone.delete(0, 'end')
            c_gender.delete(0, 'end')
            c_mode.delete(0, 'end')

    def delete():
        id = c_id.get();
        if (id == ""):
            Messagebox.showinfo("Delete Status", "Enter ID")
        else:
            rec = {'Id': id}
            collection.delete_one(rec)
            Messagebox.showinfo("Delete Status", "Deleted Successfully")
            c_id.delete(0, 'end')
            c_name.delete(0, 'end')
            c_phone.delete(0, 'end')
            c_gender.delete(0, 'end')
            c_mode.delete(0, 'end')

    def update():
        id = c_id.get();
        name = c_name.get();
        phone = c_phone.get();
        gender = c_gender.get();
        mode = c_mode.get();
        if (id == "" or name == "" or phone == "" or gender == "" or mode == ""):
            Messagebox.showinfo("Update Status", "All fields are required")
        else:
            prev= {'Id' : id}
            new = {'$set':{'Name' : name , 'Phone' : phone , 'Gender' : gender , 'Mode' : mode}}
            collection.update_one(prev,new)
            Messagebox.showinfo("Update Status", "Updated Successfully")
            c_id.delete(0, 'end')
            c_name.delete(0, 'end')
            c_phone.delete(0, 'end')
            c_gender.delete(0, 'end')
            c_mode.delete(0, 'end')

    def view():
        id = c_id.get();
        if (id == ""):
            Messagebox.showinfo("View Status", "Enter ID")
        else:
            cus = collection.find_one({'Id' : id}, {'_id':0})

            cus_name = cus.get("Name")
            cus_phone = cus.get("Phone")
            cus_gender = cus.get("Gender")
            cus_mode = cus.get("Mode")

            c_name.insert(0, cus_name)
            c_phone.insert(0, cus_phone)
            c_gender.insert(0, cus_gender)
            c_mode.insert(0, cus_mode)
            Messagebox.showinfo("View Status", "Viewed Successfully")



    root = Tk()
    root.geometry("600x300")
    root.title("Python+Mongo")
    id = Label(root, text='Enter ID', font=('bold', 10))
    id.place(x=20, y=30)
    name = Label(root, text='Enter Name', font=('bold', 10))
    name.place(x=20, y=60)
    phone = Label(root, text='Enter Phone', font=('bold', 10))
    phone.place(x=20, y=90)
    gender = Label(root, text='Enter Gender', font=('bold', 10))
    gender.place(x=20, y=120)
    mode = Label(root, text='Enter Mode', font=('bold', 10))
    mode.place(x=20, y=150)
    c_id = Entry()
    c_id.place(x=150, y=30)
    c_name = Entry()
    c_name.place(x=150, y=60)
    c_phone = Entry()
    c_phone.place(x=150, y=90)
    c_gender = Entry()
    c_gender.place(x=150, y=120)
    c_mode = Entry()
    c_mode.place(x=150, y=150)
    insert = Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
    insert.place(x=10, y=170)
    delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
    delete.place(x=60, y=170)
    Update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
    Update.place(x=120, y=170)
    View = Button(root, text="View", font=("italic", 10), bg="white", command=view)
    View.place(x=180, y=170)

    root.mainloop()