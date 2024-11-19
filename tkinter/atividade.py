import tkinter as tk


root = tk.Tk()



label2 = tk.Label(root, text = 'Label 2', fg = 'white', background = 'green')

label2.pack(anchor = "n", side = 'left')

label = tk.Label(root, text = 'Label 1', fg = 'white', background= 'blue')

label.pack(anchor = "n", side= 'left')

label3 = tk.Label(root, text = 'Label 3', fg = 'white', background= 'red')
 
label3.pack(anchor = "n", side = 'left')

root.mainloop()