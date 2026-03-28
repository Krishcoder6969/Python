from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

label1 = Label(
    root,
    text="Hey user1 Welcome to the Denomination Counter Application.",
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msgh():
    MsgBox = messaagebox.showinfo(
        "Alert!"
        "Do you want to Calculate the denomination count?"
    )
    if MsgBox == "ok":
        topwin()

button1 = Button(
    root,
    text="Lets get started!",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)

    lbl = Label(
        top,
        text="Here are number of notes for each denomination",
    )

    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)