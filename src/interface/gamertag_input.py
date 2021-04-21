import tkinter as tk
from gameplay.player_score import Player
import gameplay.create_widget as cw

class GamertagPage:

    def __init__(self, root, gamertag_button_action, index_button_action):
        self.root = root
        self.gamertag_button_action = gamertag_button_action
        self.index_button_action = index_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the gamertag input page'''
        self.frame = tk.Frame(master = self.root)
        cw.create_background_label(self.root)

        self.gamertag_input_label = tk.Label(
            self.root,
            text = 'Input your gamertag\nof three letters!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                13
            )
        )
        self.gamertag_input_label.place(
            x = 60,
            y = 100,
            width = 180,
            height = 60
        )

        self.gamertag_entry = tk.Entry(
            self.root,
            bd = 5,
            justify = 'center',
            font = (
                'Helvetica',
                20,
                'bold'
            )
        )
        self.gamertag_entry.place(
            x = 60,
            y = 180,
            width = 90,
            height = 60
        )

        self.gamertag_button = tk.Button(
            self.root,
            text = 'Pick\ngamertag!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                13
            ),
            command = self.send_gamertag
        )
        self.gamertag_button.place(
            x = 150,
            y = 180,
            width = 90,
            height = 60
        )

        index_button = tk.Button(
            self.root,
            text = 'Return to index!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                10
            ),
            command = self.index_button_action
        )
        index_button.place(
            x = 520,
            y = 20,
            width = 100,
            height = 45
        )

    def send_gamertag(self):
        gamertag = str(self.gamertag_entry.get().upper())

        if gamertag == 'KKK':
            self.gamertag_input_label['text'] = 'Choose a different\ngamertag, thank you.'
            self.gamertag_input_label['font'] = ('Helvetica', 10)

        elif len(gamertag) == 3 and gamertag.isalpha():
            self.gamertag_input_label['text'] = 'Your gamertag\nwill be ' + gamertag
            player_score = Player(gamertag)

            play_button = tk.Button(
            self.root,
            text = 'PLAY!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                20
            ),
            command = lambda: self.gamertag_button_action(player_score)
            )
            play_button.place(
            x = 105,
            y = 300,
            width = 90,
            height = 60
            )

        else:
            self.gamertag_input_label['text'] = 'Your gamertag must consist\nof three letters (A-Ö)'
            self.gamertag_input_label['font'] = ('Helvetica', 10)

    def close_frame(self):
        self.frame.destroy()
