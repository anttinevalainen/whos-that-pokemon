import tkinter as tk

import interface.create_widget as cw

class HiscorePage:
    '''A class for the hiscore page of the graphic interface

    Attributes:
        root: The main root of the game
        index_button_action: Action to return to index page
    '''

    def __init__(self, root, index_button_action):
        '''Class constructor for the hiscore page

            Args:
                self
                root: The main window for the whole interface
                index_button_action: Action for the button used to return to
                    the index page
        '''

        self.root = root
        self.index_button_action = index_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the hiscore page

        Args:
            Self

        Returns:
            None'''

        self.frame = tk.Frame(master = self.root)
        cw.create_background_label(self.root)

        cw.create_hiscore_table(self.root)

        index_button = tk.Button(
            self.root,
            text = 'Return to index!',
            bg = '#0f4d88',
            fg = '#ffcb05',
            font = ('Helvetica', 10),
            command  = self.index_button_action
        )

        index_button.place(x = 520, y = 20, width = 100, height = 44)

        self.root.bind("<Return>", lambda x: self.index_button_action())

    def close_frame(self):
        '''Actions to close the frame of the hiscore page

        Args:
            Self

        Returns:
            None'''

        self.frame.destroy()
