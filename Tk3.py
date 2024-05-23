from tkinter import *
from tkinter.font import BOLD

index = Tk()
index.geometry("500x500")
index.minsize(500,500)

# Important Attributes of Tk
# text : add text
# bg : background
# fg : foreground
# padx : x padding
# pady : y padding
# relief : border styling (Sunken,raised,groove,riged)
# font : font=("fontFamily",size)

txt1 = Label(text="Hello",bg="black",fg="white",
padx=100,pady=100,font=("Times New Roman",30,BOLD),borderwidth=5,relief=RIDGE)
#side is to allign the Label

txt1.pack(side="bottom" ,anchor="center",fill=X,pady=150)

index.mainloop()
