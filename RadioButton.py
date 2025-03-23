from tkinter import *

root = Tk()
v = IntVar()
Radiobutton(root, text='python', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='C++', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='Java', variable=v, value=3).pack(anchor=W)
Radiobutton(root, text='PHP', variable=v, value=4).pack(anchor=W)
mainloop()
