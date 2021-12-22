from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x130")
window.title("Calculator")
window.resizable(False, False)


def add():                                                                          #Adding the entered value from the total
    try:
        if varname1.get() == '':
            pass
        else:
            value = int(varname1.get())
            ans = int(label2.cget("text"))
            ans += value
            label2.config(text=ans)
            entry1.delete(0, END)
    except:
        messagebox.showinfo('Exception', 'Please enter ana intiger !', parent=window)


def sub():                                                                          #subtracting the entered value from the total
    try:
        if varname1.get() == '':
            pass
        else:
            value = int(varname1.get())
            ans = int(label2.cget("text"))
            ans -= value
            label2.config(text=ans)
            entry1.delete(0, END)
    except:
            messagebox.showinfo('Exception', 'Please enter ana intiger !', parent=window)


def reset():
    entry1.delete(0, END)                                       #reseting the total value
    label2.config(text="0")


#box
varname1 = StringVar()
entry1 = Entry(window, width=35, textvar=varname1)
entry1.place(x=5, y=70)

#labels
label1 = Label(window, text="Total:")
label1.place(x=5, y=40)

label2 = Label(window, text="0")
label2.place(x=180, y=40)




#buttons
btn1 = Button(window, text='+', width=3, command=add)                         #button to add the value to the total
btn1.place(x=30, y=95)

btn5 = Button(window, text='-', width=3,  command=sub)                        #button to sub the value to the total
btn5.place(x=80, y=95)

btn2 = Button(window, text='Reset', width=8, command=reset)
btn2.place(x=152, y=95)

window.mainloop()
