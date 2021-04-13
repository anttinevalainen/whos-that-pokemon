import tkinter as tk
import data_handling as dh

class Play_page:

    def __init__(self, root):
        self.root = root
        self.initialize()

    def initialize(self):
        self.frame = tk.Frame(self.root)
        random_filename, silhouette_filename, self.pokemon_name_string, self.pokemon_full_name_string, silhouette_image, pokemon_image, self.silhouette_photoimage, self.pokemon_photoimage = dh.get_pokemon_data()

        background_image = tk.PhotoImage(file = 'data/png/whos_that_pokemon.png')
        background_label = tk.Label(self.root,image = background_image)
        background_label.image = background_image
        background_label.place(x = 0,y = 0,width = 640,height = 480)

        label = tk.Label(
            self.root, 
            text = "?!?!?!?!", 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 20)
            )
        label.place(x = 80,y = 20,width = 160,height = 44)

        self.create_silhouette_label(self.silhouette_photoimage)

        button1 = tk.Button(
            self.root, 
            text = 'Return to index!', 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 10),
            #command  = 
        )
        button1.place(
            x = 520, 
            y = 20, 
            width = 100, 
            height = 44
        )

        self.answer = tk.Entry(
            self.root,
            bd = 4,
            font = ('Helvetica',10,'bold')
        )
        self.answer.place(
            x = 20, 
            y = 400, 
            width = 200, 
            height = 30
        )
        button2 = tk.Button(
            self.root, 
            text = '!', 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 20),
            command = self.send_answer
        )
        button2.place(
            x = 230,
            y = 395, 
            width = 44, 
            height = 44
        )

    def create_silhouette_label(self, silhouette_photoimage):
        silhouette_label = tk.Label(
            self.root, 
            image = self.silhouette_photoimage, 
            bd = 0, 
            highlightthickness = 0, 
            relief = 'ridge'
        )
        silhouette_label.place(
            x =  33, 
            y = 104
        )

    def create_pokemon_label(self, pokemon_photoimage):
        pokemon_label = tk.Label(
            self.root, 
            image = self.pokemon_photoimage, 
            bd = 0, 
            highlightthickness = 0, 
            relief = 'ridge'
        )
        pokemon_label.place(
            x =  33, 
            y = 104
        )

    def send_answer(self):
        if self.pokemon_name_string.lower() ==  self.answer.get().lower():

            self.background, self.text = dh.get_correct_answer(self.pokemon_full_name_string)

            text_canvas = tk.Canvas(
                self.root, 
                bd = 0, 
                highlightthickness = 0, 
                relief = 'ridge'
            )
            text_canvas.place(
                x = 20, 
                y = 400, 
                width = 200, 
                height = 60
            )
            text_canvas.create_image(
                200/2,
                60/2, 
                image = self.background
            )
            text_canvas.create_text(
                200/2,
                20,
                text = self.text, 
                font = ("Helvetica", 13), 
                fill = 'blue'
            )

        else:

            self.background, self.text = dh.get_incorrect_answer(self.pokemon_full_name_string)
            text_canvas = tk.Canvas(
                self.root, 
                bd = 0, 
                highlightthickness = 0, 
                relief = 'ridge'
            )
            text_canvas.place(
                x = 20, 
                y = 400, 
                width = 200, 
                height = 60
            )
            text_canvas.create_image(
                200/2,
                60/2, 
                image = self.background
            )
            text_canvas.create_text(
                200/2, 
                20,
                text = self.text, 
                font = ("Helvetica", 13), 
                fill = 'blue'
            )

        self.create_pokemon_label(self.pokemon_photoimage)

        next_button = tk.Button(
            self.root, 
            text = 'Next!', 
            bg = 'red',
            fg = 'blue',
            font = ("Helvetica", 10),
            command = self.next_button_pressed
        )
        next_button.place(
            x = 230,
            y = 395, 
            width = 44, 
            height = 44
        )


    def next_button_pressed(self):
        self.close_frame()
        self.initialize()
        #self.pack()

    def close_frame(self):
        self.frame.destroy()

    #def pack(self):
        #self.frame.pack()