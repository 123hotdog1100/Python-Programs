import tkinter
tk = tkinter
window = tk.Tk()
answer = 0


label1 = tk.Label(window, text = "What is the first number? ").grid(row = 0)
e = tk.Entry(window)
e.grid(row=0, column = 1)
label2 = tk.Label(window, text = "What is the second number? ").grid(row = 1)
e2 = tk.Entry(window)
e2.grid(row=1, column = 1)
label3 = tk.Label(window, text = "Your answer is ")
label3.grid(row =5, column = 0)

def add():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte + inte2
def minus():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte - inte2
def times():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte * inte2
def divide():
    global answer, inte, inte2
    inte = int(e.get())
    inte2 = int(e2.get())
    answer = inte / inte2
def equals():
    global label3, answer
    strans = str(answer)
    label3.configure(text = "Your answer is " + strans)

def square():
    global label3, answer, inte
    answer = inte * inte
def cube():
    global label3, answer, inte
    answer = inte * inte * inte
btn = tk.Button(window, text= "+", command = add, height = 2, width = 4)
btn.grid(row = 3, column = 3)
btn2 = tk.Button(window, text= "-", command = minus, height = 2, width = 4)
btn2.grid(row = 4, column = 3)
btn3 = tk.Button(window, text= "*", command = times, height = 2, width = 4)
btn3.grid(row = 5, column = 3)
btn4 = tk.Button(window, text= "/", command = divide, height = 2, width = 4)
btn4.grid(row = 6, column = 3)
btn5 = tk.Button(window, text= "=", command = equals, height = 2, width = 4)
btn5.grid(row = 7, column = 3)

window.title("Calculator")
window.geometry("360x280")
window.mainloop()
