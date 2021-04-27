import tkinter as tk
import interface.create_widget as cw

class IndexPage:

    def __init__(self, root, play_button_action, hiscores_button_action):
        self.root = root
        self.play_button_action = play_button_action
        self.hiscores_button_action = hiscores_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the index page'''
        self.frame = tk.Frame(master = self.root)
        cw.create_background_label(self.root)

        play_button = tk.Button(
            self.root,
            text = 'Play!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = 'Helvetica',
            command = self.play_button_action
        )
        play_button.place(
            x = 100,
            y = 150,
            width = 100,
            height = 45
        )

        hiscore_button = tk.Button(
            self.root,
            text = 'Hiscores!',
            bg = '#0f4d88',
            fg = '#ffcb05',
            font = 'Helvetica',
            command = self.hiscores_button_action
        )
        hiscore_button.place(
            x = 100,
            y = 225,
            width = 100,
            height = 45
        )

        exit_button = tk.Button(
            self.root,
            text = 'Exit!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = 'Helvetica',
            command = self.root.quit
        )
        exit_button.place(
            x = 100,
            y = 300,
            width = 100,
            height = 45
        )

    def close_frame(self):
        self.frame.destroy()
