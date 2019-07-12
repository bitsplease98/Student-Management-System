import sqlite3
from tkinter import *
from tkinter import messagebox,ttk

mainwindow = Tk()
mainwindow.title('Database App for Sqlite3')

l1=Label(mainwindow,text='Enter your name')
l1.pack()
t1=Entry(mainwindow)
t1.pack()
l2=Label(mainwindow,text='Enter your college')
l2.pack()
t2=Entry(mainwindow)
t2.pack()
l3=Label(mainwindow,text='Enter your address')
l3.pack()
t3=Entry(mainwindow)
t3.pack()
l4=Label(mainwindow,text='Enter your phone')
l4.pack()
t4=Entry(mainwindow)
t4.pack()


connection=sqlite3.connect('student1.db')
print('database opened successfully')

TABLE_NAME='student1_table'
ID='Student_Id'
NAME='Student_Name'
COLLEGE='Student_College'
ADDRESS='Student_Address'
PHONE='Student_Phone'

def savetodatabase():
    name=t1.get()
    college=t2.get()
    address=t3.get()
    phone=t4.get()
    if ((name == '') | (college == '') | (address == '') | (phone == '')):
        messagebox.showerror('ERROR','Fill all the values')
    else:
        try:
            connection.execute('CREATE TABLE IF NOT EXISTS ' +
                                TABLE_NAME +'('+ ID +
                                ' INTEGER PRIMARY KEY ''AUTOINCREMENT, '+
                                 NAME +' TEXT, '+ COLLEGE +
                                ' TEXT, '+ ADDRESS +' TEXT, '+
                                PHONE +' INTEGER);')

            connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
                                NAME +", "+ COLLEGE + ", "+
                                ADDRESS +", "+
                                PHONE +
                                " ) VALUES ( '" +name +"','" +college +"'," +
                                "'" + address +"', "+ phone +"); ")

            connection.commit()
            messagebox.showinfo('Success', 'Values committed to Database')
        except sqlite3.OperationalError:
            messagebox.showerror('ERROR','Enter proper Values')

b1=Button(mainwindow,text='Submit',command=lambda:savetodatabase())
b1.pack()


def showdatabase():
    secondwindow = Tk()
    secondwindow.title('Database')

    tree = ttk.Treeview(secondwindow)
    tree['columns'] = ('one', 'two', 'three', 'four', 'five')
    tree.heading('one', text='Student Id')
    tree.heading('two', text='Student Name')
    tree.heading('three', text='Student College')
    tree.heading('four', text='Student Address')
    tree.heading('five', text='Student Phone')

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i=0
    for row in cursor:
        tree.insert('', i, text='Student ' + str(row[0]),
                    values=( row[0], row[1],row[2] ,row[3] ,row[4]))
        i=i+1
    tree.pack()
    secondwindow.mainloop()

b3=Button(mainwindow,text='Show Database',command=lambda:showdatabase())
b3.pack()


def closeconnection():
    connection.close()
    print("Connection has been closed.")
    mainwindow.destroy()
    print("Main window destoryed.")

b3=Button(mainwindow,text='Close Connection',command=lambda:closeconnection())
b3.pack()
l5=Label(mainwindow,text='Close the connection before quitting the App')
l5.pack()

mainwindow.mainloop()

