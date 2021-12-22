import tkinter as tk
from tkinter import messagebox
window = tk. Tk()
window.title("My First GUI")                                                        #title of the window
window.geometry( "324x128")                                                         #size of the window


Label1 = tk.Label(text="Enter your name:", fg="#EC7C2A",                            #specific color
bg="yellow", width=15)


entry1 = tk.Entry(fg="red", bg="gray", width=20)                                    #background color of the entry
entry1.insert(6, "Type your name")


def clickme():
    name = entry1.get()
    print("Hello ", name)

button1 = tk.Button(text="Click me!", width=10, fg="blue", command=clickme)         #button to print the current text with"hello"


def closeme ():
    window.destroy()
button2 = tk.Button(text="Close me!", width=10, fg="black", command=closeme)        #button to close the current window


def clearme():
    entry1.delete(0, tk.END)                                                        #the command will delete the whole text written
button3 = tk.Button(text="Clear me!",width=10, fg="red", command=clearme)           #this button to clear the current text


Label1.pack()                                                                   #Label1.pack()is to place widgets in a Frame or window in a specified order.(it will be thr first one )
entry1.pack()                                                                   #entry1.pack()is to place widgets in a Frame or window in a specified order.(it will be thr second one )
button1.pack()                                                                  #button1.pack()is to place widgets in a Frame or window in a specified order.(it will be thr third one )
button2.pack()                                                                  #button2.pack()is to place widgets in a Frame or window in a specified order.(it will be thr fourth one )
button3.pack()                                                                  #button3.pack()is to place widgets in a Frame or window in a specified order.(it will be thr fifth one )

window.mainloop()