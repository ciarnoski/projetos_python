import tkinter as tk


root = tk.Tk()
def esc(event):
    print("voce apertou esc")
root.bind("<Escape>",esc)
root.mainloop()
