import tkinter
from tkinter import  *
import  random
from tkinter import  messagebox
from random import shuffle


answer=["google","facebook","instagram","book","krishna","yellow","king","chicken","fruits","june","king"]

words=[]
for i in answer:
    word=list(i)
    shuffle(word)
    words.append(word)

num=random.randint(0,len(words))

def intital():
    global words,answer,num
    lb1.configure(text=words[num])

def ans_check():
    global words,num,answer
    user_input=e1.get()
    if user_input==answer[num]:
        messagebox.showinfo("Success","This is Right answer")
        reset()
    else:
        messagebox.showerror("Error","Nope This is NOT Right answer")
        e1.delete(0,END)

def reset():
    global num,words,answer
    num = random.randint(0, len(words))
    lb1.configure(text=words[num])
    e1.delete(0,END)

root=tkinter.Tk()
root.geometry("300x300")
root.title("JUMBLE WORD")
root.configure(background = "#000000")

lb1=Label(root, bg = "#000000",
    fg = "#FFFFFF",font="times 20")
lb1.pack(pady=30,ipady=10,ipadx=10)

answers=StringVar()

e1=Entry(root,font = ("Verdana", 16),textvariable=answer)
e1.pack(ipadx=5,ipady=5)

button1=Button(root,text="Check",font = ("Comic sans ms", 16),
    width = 16,bg = "#4c4b4b",
    fg = "#6ab04c",command=ans_check)
button1.pack(pady=10)

button2=Button(root,text="Reset",width=16,font = ("Comic sans ms", 16),
    bg = "#4c4b4b",
    fg = "#EA425C",command=reset)
button2.pack()


intital()
root.mainloop()