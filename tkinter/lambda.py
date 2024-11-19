from tkinter import *
root = Tk()
 
 
 
def hide_button():
    global B1
    B1.pack_forget()
 
 
def show_button(widget):
   
    widget.pack()
 
 
B1 = Button(root, text="Button 1")
B1.pack()
 
 
B2 = Button(root, text="ocultar b1", command=hide_button)
B2.pack()
B3 = Button(root, text="aparecer b1", command=lambda: show_button(B1))
B3.pack()
 
root.mainloop()
