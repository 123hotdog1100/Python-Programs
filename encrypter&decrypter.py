import tkinter
tk = tkinter
window = tk.Tk()
label1 = tk.Label(window, text ="Enter the shift:").grid(row= 0, column = 0)
e1 = tk.Entry(window)
e1.grid(row=0, column = 1)
label2 = tk.Label(window, text ="Enter the word/phrase to encrypt:").grid(row= 2, column = 0)
e2 = tk.Entry(window)
e2.grid(row= 2, column = 1)
result = tk.Label(window, text = "Output:" )
result.grid(row=3, column = 0)
alpha  =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypted():
     global shift, alpha, word, e1, e2, result
     wordget = e2.get()
     wordlist = list(wordget)
     s = e1.get()
     shift = int(s)
     
     encrypted = []
     for letter in wordlist:
          index = alpha.index(letter)
          index = index + shift
          if index > 25:
               index = index - 25
          encrypted.append(alpha[index])
     str1 = ""
     result.config(text = "Output: " + str1.join(encrypted))


def decrypted():
     global shift, alpha, word, e1, e2
     wordget = e1.get
     wordlist = list(wordget)
     decrypted = []
     shift = e1.get()
     for letter in wordlist:
          index = alpha.index(letter)
          index = index - shift
          if index < -1:
               index = index + 25
          decrypted.append(alpha[index])
     str1 = ""

     result.config(text = "Output: " + str1.join(encrypted))
     


btn = tk.Button(window, text= "Encrypt", command = encrypted, height = 1, width = 5)
btn.grid(row = 3, column = 2)
btn2 = tk.Button(window, text= "Decrypt", command = decrypted, height = 1, width = 5)
btn2.grid(row = 4, column = 2)
window.geometry("354x99")
window.title("Encrypter/Decrypter")
window.mainloop()

