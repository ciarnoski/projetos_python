import tkinter as tk

janela = tk.Tk()
janela.geometry("500x40")
janela.title("Grid Layout with Borders")

frame = tk.Frame(janela, borderwidth=2, relief="solid")
frame.pack( fill="both")


seg = tk.Label(frame,anchor= 'w',  text="seg",background= 'black', fg = 'white', borderwidth=1, relief="solid")
seg.grid(row=0, column=1, sticky="nsew")
corseg = tk.Label(frame, background= 'Blue')
corseg.grid(row=1, column=1, sticky="nsew")

ter = tk.Label(frame,anchor= 'w',  text="ter", background= 'black', fg = 'white', borderwidth=1, relief="solid")
ter.grid(row=0, column=2, sticky="nsew")
corseg = tk.Label(frame, background= 'White')
corseg.grid(row=1, column=2, sticky="nsew")

qua = tk.Label(frame,anchor= 'w',  text="quar",background= 'black', fg = 'white',borderwidth=2, relief="solid")
qua.grid(row=0, column=3, sticky="nsew")
corqua = tk.Label(frame, background= 'Blue')
corqua.grid(row=1, column=3, sticky="nsew")


qui = tk.Label(frame,anchor= 'w',  text="quin",background= 'black', fg = 'white',borderwidth=2, relief="solid")
qui.grid(row=0, column=4, sticky="nsew")
corqui = tk.Label(frame, background= 'White')
corqui.grid(row=1, column=4, sticky="nsew")

sex = tk.Label(frame,anchor= 'w',  text="sexta",background= 'black', fg = 'white',borderwidth=2, relief="solid")
sex.grid(row=0, column=5, sticky="nsew")
corsex = tk.Label(frame, background= 'orange')
corsex.grid(row=1, column=5, sticky="nsew")

sab = tk.Label(frame,anchor= 'w',  text="sáb",background= 'black', fg = 'white',borderwidth=2, relief="solid")
sab.grid(row=0, column=6, sticky="nsew")
corsab = tk.Label(frame, background= 'white')
corsab.grid(row=1, column=6, sticky="nsew")

dom = tk.Label(frame,anchor= 'w',  text="dom",background= 'black', fg = 'white',borderwidth=2, relief="solid")
dom.grid(row=0, column=7, sticky="nsew")
cordom = tk.Label(frame, background= 'blue')
cordom.grid(row=1, column=7, sticky="nsew")

for i in range(1, 8):
    frame.grid_columnconfigure(i, weight=1)


janela.mainloop()