from tkinter import *
from tkinter.font import BOLD

app = Tk()
app.geometry("500x400")
txt1 = Label(text="Ready",bg="black",fg="green",font=("Arial",20,BOLD))
txt1.pack(side="bottom",fill=X)
app.mainloop()
