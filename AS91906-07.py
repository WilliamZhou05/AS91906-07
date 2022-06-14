import hashlib
import tkinter as tk
from functools import partial  # a quick way to make a callback function
from tkinter import font #importing font
#importing Tkinter

font_colour = "#00ffff"
border_colour = "#00ffff"
background_colour = "#000000"
#selecting colours for certain objects

class Situation(tk.Frame): #making a frame
    def __init__(self, master = None, story = '', buttons = [], **kwargs):#sets up the main part of the code kwargs is a function that allows me to put as much story inside the code as possible
        tk.Frame.__init__(self, master, **kwargs)#creates the frame for the main code
        story_label = tk.Label(self, text = story, bg = background_colour, fg = font_colour, justify = tk.LEFT, anchor = tk.NW, font = ("Play", 10))#creates the label of the main story code
        story_label.pack()#places the label

def beginning(): #the beginning destroys the starter boxes
    title_text.destroy()
    start_button.destroy()
    name_entry_box.destroy()
    name_text.destroy()
    load() # load the first story

def load(situation = None):#defining the loading
    frame = Situation(root, **SITUATIONS.get(situation))#grabs the situations
    frame.config(bg = background_colour)#colours the background
    frame.pack()#places the frame

#WINDOW
root = tk.Tk()
root.geometry('500x500-500-300')
root.title('The Adventure')
root.config(background = background_colour)

#TEXT BOX
title_text = tk.Label(root, text = "Welcome To The Adventure", bg = background_colour, fg = font_colour, font = ("bold", "20"))
title_text.place(relx = .5, rely = .3, anchor = 'c')

#NAME ENTRY BOX
name_text = tk.Label(root, text = "Please enter your name below:", bg = background_colour, fg = font_colour)
name_text.place(relx = .5, rely = .4, anchor = 'c')

#NAME ENTRY
name_entry_box = tk.Entry(root, highlightthickness = 2, bg = "#333333", fg = font_colour)
name_entry_box.place(relx = .5, rely = .5, anchor = 'c')
name_entry_box.config(highlightbackground = font_colour, highlightcolor= "blue")

#START
start_button = tk.Button(root, text = "START", highlightthickness = 2, command = beginning, bg = background_colour, fg = font_colour)
start_button.place(relx = .5, rely = .6, anchor = 'c')
start_button.config(highlightbackground = font_colour, highlightcolor= "blue")

#THE LOOP
root.mainloop()

def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")
def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
    else:
         print("Login failed! \n")
while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")