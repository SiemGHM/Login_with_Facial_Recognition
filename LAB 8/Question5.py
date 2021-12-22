from tkinter import *

import tkinter.messagebox
#created class called orderPizza
class orderPizza:

    def __init__(self, window1):
        self.window = window1
        window1.title("Home Style Pizza")
        window1.geometry("600x750")

#labels
        self.a1 = Label(window1, text='Welcome to Home Style Pizza Shop', font=("bold", 16), fg='Red').place(x=60, y=10)
        self.a2 = Label(window1, text='Extra Toppings: $1.50', font=("bold", 12), fg='red', borderwidth=2).place(x=10, y=70)
        self.a3 = Label(window1, text='Pizza Size', font=("bold", 12), fg='Red', borderwidth=2).place(x=240, y=70)
        self.a4 = Label(window1, text='Pizza Type', font=("bold", 12), fg='Red', borderwidth=2).place(x=440, y=70)
#check boxes
        topping1 = IntVar()
        topping2 = IntVar()
        topping3 = IntVar()
        topping4 = IntVar()
        topping5 = IntVar()
        topping6 = IntVar()
        topping7 = IntVar()
        self.toppings = [topping1, topping2, topping3, topping4, topping5, topping6, topping7]
#setting the options
        self.toppingsAvailable = ['Tomato', 'Green Pepper', 'Black Olives', 'Mushrooms', 'Extra Cheese', 'Pepperoni', 'Sausage']
        m=110
        for i in range(len(self.toppings)):
            self.button1 = Checkbutton(window1, text=self.toppingsAvailable[i], variable=self.toppings[i]).place(x=30, y=m)
            m+= 35

#sizes of the pizza
        self.sizeList = IntVar()
        self.sizes = ['small', 'medium', 'large']
        m = 110
        size_price = [6.50,8.50,10]
        for i in range(3):
            Radiobutton(window1, text=self.sizes[i] + ":$" + str(size_price[i]), variable=self.sizeList, value=(i + 1)).place(x=240, y=m)
            m += 40
#type of the pizza
        self.pizza = ['Thin Crust','Medium Crust','Pan']
        self.pizza_types = IntVar()
        m=110
        for i in range(len(self.pizza)):
            Radiobutton(window1, text=self.pizza[i], variable=self.pizza_types, value=(i + 1)).place(x=440, y=m)
            m += 40
        self.result = Text(width=100, heigh=4)
        self.result.place(x=30, y=390)
        self.btn_one = Button(window1, text='Process Selection', width=35, bg='skyblue', command=self.processinformation).place(x=180, y=350)

        window1.mainloop()
#process the information
    def processinformation(self):
        toppings = 0
        toppings_that_are_added = []
        for i in range(len(self.toppings)):
            if self.toppings[i].get() > 0:
                toppings += 1.50
                toppings_that_are_added.append(self.toppingsAvailable[i])

        pizza_size = 0
        selectedsize = ''
        if self.sizeList.get() == 1:
            selectedsize = self.sizes[self.sizeList.get() - 1]
        elif self.sizeList.get() == 2:
            selectedsize = self.sizes[self.sizeList.get() - 1]
        elif self.sizeList.get() == 3:
            selectedsize = self.sizes[self.sizeList.get() - 1]
        if selectedsize.lower() == 'small':
            pizza_size += 6.50
        elif selectedsize.lower()== 'medium':
            pizza_size += 8.50
        elif selectedsize.lower()== 'large':
            pizza_size += 10.00

        orderedpizza = ' '

        for i in range(3):
            if self.pizza_types.get() == (i + 1):
                orderedpizza = self.pizza[i]

        self.fifth_label = Label(text='Your Order:').place(x=30, y=360)
        dueAmount = toppings + pizza_size
        if orderedpizza != "" and selectedsize != "" and len(toppings_that_are_added) != 0:
            self.result.insert(END,'Pizza Type: ' + orderedpizza + "\nPizza Size: " +
                           selectedsize + '\nToppings: ' + str(toppings_that_are_added) + '\nAmount Due: $' + str(dueAmount))
        else:
            tkinter.messagebox.showwarning(title=None, message="Incomplete details")

Window = Tk()
root = orderPizza(Window)
Window.mainloop()
