import tkinter as tk
from data_handling_new import get_random_filename, get_silhouette, get_pokemon_name, get_pokemon_image, get_silhouette_image
from PIL import Image, ImageTk

class Gamestage:

    def __init__(self, root):
        self.root = root
        self.Frame = None
        pokemon_filename = None
        silhouette_filename = None
        pokemon_name = None
        pokemon_image = None
        silhouette_image = None
        self.initialize()

    def initialize(self):
        self.frame = tk.Frame(master=self.root, width=10, height=1)
        pokemon_filename = get_random_filename()
        silhouette_filename = get_silhouette(pokemon_filename)
        pokemon_name = get_pokemon_name(pokemon_filename)
        pokemon_image = get_pokemon_image(pokemon_filename)
        silhouette_image = get_silhouette_image(silhouette_filename)

        # create a canvas to show image on
        canvas_for_image = tk.Canvas(self.frame, height=256, width=256, borderwidth=0, highlightthickness=0)
        # canvas_for_image.grid(row=0, column=0, sticky='nesw', padx=0, pady=0)

        # create image from image location resize it to 200X200 and put in on canvas

        canvas_for_image.image = ImageTk.PhotoImage(silhouette_image, Image.ANTIALIAS)
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')

    def exit(self):
        self.root.destroy()

    def pack(self):
        self.frame.pack()
