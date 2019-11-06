##importing functions
from random import randint
import tkinter
##gui variables
tk = tkinter
window = tk.Tk()
label = tk.Label(window, text ="Hello, Welcome to the random name generator").pack()
##variables
namelist = [] 
label2 = tk.Label(window)
label3 = tk.Label(window, text ="Enter the names you want to use and press the button after each one").pack()
labelcheck = tk.Label(window)
e1 = tk.Entry(window)
e1.pack()
def randomdef():
    global randnum, label2, e1, namelist, lengthlist, randomnum, labelcheck
    randomnum = randint(0, lengthlist)
    label2.config(text="Your random name is: " + namelist[randomnum])
    labelcheck.config(text="")

def namecheck():
    global namelist, e1, randomnum, labelcheck, lengthlist
    namelist.append(e1.get())
    labelcheck.config(text="Your name has been added and the list is now " + ", ".join(namelist))
    lengthlist = len(namelist) - 1
def nameclear():
    global namelist, label2
    label2.config(text="")
    namelist = []
    labelcheck.config(text="Your name list has been cleared check to see if it is here(should be blank): " + ", ".join(namelist))
def nameimport():
    global namelist, file
    file = open("namelist.txt","r")
    f1 = file.readlines()
    for x in f1:
        namelist.append(x)
    file.close()
def nameexport():
    global file, namelist
    file = open("namelist.txt","w+")
    file.write("\n".join(namelist))
    file.close()
window.geometry("620x620")
window.title("Random number generator")
btn1 = tk.Button(window, text = "Add names", command = namecheck).pack()
btn2 = tk.Button(window, text = "Generate", fg = "blue", command = randomdef).pack()
btn3 = tk.Button(window, text = "Clear names",fg = "red", command = nameclear).pack()
btn4 = tk.Button(window, text = "Name import from file",fg = "green", command = nameimport).pack()
btn5 = tk.Button(window, text = "Name export to a  file",fg = "red", command = nameexport).pack()

label2.pack()
labelcheck.pack()
window.mainloop()
