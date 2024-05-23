from tkinter import *
from PIL import Image , ImageTk

index = Tk()
index.geometry("500x500")
#for JPG image
img = Image.open("img/bg1.jpg")
img1 = ImageTk.PhotoImage(img)
img2 = Label(image=img1)
img2.pack()


index.mainloop()
