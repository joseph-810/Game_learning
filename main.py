import tkinter as tk
from tkinter import *



win = tk.Tk()
win.title("crashed")
win.geometry("1100x730")
win.config(bg="white")
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d+0+0" % (width, height))
# bg = PhotoImage(file="cover.png")
# my_label = Label(win, image=bg)
# my_label.pack()


# upload images:
image_1 = PhotoImage(file="1.png")
img_lb1 = Label(win, image=image_1)

image_2 = PhotoImage(file="C:\\Users\\KATTAKART\\Desktop\\joseph\\charan_code\\11.png")
img_lb2 = Label(win, image=image_2)

image_3 = PhotoImage(file="2.png")
img_lb3 = Label(win, image=image_3)

image_4 = PhotoImage(file="22.png")
img_lb4 = Label(win, image=image_4)

def team_1(self,name):
    PT_1 = img_lb1.place(x=74, y=140)


def team_2():
    img_lb2.place(x=1100, y=140)

# Blocks:
block1 = tk.StringVar()
e = Entry(win, width=20,  borderwidth=10, justify=RIGHT,font=('Arial', 16), textvariable=block1)
e.place(x=20, y=540)
def call_1():
    entry = block1.get()
    if entry == "8":
        team_1()


block2 = tk.StringVar()
e1 = Entry(win, width=20, borderwidth=10, justify=RIGHT,font=('Arial', 16), textvariable=block2)
e1.place(x=1065, y=549)
def call_2():
    entry = block2.get()
    if entry == "8":
        team_2()

def submit1():
    call_1()
    # questions()

def submit2():
    call_2()



x = PhotoImage(file="submit.png")
x1 = PhotoImage(file="submit.png")

submit_but1 = Button(win, image=x, command=submit1, borderwidth=0)
submit_but1.place(x=70, y=600)

submit_but2 = Button(win, image=x1, command=submit2, borderwidth=0)
submit_but2.place(x=1140, y=604)

bg1 = PhotoImage(file="board2.png")
my_label1 = Label(win, image=bg1)
my_label1.place(x=455, y=10)
questions = ["submit.png","board2.png"]

# def questions():
#     for i in questions:
#         bg1 = PhotoImage(file=i)
#         my_label1 = Label(win, image=bg1)
#         my_label1.place(x=455, y=10)


win.mainloop()
