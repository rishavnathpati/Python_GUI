from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Sudoku Solver and Player")
# Window parameters
root.geometry("600x600")  # width x height
root.minsize(500, 500)  # width,height
root.maxsize(1080, 1080)  # width,height
###################################################################################################################

# Title label
sudoku_welcome_label = Label(text="Sudoku Game-Solve and Play")
sudoku_welcome_label.pack()
###################################################################################################################

# Important Label options
# text - adds text
# bd-background
# fg-foreground
# font - sets the font
# font=("comicsans 10 bold")
# padx,pady - padding for x and y
# relief- border styling - SUNKEN,RAISED,GROOVE,RIDGE
title_label = Label(text='''The tkinter package (“Tk interface”)''', bg="red", fg="yellow",
                    padx=20, pady=10, font="comicsansms 10 bold", borderwidth=10, relief=RAISED)
###################################################################################################################

# Important Pack options
# anchor = nw
# side= top,bottom,left,right
# Need to pack after adding any widget
title_label.pack(side=TOP, anchor="sw", fill=X, padx=10, pady=10)
###################################################################################################################

# Frames-kinda like boxes
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
Label(f1, text="Sudoku solve left side").pack(pady=20)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=7, relief=SUNKEN)
Label(f2, text="Sudoku solve top side").pack(pady=20)
f2.pack(side=TOP, fill=X)

# Photo Loading
# photo = PhotoImage(file="image.png")
# photo_label = Label(image=photo)
# photo_label.pack()

root.mainloop()
