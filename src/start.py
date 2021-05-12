import tkinter as tk

from interface.ui import UI

root = tk.Tk()
root.title("Who's that Pokémon?!?!?!?!?!")

ui = UI(root)
ui.start()

root.geometry('640x480')
root.resizable(0,0)

root.mainloop()
