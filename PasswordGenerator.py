import string
import random
from tkinter import *

def get_pwd(len):

    l1 = list(string.ascii_lowercase)
    l2 = list(string.ascii_uppercase)
    l3 = list(string.digits)
    l4 = list(string.punctuation)

    lst = []
    lst.extend(random.choices(l1, k=(len - 5)))
    lst.extend(random.choices(l2, k=2))
    lst.extend(random.choices(l3, k=2))
    lst.extend(random.choices(l4, k=1))

    random.shuffle(lst)
    pwd = "".join(lst)
    # print(pwd)
    display_textbox.insert(INSERT,pwd)


def chk_input(len):
    if (len < 8):
        print("Retry : Minimum length of password should be 8\n")
        get_input()
    else:
        get_pwd(len)

def get_input():
    # len=int(input("Enter Password Length : "))
    len=int(inpEntry.get())
    chk_input(len)

# if __name__ == "__main__":
    # get_input()
    # pass

def reset():
    display_textbox.delete(1.0, END)

## Creating GUI

root = Tk()

root.title("Password Generator - [YYScoop.com]")
root.geometry("400x400")

fontstyle=("Helvitica",10,"bold")
txt_fontstyle=("Helvitica",15,"bold")
inplabel = Label(root,text="Enter the Digit of Password:", font= fontstyle)
inplabel.grid(row=0,column=0,columnspan=2,sticky=W,padx=10, pady=5)

inpEntry = Entry(root,width=33,font=txt_fontstyle)
inpEntry.grid(row=1,column=0,columnspan=2,sticky=W,padx=10, pady=5)

submit_btn = Button(root,text="Generate Password", command=get_input,fg="white",bg="#f57971",width=22)
submit_btn.grid(row=2,column=0,columnspan=2,sticky=W,padx=10, pady=5)

reset_btn = Button(root,text="Reset All ", command=reset,fg="white",bg="green",width=22)
reset_btn.grid(row=2,column=1,columnspan=2,sticky=W,padx=10, pady=5)


outlabel = Label(root,text="Your secure password is:", font= fontstyle)
outlabel.grid(row=3,column=0,columnspan=2,sticky=W,padx=10, pady=5)

display_textbox = Text(root,font=txt_fontstyle, width=33, height = 10)
display_textbox.grid(row=4,column=0,columnspan=2,sticky=W,padx=10, pady=5)

root.mainloop()
