import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
from functools import partial
from tkcalendar import Calendar

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
                        messagebox.showinfo("Error", "Please provide correct username and password.")
            except:
                messagebox.showinfo("Error", "Couldnt open file")
     
         
        self.submitbutton = Button(self.border, text="Submit",fg = font_colour,bg=background_colour, font=("Arial", 15), command=verify)
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
                            messagebox.showinfo("Welcome","You are registered successfully.")
                            register_window.destroy()
                    else:
                        messagebox.showinfo("Error","Your password is wrong.")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field.")
                    
            self.register_button = Button(register_window, text="Sign in",fg = font_colour, font=("Arial",15), bg=border_colour, command=check)
            self.register_button.place(x=170, y=150)
            
            register_window.geometry("470x220")
            register_window.mainloop()
            
        self.register_button = Button(self, text="Register", bg = border_colour,fg = font_colour, font=("Arial",15), command=register)
        self.register_button.place(x=600, y=85)
        
class Second(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg=background_colour)
        
        self.title_label = Label(self, text="Exam Planner 2022",bg = border_colour,fg = font_colour, font=("Arial Bold", 25))
        self.title_label.place(x=40, y=150)        
        self.next_button = Button(self, text="Next",bg = border_colour,fg = font_colour, font=("Arial", 15), command=lambda: controller.show_frame(Third))
        self.next_button.place(x=10, y=20)
        
        self.back_button = Button(self, text="Back",bg = border_colour,fg = font_colour, font=("Arial", 15), command=lambda: controller.show_frame(Start))
        self.back_button.place(x=70, y=20)

        
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
        date = cal.datetime.today() + cal.timedelta(days=2)
        cal.calevent_create(date, 'Hello World', 'message')
        cal.calevent_create(date, 'Reminder 2', 'reminder')
        cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
        cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
     
        cal.tag_config('reminder', background='red', foreground='yellow')
     
        cal.pack(fill="both",pady=100,padx=100, expand=True)
        
'''https://pythonprogramming.net/object-oriented-programming-crash-course-tkinter/
above link explains the new *args,**kwargs arguments used below
Like "self," actually typing out "args" and "kwargs" is not necessary, the asterisks to the trick. It is just common to add the "args" and "kwargs." 
So what are these? These are used to pass a variable, unknown, amount of arguments through the method. The difference between them is that args are used to pass non-keyworded arguments, 
where kwargs are keyword arguments (hence the meshing in the name to make it kwargs). Args are your typical parameters. Kwargs, will basically be dictionaries.
You can get by just thinking of kwargs as dictionaries that are being passed.
'''
        
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


#start of program
if __name__ == '__main__':           
    app = Application()
    app.maxsize(800,500)
    app.mainloop()


