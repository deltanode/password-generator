import string
import random

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
    print(pwd)

def chk_input(len):
    if (len < 8):
        print("Retry : Minimum length of password should be 8\n")
        get_input()
    else:
        get_pwd(len)

def get_input():
    len=int(input("Enter Password Length : "))
    chk_input(len)

if __name__ == "__main__":
    get_input()


