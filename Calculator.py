import tkinter as tk
s=" "
def num(i):
    global s
    if i!=" ":
        s+=i
        eq.set(s)
    else:
        s=s[:len(s)-1]
        eq.set(s)
def erase():
    global s
    s=" "
    eq.set(s)
def solve():
    global s
    try:
        eq.set(eval(s))

    except:
        eq.set("Syntax error")

root=tk.Tk()

eq=tk.StringVar()
ent=tk.Entry(root,width=60,textvariable=eq)
ent.grid(columnspan=4,ipadx=50,ipady=30)

button=tk.Button(root,text="1", background="skyblue",width=20,height=5,command=lambda:num("1"))
button.grid(row=1)
button=tk.Button(root,text="2", background="light green",width=20,height=5,command=lambda:num("2"))
button.grid(row=1,column=1)
button=tk.Button(root,text="3", background="orange", width=20,height=5,command=lambda:num("3"))
button.grid(row=1,column=2)
button=tk.Button(root,text="4",  background="light green", width=20,height=5,command=lambda:num("4"))
button.grid(row=2)
button=tk.Button(root,text="5", background="orange", width=20,height=5,command=lambda:num("5"))
button.grid(row=2,column=1)
button=tk.Button(root,text="6", background="skyblue",width=20,height=5,command=lambda:num("6"))
button.grid(row=2,column=2)
button=tk.Button(root,text="7", background="orange",width=20,height=5,command=lambda:num("7"))
button.grid(row=3)
button=tk.Button(root,text="8", background="skyblue", width=20,height=5,command=lambda:num("8"))
button.grid(row=3,column=1)
button=tk.Button(root,text="9",  background="light green",width=20,height=5,command=lambda:num("9"))
button.grid(row=3,column=2)
button=tk.Button(root,text="0",background="light green", width=20,height=5,command=lambda:num("0"))
button.grid(row=4)
button=tk.Button(root,text="+", background="orange",width=20,height=5,command=lambda:num("+"))
button.grid(row=4,column=1)
button=tk.Button(root,text="-",background="skyblue", width=20,height=5,command=lambda:num("-"))
button.grid(row=4,column=2)
button=tk.Button(root,text="X", background="skyblue",width=20,height=5,command=lambda:num("*"))
button.grid(row=5)
button=tk.Button(root,text="/", background="light green", width=20,height=5,command=lambda:num("/"))
button.grid(row=5,column=1)
button=tk.Button(root,text="Clear", background="orange", width=20,height=5,command=lambda:num(" "))
button.grid(row=5,column=2)
button=tk.Button(root,text="Erase",  background="orange",width=20,height=5,command=erase)
button.grid(row=6)
button=tk.Button(root,text="=", background="sky blue", width=20,height=5,command=solve)
button.grid(row=6,column=1)
button=tk.Button(root,text="Close", background="light green", width=20,height=5,command=root.destroy)
button.grid(row=6,column=2)
root.mainloop()
