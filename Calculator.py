from tkinter import *

def click(event):
    global Scvalue
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if Scvalue.get().isdigit():
            value = int(Scvalue.get())
        else:
            value = eval(screen.get()) 

        Scvalue.set(value)
        screen.update()

    elif text== "C":
        Scvalue.set("")
        screen.update()
    else:
        Scvalue.set(Scvalue.get() + text)
        screen.update()

root=Tk()
root.geometry("644x900")
root.title("Calculator By Spandan Polley")

Scvalue=StringVar()
Scvalue.set("")
screen=Entry(root, textvar=Scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, padx=10 ,pady=10)

f=Frame(root, bg="black")
f.pack()

button_texts=["7", "8", "9"]

for text in button_texts:
    b=Button(f, text=text, padx=28, pady=22,font="lucida 35 bold")
    b.pack(side=LEFT,padx=18, pady=12)
    b.bind("<Button-1>", click)

button_texts1=["4", "5", "6"]

f1=Frame(root, bg="black")
f1.pack() 

for text1 in button_texts1:
    b=Button(f1, text=text1, padx=28, pady=22,font="lucida 35 bold")
    b.pack(side=LEFT,padx=18, pady=12)
    b.bind("<Button-1>", click)

button_texts1=["1", "2", "3"]


f2=Frame(root, bg="black")
f2.pack() 

for text1 in button_texts1:
    b=Button(f2, text=text1, padx=28, pady=22,font="lucida 35 bold")
    b.pack(side=LEFT,padx=18, pady=12)
    b.bind("<Button-1>", click)

button_texts1=["0", "-", "+"]

f3=Frame(root, bg="black")
f3.pack() 

for text1 in button_texts1:
    b=Button(f3, text=text1, padx=28, pady=22,font="lucida 35 bold")
    b.pack(side=LEFT,padx=19, pady=12)
    b.bind("<Button-1>", click)

button_texts1=["/", "%", "="]

f4=Frame(root, bg="black")
f4.pack() 

for text1 in button_texts1:
    b=Button(f4, text=text1, padx=28, pady=22,font="lucida 35 bold")
    b.pack(side=LEFT,padx=18, pady=12)
    b.bind("<Button-1>", click)

button_texts1=["*", "C","."]

f5=Frame(root, bg="black")
f5.pack() 

for text1 in button_texts1:
    b=Button(f5, text=text1, padx=28, pady=22,font="lucida 35 bold")
    b.pack(side=LEFT,padx=18, pady=12)
    b.bind("<Button-1>", click)

root.mainloop()