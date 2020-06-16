import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3

def viewContact():
	try:
		contactList.configure(state=NORMAL)
	except:
		print("Already NORMAL")

	conn = sqlite3.connect("contact.db")
	cursor = conn.cursor()

	contacts = cursor.execute("""
		SELECT * FROM my_contacts
	""")

	for contact in contacts:
		print(f"0{contact}")
		contactList.insert(1.0, f"{contact[0]}\t\t\t{contact[1]}\t\t\t{contact[2]}\n\n")

	conn.commit()
	cursor.close()
	conn.close()
	vwBtn.configure(state=DISABLED)

	try:
		contactList.configure(state=DISABLED)
	except:
		print("Already NORMAL")

def addContact():
	try:
		contactList.configure(state=NORMAL)
	except:
		print("Already NORMAL")
	name = nmEnt.get()
	number = telEnt.get()
	address = addEnt.get()

	if name == "" or number == "" or address == "":
		print("Failed")
	else: 
		try:
			conn = sqlite3.connect("contact.db")
			cursor = conn.cursor()

			cursor.execute("""
				CREATE TABLE IF NOT EXISTS my_contacts(name TEXT NOT NULL, telephone INT NOT NULL, address TEXT NOT NULL)
			""")

			cursor.execute("""
				INSERT INTO my_contacts(name, telephone, address) VALUES(?,?,?)""", (name, number, address))
			conn.commit()
			cursor.close()
			conn.close()

			try:
				nmEnt.delete(0, END)
				addEnt.delete(0, END)
				telEnt.delete(0, END)
				vwBtn.configure(state=NORMAL)
				contactList.delete(1.0, END)
			except:
				print("Button Not Available")

		except Exception as e:
			return e.args

	try:
		contactList.configure(state=DISABLED)
	except:
		print("Already DISABLED")


root = tk.Tk()
root.title("Contact Management")
root.geometry("500x490")
root.configure()
root.resizable(width=False, height=False)

global nmEnt
global addEnt
global telEnt
global contactList
global vwBtn

lb1 = tk.Label(text="My Contact Management System", font=("Bowlby One SC", 13))
lb1.grid(row=0, column=0, columnspan=2, padx=20)

nm = tk.Label(text="Name", font=("Cookie", 16))
nm.grid(row=1, column=0, pady=20)

nmEnt = tk.Entry(width=20, font=("Comic Sans MS", 10))
nmEnt.grid(row=1, column=1, padx=30)

tel = tk.Label(text="Number", font=("Cookie", 16))
tel.grid(row=2, column=0, pady=20)

telEnt = tk.Entry(width=20, font=("Comic Sans MS", 10))
telEnt.grid(row=2, column=1)

add = tk.Label(text="Address", font=("Cookie", 16))
add.grid(row=3, column=0, pady=20)

addEnt = tk.Entry(width=20, font=("Comic Sans MS", 10))
addEnt.grid(row=3, column=1)

btn1 = tk.Button(text="add contact", font=("Impact", 10), bd=0, bg="grey", width=16, command=addContact)
btn1.grid(row=4, column=1)

vwBtn = tk.Button(text="view contact", font=("Impact", 10), bd=0, bg="grey", width=16, command=viewContact)
vwBtn.grid(row=4, column=2)

name  = tk.Label(text="Name", font=("Gabriola", 15))
name.grid(row=5)

number = tk.Label(text="Number", font=("Gabriola", 15))
number.grid(row=5, column=1)

address = tk.Label(text="Address", font=("Gabriola", 15))
address.grid(row=5, column=2)

contactList = ScrolledText(width=75, height=10, font=("Gill Sans Nova", 9), bd=1, fg="black", state=DISABLED)
contactList.grid(row=6, column=0, columnspan=3, padx=20)


mainloop()

