import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
from functools import partial
from tkcalendar import Calendar
import json
import datetime


font_colour = "#ffffff"
border_colour = "#000000"
background_colour = "#000000"
class Start(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.border = LabelFrame(self, bg = background_colour, fg = font_colour, font = ("Arial Bold", 20), bd=75)
        self.border.pack(fill="both", expand="yes")

        self.login_label = Label(self.border, text="Login:",fg = font_colour, font=("Arial Bold", 20), bg=border_colour)
        self.login_label.place(x=40, y=10)
        
        self.user_label = Label(self.border, text="Username:",fg = font_colour, font=("Arial Bold", 15), bg=border_colour)
        self.user_label.place(x=120, y=110)
        self.user_entry = Entry(self.border, width = 30, text="Enter your username here", bd = 5)
        self.user_entry.place(x=250, y=110)
        
        self.password_label = Label(self.border, text="Password:",fg = font_colour, font=("Arial Bold", 15), bg=border_colour)
        self.password_label.place(x=120, y=170)
        self.password_entry = Entry(self.border, width = 30, text="Enter your password here", show='*', bd = 5)
        self.password_entry.place(x=250, y=170)
        
        def verify():
            try:
                with open("users.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        self.user_name, self.user_password =e.split(",")
                        if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                            controller.show_frame(Second)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide a correct username and password.")
            except:
                messagebox.showinfo("Error", "Couldn't open file")
     
         
        self.submitbutton = Button(self.border, text="Submit",fg = font_colour,bg=background_colour, font=("Arial", 15), command=lambda: controller.show_frame(Second))
        self.submitbutton.place(x=370, y=225)
        
        def register():
            register_window = Tk()
            register_window.resizable(0,0)
            register_window.configure(bg=background_colour)
            register_window.title("Register")
            reg_name_label = Label(register_window, text="Username:",fg = font_colour, font=("Arial",15), bg=border_colour)
            reg_name_label.place(x=10, y=10)
            reg_name_entry = Entry(register_window, width=30, bd=5)
            reg_name_entry.place(x = 200, y=10)
            
            reg_password_label = Label(register_window, text="Password:",fg = font_colour, font=("Arial",15), bg=border_colour)
            reg_password_label.place(x=10, y=60)
            reg_password_entry = Entry(register_window, width=30, show="*", bd=5)
            reg_password_entry.place(x = 200, y=60)
            
            confirm_password_label = Label(register_window, text="Confirm Password:",fg = font_colour, font=("Arial",15), bg=border_colour)
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = Entry(register_window, width=30, show="*", bd=5)
            confirm_password_entry.place(x = 200, y=110)
            
            def check():
                if reg_name_entry.get()!="" or reg_password_entry.get()!="" or confirm_password_entry.get()!="":
                    if reg_password_entry.get()==confirm_password_entry.get():
                        with open("users.txt", "a") as f:
                            f.write(reg_name_entry.get()+","+reg_password_entry.get()+"\n")
                            messagebox.showinfo("Welcome","You have been successfully registered.")
                            register_window.destroy()
                    else:
                        messagebox.showinfo("Error","Your password is wrong.")
                else:
                    messagebox.showinfo("Error", "Please fill in all the fields.")
                    
            self.register_button = Button(register_window, text="Sign in",fg = font_colour, font=("Arial",15), bg=border_colour, command=check)
            self.register_button.place(x=170, y=150)
            
            register_window.geometry("470x220")
            register_window.mainloop()
            
        self.register_button = Button(self, text="Register", bg = border_colour,fg = font_colour, font=("Arial",15), command=register)
        self.register_button.place(x=600, y=85)
        
class Second(Frame):
    def subject(self):
        subject_window = Tk()
        subject_window.resizable(0,0)
        subject_window.minsize(width=400, height=400)
        subject_window.configure(bg=background_colour)
        subject_window.title("Subjects")
        subject_label = Label(subject_window, text="Please Select Your Subjects",fg = font_colour, font=("Arial",15), bg=border_colour)
        subject_label.place(x=10, y=10) 

        
        subjectselect= OptionMenu (subject_window, words1, *subjects_date["Subjects"], command = lambda fff: words1 = fff)
        subjectselect.place(x=100, y=100) 

        subjectselect2= OptionMenu(subject_window, words2,*subjects_date["Subjects"])
        subjectselect2.place(x=100, y=140) 
        
        subjectselect3= OptionMenu(subject_window, words3,*subjects_date["Subjects"])
        subjectselect3.place(x=100, y=180) 

        subjectselect4= OptionMenu(subject_window, words4,*subjects_date["Subjects"])
        subjectselect4.place(x=100, y=220) 

        subjectselect5= OptionMenu(subject_window, words5,*subjects_date["Subjects"])
        subjectselect5.place(x=100, y=260)


 
        
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=background_colour)
        
        self.title_label = Label(self, text="Exam Planner 2022",bg = border_colour,fg = font_colour, font=("Arial Bold", 25))
        self.title_label.place(x=250, y=100)   

        self.back_button = Button(self, text="Back",bg = border_colour,fg = font_colour, font=("Arial", 15), command=lambda: controller.show_frame(Start))
        self.back_button.place(x=70, y=20)

        self.level3button = Button(self, text="Level 3",bg = border_colour,fg = font_colour, font=("Arial", 15), command=lambda: self.subject())
        self.level3button.place(x=350, y=350)

        self.next_button = Button(self, text="Next",bg = border_colour,fg = font_colour, font=("Arial", 15), command=lambda: controller.show_frame(Third))
        self.next_button.place(x=130, y=20)


    

class Third(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(bg=background_colour)
        self.app_label = Label(self,bg = border_colour,fg = font_colour, font=("Arial Bold", 25))
        self.app_label.place(x=40, y=150)
        
        self.home_button = Button(self, text="Back",bg = border_colour,fg = font_colour, font=("Arial", 15), command=lambda: controller.show_frame(Second))
        self.home_button.place(x=10, y=20)
        
        self.back_button = Button(self, text="Home",bg = border_colour,fg = font_colour, font=("Arial", 15), command=lambda: controller.show_frame(Start))
        self.back_button.place(x=70, y=20)
        cal = Calendar(self,height=800, selectmode='day')
       # date = datetime.datetime.strptime()
       # cal.calevent_create(date, "test","test")

        cal.pack(fill="both",pady=100,padx=100, expand=True)
        
        
class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
      
        self.window = Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (Start, Second, Third):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(Start)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")

words1 = "Please Select Your Subjects"
words2 = "Please Select Your Subjects"
words3 = "Please Select Your Subjects"
words4 = "Please Select Your Subjects"
words5 = "Please Select Your Subjects"
#start of program
if __name__ == '__main__':      
    subjects_date = json.load(open("Term_Dates.json"))    
    app = Application()
    app.maxsize(800,500)
    app.mainloop()
    


