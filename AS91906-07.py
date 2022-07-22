"""This file is for tracking and finding out exam dates."""
# imports the functions that the code uses
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
import json
import datetime

# global variables for Font Colour, Border Colour, Background Colour etc.
fnc = "#ffffff"
bcl = "#000000"
bgc = "#000000"
fntl = ("Arial Bold", 20)
fnts = ("Arial", 15)
fntsb = ("Arial Bold", 15)


# this starts the first login page
class Start(Frame):
    """The First frame."""

    def __init__(self, parent, controller):
        """Make Frame."""
        Frame.__init__(self, parent)
        # border around the login menu
        self.border = LabelFrame(self, bg=bgc, fg=fnc, font=fntl, bd=75)
        self.border.pack(fill="both", expand="yes")
        # places text on the gui
        self.login_label = Label(self.border, text="Login:", fg=fnc, font=fntl, bg=bcl)
        self.login_label.place(x=40, y=10)
        self.user_label = Label(self.border, text="Username:", fg=fnc, font=fntsb, bg=bcl)
        self.user_label.place(x=120, y=110)
        self.password_label = Label(self.border, text="Password:", fg=fnc, font=fntsb, bg=bcl)
        self.password_label.place(x=120, y=170)
        # entry boxes for the end user to enter their login details
        self.user_entry = Entry(self.border, width=30, text="Enter your username here", bd=5)
        self.user_entry.place(x=250, y=110)
        self.password_entry = Entry(self.border, width=30, text="Enter your password here", show='*', bd=5)
        self.password_entry.place(x=250, y=170)
        # this function allows the inputted username and password to be compared to the saved one to ensure successful logins when when both match

        def verify():
            try:
                with open("users.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        self.user_name, self.user_password = e.split(",")
                        if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                            controller.show_frame(Second)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo("Error", "Please provide a correct username and password.")
            except:
                messagebox.showinfo("Error", "Couldn't open file")
        # when you login this runs the verification function
        self.submitbutton = Button(self.border, text="Submit", fg=fnc, bg=bgc, font=fnts, command=verify)
        self.submitbutton.place(x=370, y=225)

        # opens the registration window
        def register():
            register_window = Tk()
            register_window.resizable(0, 0)
            register_window.configure(bg=bgc)
            register_window.title("Register")

            # text on the gui and boxes where the end users enter their datails
            reg_name_label = Label(register_window, text="Username:", fg=fnc, font=fnts, bg=bcl)
            reg_name_label.place(x=10, y=10)
            reg_name_entry = Entry(register_window, width=30, bd=5)
            reg_name_entry.place(x=200, y=10)

            reg_password_label = Label(register_window, text="Password:", fg=fnc, font=fnts, bg=bcl)
            reg_password_label.place(x=10, y=60)
            reg_password_entry = Entry(register_window, width=30, show="*", bd=5)
            reg_password_entry.place(x=200, y=60)

            confirm_password_label = Label(register_window, text="Confirm Password:", fg=fnc, font=fnts, bg=bcl)
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = Entry(register_window, width=30, show="*", bd=5)
            confirm_password_entry.place(x=200, y=110)

            # function that ensures registration is succesful
            def check():
                if reg_name_entry.get() != "" or reg_password_entry.get() != "" or confirm_password_entry.get() != "":
                    if reg_password_entry.get() == confirm_password_entry.get():
                        with open("users.txt", "a") as f:
                            f.write(reg_name_entry.get() + ","+reg_password_entry.get()+"\n")
                            messagebox.showinfo("Welcome", "You have been successfully registered.")
                            register_window.destroy()
                    else:
                        messagebox.showinfo("Error", "Your password has been entered incorrectly.")
                else:
                    messagebox.showinfo("Error", "Please fill in all the fields.")

            self.register_button = Button(register_window, text="Sign in", fg=fnc, font=fnts, bg=bcl, command=check)
            self.register_button.place(x=170, y=150)

            register_window.geometry("470x220")
            register_window.mainloop()
        # button that runs the check function
        self.register_button = Button(self, text="Register", bg=bcl, fg=fnc, font=fnts, command=register)
        self.register_button.place(x=600, y=85)


# creates the second frame
class Second(Frame):
    """The Second frame."""
    # function that allows the user to choose their subjects
    def subject(self):
        """Make The Subject Choosing Window."""
        subject_window = Tk()
        global words1
        global words2
        global words3
        global words4
        global words5
        words1 = StringVar(subject_window)
        words2 = StringVar(subject_window)
        words3 = StringVar(subject_window)
        words4 = StringVar(subject_window)
        words5 = StringVar(subject_window)
        subject_window.resizable(0, 0)
        subject_window.minsize(width=400, height=400)
        subject_window.configure(bg=bgc)
        subject_window.title("Subjects")
        subject_label = Label(subject_window, text="Please Select Your Subjects", fg=fnc, font=fnts, bg=bcl)
        subject_label.place(x=10, y=10)
        # drop down text boxes which allow the user to quickly pick their subjects
        words1.set("Please Select Your Subjects")
        subjectselect = OptionMenu(subject_window, words1, *subjects_date["Subjects"])
        subjectselect.place(x=100, y=100)

        words2.set("Please Select Your Subjects")
        subjectselect2 = OptionMenu(subject_window, words2, *subjects_date["Subjects"])
        subjectselect2.place(x=100, y=140)

        words3.set("Please Select Your Subjects")
        subjectselect3 = OptionMenu(subject_window, words3, *subjects_date["Subjects"])
        subjectselect3.place(x=100, y=180)

        words4.set("Please Select Your Subjects")
        subjectselect4 = OptionMenu(subject_window, words4, *subjects_date["Subjects"])
        subjectselect4.place(x=100, y=220)

        words5.set("Please Select Your Subjects")
        subjectselect5 = OptionMenu(subject_window, words5, *subjects_date["Subjects"])
        subjectselect5.place(x=100, y=260)

    # function that disables the third page untill the end users enter in their subjects to ensure the code works
    def show_calendar(self, controller):
        """Stop the next button from being pressed untill they select all their subjects."""
        subjects = [words1.get(), words2.get(), words3.get(), words4.get(), words5.get()]
        if all(elem != "Please Select Your Subjects" for elem in subjects):
            controller.show_frame(Third)

    # creates the second frame
    def __init__(self, parent, controller):
        """Create Second Frame."""
        Frame.__init__(self, parent)
        self.configure(bg=bgc)
        # text placed onto GUI and button so you can select your subjects
        self.title_label = Label(self, text="Exam Planner 2022", bg=bcl, fg=fnc, font=("Arial Bold", 25))
        self.title_label.place(x=250, y=100)

        self.title_label = Label(self, text="Please select your subjects before pressing the next button.", bg=bcl, fg=fnc, font=fntsb)
        self.title_label.place(x=125, y=150)

        self.back_button = Button(self, text="Back", bg=bcl, fg=fnc, font=fnts, command=lambda: controller.show_frame(Start))
        self.back_button.place(x=70, y=20)

        self.subjectbutton = Button(self, text="Select Your Subjects:", bg=bcl, fg=fnc, font=fnts, command=lambda: self.subject())
        self.subjectbutton.place(x=300, y=200)

        self.next_button = Button(self, text="Next", bg=bcl, fg=fnc, font=fnts, command=lambda: self.show_calendar(controller))
        self.next_button.place(x=160, y=20)


# creates the third frame
class Third(Frame):
    """The Third frame."""
    # creates the third frame
    def __init__(self, parent, controller):
        """Create Third Frame."""
        Frame.__init__(self, parent)
        self.configure(bg=bgc)
        self.app_label = Label(self, bg=bcl, fg=fnc, font=("Arial Bold", 25))
        self.app_label.place(x=40, y=150)

        self.home_button = Button(self, text="Exit", bg=bcl, fg=fnc, font=fnts, command=lambda: exit())
        self.home_button.place(x=70, y=20)

        self.get_dates = Button(self, text="Show exam dates", bg=bcl, fg=fnc, font=fnts, command=lambda: self.populate_calendar())
        self.get_dates.place(x=330, y=20)
        self.update_idletasks()
        self.cal = Calendar(self, height=800, selectmode='day', month=11, tooltipdelay=50)
        self.cal.pack(fill="both", pady=100, padx=100, expand=True)

    # this function is a button which highlights the dates on the calander, also handles the function of hovering over the dates to get specific times
    def populate_calendar(self):
        """Show Events on Calendar."""
        self.cal.calevent_remove('all')
        subjects = [words1.get(), words2.get(), words3.get(), words4.get(), words5.get()]
        for time_slot in subjects_date['Dates']:
            for subject in subjects:
                subject_list = time_slot['Level 3'].split("\n")
                if subject in subject_list:
                    date = datetime.datetime.strptime(time_slot['Date'], '%a %d %b %Y').date()
                    self.cal.calevent_create(date, f"{time_slot['Time']}: {subject}", ["Subject"])


# creates the window where the frame sits
class Application(Tk):
    """The Application Window."""
    # changes the size of the window
    def __init__(self, *args, **kwargs):
        """Make the size of the Window."""
        Tk.__init__(self, *args, **kwargs)

        self.window = Frame(self)
        self.window.pack()

        self.window.grid_rowconfigure(0, minsize=500)
        self.window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for f in (Start, Second, Third):
            frame = f(self.window, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    # displays the first frame when program is opened
    def show_frame(self, page):
        """Show Frame."""
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")

# acceses the json file
subjects_date = json.load(open("Term_Dates.json"))
# start of program
if __name__ == '__main__':
    app = Application()
    app.maxsize(800, 500)
    app.mainloop()
