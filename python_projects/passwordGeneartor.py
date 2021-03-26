#Importing all the necessary libraries

from tkinter import *
import random,string
import pyperclip

#initialize Window

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Password Generator")
Label(root, text ='Password Generator', font='arial 15 bold').pack(side = BOTTOM)

pass_label = Label(root, text = 'Password Length', font = 'arial 10 bold').pack()
pass_length = IntVar()
length = Spinbox(root, from_=8, to_= 32, textvariable = pass_length, width = 15).pack()
pass_str = StringVar()

#Pass_Genrate Func

def Generator():
 	password = '' 

 	for x in range(0,4):
 		password= random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)

 	for y in range (pass_length.get()-4):
 		 password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    
 	pass_str.set(password)


Button(root, text = "Generate Password", command = Generator).pack(pady = 5)
Entry(root, textvariable = pass_str).pack()

#Copy Func

def copy_pass():
	pyperclip.copy(pass_str.get())

Button(root, text = 'Copy Password', command = copy_pass).pack(pady=5)

