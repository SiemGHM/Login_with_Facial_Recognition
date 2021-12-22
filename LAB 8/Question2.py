import tkinter as tk

# create container
window = tk.Tk()

window.geometry("312x200")
window.resizable(0, 0)  # deactivate resizing

# create  label and entry for firstname and lastname
FN = tk.Label(text="Full Name", fg="black", bg="yellow", width=20, height=2)
FNbox = tk.Entry()

EM = tk.Label(text="    Email Address", fg="black", bg="red", width=20, height=2)
EMbox = tk.Entry()


# button and their functions
def close():                                                                                        # function to close window
    window.destroy()

button1 = tk.Button(text="Quit", fg="black", highlightbackground="white",
                    command=close)                                                                  # button to that uses previous funcion


def name():  # function to display firstname and lastname together
    print("Full name :", FNbox.get() + "    " + "Email Address :",EMbox.get())                      #getting the entries


button2 = tk.Button(text="Show", fg="black", highlightbackground="white",command=name)              # button to that uses previous functioon

def clearme():
    FNbox.delete(0, tk.END)
    EMbox.delete(0, tk.END)                                                                         #the command will delete the whole text written
button3 = tk.Button(text="Clear me!",width=10, fg="red", command=clearme)                           #this button to clear the current text


# insert GUI elemnt into window
FN.pack()
FNbox.pack()
EM.pack()
EMbox.pack()
button1.pack()
button2.pack()
button3.pack()

# keep focus on window
window.mainloop()
