import tkinter as tk

class Hiscore_page:

    def __init__(self, root):
        self.root = root
        self.initialize()

    def initialize(self):
        self.frame = tk.Frame(master = self.root)

        background_image = tk.PhotoImage(file = '/data/png/whos_that_pokemon.png')
        background_label = tk.Label(self.root,image = background_image)
        background_label.image = background_image
        background_label.place(x = 0,y = 0,width = 640,height = 480)
        label = tk.Label(
            self.root, 
            text = "High scores!", 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 20)
            )
        label.place(x = 80,y = 50,width = 160,height = 44)

        button1 = tk.Button(
            self.root, 
            text = 'Return to index!', 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 10),
            #command = 
        )

        button1.place(x = 520, y = 20, width = 100, height = 44)

    def pack(self):
        self.frame.pack()

    def close_frame(self):
        self.frame.destroy()