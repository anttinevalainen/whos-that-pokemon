import random
import pandas as pd
from PIL import Image, ImageTk
import tkinter as tk
from data_handling import get_random_filename, get_silhouette, get_pokemon_name, get_pokemon_image, get_silhouette_image, get_pokemon_data

class UiTest(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("Who's that Pokémon?!?!?!")
        self.geometry('640x480')
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (IndexPage, PlayPage, HiScorePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.switch_page(IndexPage)

    def switch_page(self, c):
        frame = self.frames[c]
        frame.tkraise()

class IndexPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file = 'data/png/whos_that_pokemon.png')
        BGlabel = tk.Label(self,image = logo)
        BGlabel.image = logo
        BGlabel.place(x = 0,y = 0,width = 640,height = 480)
        label = tk.Label(
            self, 
            text = 'Index page!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica')
        label.place(x = 80,y = 20,width = 160,height = 44)

        button1 = tk.Button(
            self, 
            text = 'Play!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica',
            command = lambda: controller.switch_page(PlayPage)
        )
        button2 = tk.Button(
            self, 
            text = 'Hiscores!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica',
            command = lambda: controller.switch_page(HiScorePage)
        )
        button3 = tk.Button(
            self, 
            text = 'Exit!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica',
            command = self.quit
        )

        button1.place(x = 100,y = 150,width = 100,height = 44)
        button2.place(x = 100,y = 225,width = 100,height = 44)
        button3.place(x = 100,y = 300,width = 100,height = 44)

class PlayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file = 'data/png/whos_that_pokemon.png')
        BGlabel = tk.Label(self,image = logo)
        BGlabel.image = logo
        BGlabel.place(x = 0,y = 0,width = 640,height = 480)
        label = tk.Label(
            self, 
            text = "?!?!?!?!", 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 20)
            )
        label.place(x = 80,y = 20,width = 160,height = 44)

        random_filename, silhouette_filename, pokemon_name_string, silhouette_image, pokemon_image = get_pokemon_data()

        image_background = Image.open('data/png/image_background.png').convert("RGBA")
        image_background.paste(silhouette_image, (0, 0), silhouette_image)
        self.label_picture = ImageTk.PhotoImage(image_background)
        img = tk.Label(master = self, image = self.label_picture, bd = 0, highlightthickness = 0, relief = 'ridge')
        img.place(x = 33, y = 104)


        button1 = tk.Button(
            self, 
            text = 'Return to index!', 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 10),
            command = lambda: controller.switch_page(IndexPage)
        )
        button2 = tk.Button(
            self, 
            text = '!', 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 20),
            #command = [[send answer]]
        )

        button1.place(x = 520, y = 20, width = 100, height = 44)
        button2.place(x = 230,y = 395, width = 44, height = 44)


        answer = tk.Entry(
            self,
            bd = 4,
            font = ('Helvetica',10,'bold')
        )

        answer.place(x = 20, y = 400, width = 200, height = 30)

class HiScorePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file = 'data/png/whos_that_pokemon.png')
        BGlabel = tk.Label(self,image = logo)
        BGlabel.image = logo
        BGlabel.place(x = 0,y = 0,width = 640,height = 480)
        label = tk.Label(
            self, 
            text = "High scores!", 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 20)
            )
        label.place(x = 80,y = 20,width = 160,height = 44)

        button1 = tk.Button(
            self, 
            text = 'Return to index!', 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 10),
            command = lambda: controller.switch_page(IndexPage)
        )

        button1.place(x = 520, y = 20, width = 100, height = 44)

if __name__ ==  '__main__':
    app = UiTest()
    app.mainloop()
