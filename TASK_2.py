# Task 2 - Calculator App

# Importing all the required moudles
from tkinter import *
from tkinter.font import Font

operation = ""

def add_opreation(symbol):
    global operation
    operation += str(symbol)
    text_box.delete(1.0, "end")
    text_box.insert(1.0, operation)
    
def evaluate():
    global operation
    try:
        operation = str(eval(operation))
        text_box.delete(1.0, "end")
        text_box.insert(1.0, operation)
    except:
        clear_cal()
        text_box.insert(1.0, "Error")
        
def clear_cal():
    global operation
    operation = ""
    text_box.delete(1.0, "end")


# Initializing the Calculator in GUI windows
root = Tk()
root.title('CALCULATOR')
root.geometry("300x285")

text_box = Text(root, height=2, width=17, font=("Arial", 24))
text_box.grid(columnspan=5)

button_1 = Button(root, text="1", command=lambda: add_opreation(1), width=6, font=("Arial", 14))
button_1.grid(row=2, column=1)
button_2 = Button(root, text="2", command=lambda: add_opreation(2), width=6, font=("Arial", 14))
button_2.grid(row=2, column=2)
button_3 = Button(root, text="3", command=lambda: add_opreation(3), width=6, font=("Arial", 14))
button_3.grid(row=2, column=3)
button_4 = Button(root, text="4", command=lambda: add_opreation(4), width=6, font=("Arial", 14))
button_4.grid(row=3, column=1)
button_5 = Button(root, text="5", command=lambda: add_opreation(5), width=6, font=("Arial", 14))
button_5.grid(row=3, column=2)
button_6 = Button(root, text="6", command=lambda: add_opreation(6), width=6, font=("Arial", 14))
button_6.grid(row=3, column=3)
button_7 = Button(root, text="7", command=lambda: add_opreation(7), width=6, font=("Arial", 14))
button_7.grid(row=4, column=1)
button_8 = Button(root, text="8", command=lambda: add_opreation(8), width=6, font=("Arial", 14))
button_8.grid(row=4, column=2)
button_9 = Button(root, text="9", command=lambda: add_opreation(9), width=6, font=("Arial", 14))
button_9.grid(row=4, column=3)
button_0 = Button(root, text="0", command=lambda: add_opreation(0), width=6, font=("Arial", 14))
button_0.grid(row=5, column=2)
button_plus = Button(root, text="+", command=lambda: add_opreation("+"), width=6, font=("Arial", 14))
button_plus.grid(row=2, column=4)
button_minus = Button(root, text="-", command=lambda: add_opreation("-"), width=6, font=("Arial", 14))
button_minus.grid(row=3, column=4)
button_multiple = Button(root, text="*", command=lambda: add_opreation("*"), width=6, font=("Arial", 14))
button_multiple.grid(row=4, column=4)
button_division = Button(root, text="/", command=lambda: add_opreation("/"), width=6, font=("Arial", 14))
button_division.grid(row=5, column=4)
button_open = Button(root, text="(", command=lambda: add_opreation("("), width=6, font=("Arial", 14))
button_open.grid(row=5, column=1)
button_close = Button(root, text=")", command=lambda: add_opreation(")"), width=6, font=("Arial", 14))
button_close.grid(row=5, column=3)
button_clear = Button(root, text="C", command=clear_cal, width=12, font=("Arial", 14))
button_clear.grid(row=6, column=1, columnspan=2)
button_equals = Button(root, text="=", command=evaluate, width=12, font=("Arial", 14))
button_equals.grid(row=6, column=3, columnspan=2)

root.mainloop()