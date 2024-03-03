import tkinter as tk

frm = tk.Tk()
frm.title("Python Frame")

def cmd():
    l1.config(text="Bye! Devansh")

l1 = tk.Label(frm, text="Hello! Devansh")
l1.pack(pady=50)
btn1 = tk.Button(frm, text="Click me", command=cmd)
btn1.pack(pady=40)
frm.mainloop()