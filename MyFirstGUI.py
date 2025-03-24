Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sqlite3
from tkinter import *


class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label1 = Label(master, text="Enter your Firstname")
        self.label1.pack()
        self.entry1 = Entry()
        self.entry1.pack()

        self.label2 = Label(master, text="Enter your Surname")
        self.label2.pack()
        self.entry2 = Entry()
        self.entry2.pack()

        self.label3 = Label(master, text="Enter your Date of Birth")
        self.label3.pack()
        self.entry3 = Entry()
        self.entry3.pack()
... 
...         self.label4 = Label(master, text="Enter your Member Type")
...         self.label4.pack()
...         self.entry4 = Entry()
...         self.entry4.pack()
... 
...         self.insertButton = Button(master, text="Insert Into Data Base", command=self.insert_into_database)
...         self.insertButton.pack()
... 
...         self.printButton = Button(master, text="Print all Members", command=self.print_all)
...         self.printButton.pack()
... 
...         self.closeButton = Button(master, text="Close", command=self.close)
...         self.closeButton.pack()
... 
...     def insert_into_database(self):
... 
...         firstname = self.entry1.get()
...         surname = self.entry2.get()
...         dob = self.entry3.get()
...         member_type = self.entry4.get()
... 
...         sql_command = f"insert into member(firstname, surname, date_of_birth, member_type) VALUES ('{firstname}', '{surname}', '{dob}', '{member_type}')"
... 
...         print(f"SQL Command: {sql_command}")
... 
...         try:
... 
...             connection = sqlite3.connect('tennisclub.db')
...             cursor = connection.cursor()
... 
...             cursor.execute(sql_command)
... 
...             connection.commit()
... 
...             connection.close()
... 
            print("Data inserted successfully")

        except Exception as e:
            print(f"An error occurred: {e}")

    def print_all(self):
        try:

            connectik = sqlite3.connect('tennisclub.db')
            cursor = connectik.cursor()

            cursor.execute("SELECT * FROM member")
            members = cursor.fetchall()

            for member in members:
                print(member)

            connectik.close()

        except Exception as e:
            print(f"An error occurred: {e}")

    def close(self):

        root.destroy()


root = Tk()
my_gui = MyFirstGUI(root)
