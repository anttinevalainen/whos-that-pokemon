import tkinter as tk
import interface.create_widget as cw

class IndexPage:
    '''A class for the hiscore page of the graphic interface

    Attributes:
        root: The main root of the game
        play_button_action: Action to move to the gamertag page
        hiscores_button_action: Action to move to the hiscore page
    '''

    def __init__(self, root, play_button_action, hiscores_button_action):
        '''Class constructor for the hiscore page

            Args:
                self
                root: The main window for the whole interface
                play_button_action: Action to move to the gamertag page
                hiscores_button_action: Action to move to the hiscore page
        '''

        self.root = root
        self.play_button_action = play_button_action
        self.hiscores_button_action = hiscores_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the hiscore page

        Args:
            Self

        Returns:
            None'''

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
        '''Actions to close the frame of the hiscore page

        Args:
            Self

        Returns:
            None'''

        self.frame.destroy()
