import tkinter as tk
import gameplay.create_widget as cw

class HiscorePage:

    def __init__(self, root, index_button_action):
        self.root = root
        self.index_button_action = index_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the high score page'''

        self.frame = tk.Frame(master = self.root)
        cw.create_background_label(self.root)

        cw.create_hiscore_table(self.root)

        index_button = tk.Button(
            self.root,
            text = 'Return to index!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = ('Helvetica', 10),
            command  = self.index_button_action
        )

        index_button.place(x = 520, y = 20, width = 100, height = 44)

    def close_frame(self):
        self.frame.destroy()
