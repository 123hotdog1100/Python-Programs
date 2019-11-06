import tkinter# importing tkinter gui module
#Setting up the variables
tk = tkinter
window = tk.Tk()
answer = 0

#setting up the labels
label1 = tk.Label(window, text = "What is the first number? ").grid(row = 0)
e = tk.Entry(window)
e.grid(row=0, column = 1)
label2 = tk.Label(window, text = "What is the second number? ").grid(row = 1)
e2 = tk.Entry(window)
e2.grid(row=1, column = 1)
label3 = tk.Label(window, text = "Your answer is ")
label3.grid(row =5, column = 0)

#Defining all the operations
def equals():
    global label3, answer
    strans = str(answer)
    label3.configure(text = "Your answer is " + strans)
def add():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte + inte2
    equals()
def minus():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte - inte2
    equals()
def times():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte * inte2
    equals()
def divide():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte / inte2
    equals()
def square():
    global label3, answer, inte
    inte = int(e.get())
    #inte2 = int(e2.get())
    answer = inte * inte
    equals()
def cube():
    global label3, answer, inte
    inte = int(e.get())
    #inte2 = int(e2.get())
    answer = inte * inte * inte
    equals()
btn = tk.Button(window, text= "+", command = add, height = 2, width = 4)
btn.grid(row = 3, column = 3)
btn2 = tk.Button(window, text= "-", command = minus, height = 2, width = 4)
btn2.grid(row = 4, column = 3)
btn3 = tk.Button(window, text= "*", command = times, height = 2, width = 4)
btn3.grid(row = 5, column = 3)
btn4 = tk.Button(window, text= "/", command = divide, height = 2, width = 4)
btn4.grid(row = 6, column = 3)
btn5 = tk.Button(window, text= "^2", command = square, height = 2, width = 4)
btn5.grid(row = 7, column = 3)
btn6 = tk.Button(window, text= "^3", command = cube, height = 2, width = 4)
btn6.grid(row = 8, column = 3)
btn7 = tk.Button(window, text= "=", command = equals, height = 2, width = 4)
btn7.grid(row = 9, column = 3)


window.title("Calculator")
window.geometry("360x280")
window.mainloop()
