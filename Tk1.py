from abc import ABCMeta
from tkinter import *

tyagi = Tk()

#to set Width and height off the application
#format would be "WxH"
tyagi.geometry("500x500")

#to set the size maximum & minimum width and height
#format would be (200,200)
tyagi.minsize(500,500)
tyagi.maxsize(500,500)

#Label is used add items in the GUI application
img1 = PhotoImage(file="img/adminW.png")
lImg1 = Label(image=img1)
lImg1.pack()
Text1 = Label(text="Hello Guys!!")
btn1 = Button(text="Hello")
Text1.pack() #it is must to do to add the item in the App
btn1.pack()


tyagi.mainloop()
