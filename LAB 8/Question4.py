from tkinter import *
import tkinter.messagebox

#created class

class form:
    def __init__(self, window):
        self.window = window

        #Title of the window
        window.title("Registration Form")
        #size of the window
        window.geometry("450x450")

        #In this part I am setting labels
        self.l1 = Label(window, text="Registration form", width=14, font=("bold", 20)).place(x=100, y=60)       #Label for title
        self.l2 = Label(window, text="FullName", width=20, font=("bold", 12)).place(x=40, y=130)                #Label for Name
        self.l3 = Label(window, text="Email", width=20, font=("bold", 12)).place(x=27, y=180)                   #Label for Email
        self.l4 = Label(window, text="Gender", width=20, font=("bold", 12)).place(x=30, y=230)                  #Label for Gender
        self.l5 = Label(window, text="Country", width=20, font=("bold", 12)).place(x=30, y=280)                 #Label for Country
        self.l6 = Label(window, text="Programming", width=20, font=("bold", 12)).place(x=30, y=330)             #Label for programming

        #text fields
        self.input1 = Entry(window)
        self.input1.place(x=240, y=130)
        self.input2 = Entry(window)
        self.input2.place(x=240, y=180)
        self.A1 = IntVar()
        self.A2 = StringVar(window)


        #Choosing the country
        self.A2.set("Select your Country")
        self.A3 = IntVar()
        self.w = OptionMenu(window, self.A2, "Korea", "Canada", "US", "Oman", "Yemen", "Kuwait", "Saudia Arabia", "Japan", "UAE", "Other").place(x=235, y=280)


        #radio buttons
        self.radiobutton1 = Radiobutton(window, text="Male", padx=5, variable=self.A1, value=1).place(x=235, y=230)             #Button for Male
        self.radiobutton2 = Radiobutton(window, text="Female", padx=20, variable=self.A1, value=2).place(x=290, y=230)          #Button for Female
        self.radiobutton3 = Radiobutton(window, text="Java", padx=5, variable=self.A3, value=1).place(x=235, y=330)             #Button for Java
        self.radiobutton4 = Radiobutton(window, text="Python", padx=20, variable=self.A3, value=2).place(x=290,y=330)           #Button for Python

        Button(window, text='Submit', width=20, bg='yellow', fg='black', command=self.onclick).place(x=180, y=400)              #Button Submiting

    #Executing the functions after clicking submit
    def onclick(self):
        if self.input1.get() == "" or self.input2.get() == "" or self.A1.get() == 0 or \
                self.A2.get() == 'Select Country' or self.A3.get() == 0:

        #Error for missing information
            tkinter.messagebox.showwarning(title=None, message="Please fill all the boxes and buttons !")
        else:                                                                                                   #if all the data is correct it will create a file and add the info on it
            m = open('registration.txt', 'w')
            m.write("User name :"+self.input1.get() + ", " + "Email :"+self.input2.get() + ", " + "Gender :"+str(
                self.A1.get()) + "," + "Country :"+self.A2.get() + "," + "Programming :"+str(self.A3.get()))
            print('New File have been Created')


windows = Tk()
Fourth = form(windows)
windows.mainloop()