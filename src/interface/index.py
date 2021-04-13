import tkinter as tk

class Index_page:

    def __init__(self, root):
        self.root = root
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the index page'''
        '''Button commands & page transitions still under construction'''
        self.frame = tk.Frame(master = self.root)

        background_image = tk.PhotoImage(file = 'png/whos_that_pokemon.png')
        background_label = tk.Label(self.root,image = background_image)
        background_label.image = background_image
        background_label.place(x = 0,y = 0,width = 640,height = 480)

        label = tk.Label(
            self.root, 
            text = 'Index page!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica')
        label.place(x = 80,y = 20,width = 160,height = 44)

        button1 = tk.Button(
            self.root, 
            text = 'Play!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica',
            #command = self.play_button_pushed
        )
        button1.place(x = 100,y = 150,width = 100,height = 44)

        button2 = tk.Button(
            self.root, 
            text = 'Hiscores!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica',
            #command = lambda: controller.switch_page(HiScorePage)
        )
        button2.place(x = 100,y = 225,width = 100,height = 44)

        button3 = tk.Button(
            self.root, 
            text = 'Exit!', 
            bg = 'red',
            fg = 'blue',
            font = 'Helvetica',
            command = self.root.quit
        )
        button3.place(x = 100,y = 300,width = 100,height = 44)

    def close_frame(self):
        self.frame.destroy()

    #def play_button_pushed(self):
        #self.show_play()