# Task 1 - To-Do-List App

# Importing all the required moudles
from tkinter import *
from tkinter.font import Font

# Initializing the To Do List in GUI windows
root = Tk()
root.title('Vaibhavi - ToDo List !!')
root.geometry("500x500")

#Define the Font 
v_font = Font(
    family="Comic Sans MS",
    size=30)
    
#Create Frame 
v_frame = Frame(root)
v_frame.pack(pady=2)

# Create Listbox
v_list = Listbox(v_frame,
    font=v_font,
    width=20,
    height=6,
    bg="#6B6B8E",
    bd=0,
    fg="#C0C0FF",
    highlightthickness=0,
    selectbackground="#B3B3EE",
    activestyle="none"
    )

v_list.pack(side=LEFT, fill=BOTH)

#Create demo ToDo List
#my_stuff = ["Learn Python", "Complete Codsoft Tasks", "Eat Tablets", "Walk a Dog", "Take a Nap", "Eat", "Read a book", "Water the plants", "Wash Clothes"]
#for item in my_stuff:
 #   v_list.insert(END, item)

#Create Scrollbar
v_scrollbar = Scrollbar(v_frame)
v_scrollbar.pack(side=RIGHT, fill=BOTH)

#Add Scrollbar
v_list.config(yscrollcommand=v_scrollbar.set)
v_scrollbar.config(command=v_list.yview)

#Create entry box or add box to add items to the list
v_entry = Entry(root, font=("Comic Sans MS", 15))
v_entry.pack(pady=5)

#Create a button
b_frame = Frame(root)
b_frame.pack(pady=12)

#Functions 
def add_item():
    v_list.insert(END, v_entry.get())
    v_entry.delete(0, END)
    
def delete_item():
    v_list.delete(ANCHOR)

def markcompleted_item():
    marked=v_list.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=v_list.get(marked)
    #update it 
    temp_marked=temp_marked+" ✔"
    #delete it then insert it 
    v_list.delete(temp)
    v_list.insert(temp,temp_marked)

#Add buttons
add_button = Button(b_frame, text="Add", command=add_item)
delete_button = Button(b_frame, text="Delete", command=delete_item)
markcompleted_button = Button(b_frame, text="Mark Completed", command=markcompleted_item)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)
markcompleted_button.grid(row=0, column=2)   

root.mainloop()

