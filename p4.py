import tkinter as tk
main = tk.Tk()
main.title("Python GUI")
button = tk.Button(main,text="Stop",width=25,command=main.destroy)
button.pack()
main.mainloop()