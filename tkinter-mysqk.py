from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
con = mysql.connect( host='127.0.0.1',user='root',password='root',port='3306',database='tp')
cursor = con.cursor()
def insert():
    id = c_id.get();
    name  = c_name .get();
    phone= c_phone.get();
    gender = c_gender.get();
    mode = c_mode.get();
    if(id=="" or name=="" or phone =="" or gender=="" or mode==""):
        Messagebox.showinfo("Insert Status", "All fields are required")
    else:
        cursor.execute("Insert into customer values('"+ id +"','"+ name +"','"+ phone +"','"+ gender +"','"+ mode +"')")
        cursor.execute("commit");
        Messagebox.showinfo("Insert Status","Inserted Successfully")
        c_id.delete(0, 'end')
        c_name.delete(0, 'end')
        c_phone.delete(0, 'end')
        c_gender.delete(0, 'end')
        c_mode.delete(0, 'end')
def delete():
    id = c_id.get();
    if(id==""):
        Messagebox.showinfo("Delete Status","Enter ID")
    else:
        cursor.execute("delete from customer where custid = ('"+id+"')")
        cursor.execute("commit");
        Messagebox.showinfo("Delete Status", "Deleted Successfully")
        c_name.delete(0, 'end')
        c_phone.delete(0, 'end')
        c_gender.delete(0, 'end')
        c_mode.delete(0, 'end')
        c_id.delete(0, 'end')
def update():
    id = c_id.get();
    name = c_name.get();
    phone = c_phone.get();
    gender = c_gender.get();
    mode = c_mode.get();
    if (id == "" or name == "" or phone == "" or gender == "" or mode == ""):
        Messagebox.showinfo("Update Status", "All fields are required")
    else:
        cursor.execute("Update customer Set cname='"+name+"',cphone='"+phone+"',cgender='"+gender+"',cpayment='"+mode+"' Where custid='"+id+"'")
        cursor.execute("commit");
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
        cursor.execute("Select * from customer where custid ='"+id+"'")
        rows =cursor.fetchall()
        for row in rows:
            c_name.insert(0,row[1])
            c_phone.insert(0, row[2])
            c_gender.insert(0, row[3])
            c_mode.insert(0, row[4])
        Messagebox.showinfo("View Status", "Viewed Successfully")
root = Tk()
root.geometry("600x300")
root.title("Python+MySQL")
id = Label(root,text='Enter ID',font=('bold',10))
id.place(x=20,y=30)
name = Label(root,text='Enter Name',font=('bold',10))
name.place(x=20,y=60)
phone = Label(root,text='Enter Phone',font=('bold',10))
phone.place(x=20,y=90)
gender = Label(root,text='Enter Gender',font=('bold',10))
gender.place(x=20,y=120)
mode = Label(root,text='Enter Mode',font=('bold',10))
mode.place(x=20,y=150)
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
insert = Button(root ,text="Insert" ,font=("italic",10) , bg="white" , command=insert)
insert.place(x=10,y=170)
delete = Button(root ,text="Delete" ,font=("italic",10) , bg="white" , command=delete)
delete.place(x=60,y=170)
Update= Button(root ,text="Update" ,font=("italic",10) , bg="white" , command=update)
Update.place(x=120,y=170)
View = Button(root ,text="View" ,font=("italic",10) , bg="white" , command=view)
View.place(x=180,y=170)


root.mainloop()