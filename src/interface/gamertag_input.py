import tkinter as tk
from gameplay.player_score import Player
from gameplay.gamemode import Gamemode
import interface.create_widget as cw

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

        index_button = tk.Button(
            self.root,
            text = 'Return to index!',
            bg = '#0f4d88',
            fg = '#ffcb05',
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
            y = 60,
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
            x = 105,
            y = 130,
            width = 90,
            height = 60
        )

        self.checkbox_info_label = tk.Label(
            self.root,
            text = 'Choose the generations\nyou wish to play with!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                13
            )
        )
        self.checkbox_info_label.place(
            x = 60,
            y = 200,
            width = 180,
            height = 60
        )

        check_x = 60
        check_y = 270
        check_height = 20
        check_width = 90

        self.gen_one_var = tk.IntVar(value=1)
        self.gen_two_var = tk.IntVar(value=1)
        self.gen_three_var = tk.IntVar(value=1)
        self.gen_four_var = tk.IntVar(value=1)
        self.gen_five_var = tk.IntVar(value=1)
        self.gen_six_var = tk.IntVar(value=1)
        self.gen_choice = []

        tk.Checkbutton(
            self.root,
            text = 'Gen. I',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_one_var
        ).place(
            x = check_x,
            y = check_y,
            width = check_width,
            height= check_height
        )
        tk.Checkbutton(
            self.root,
            text = 'Gen. II',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_two_var
        ).place(
            x = check_x + check_width,
            y = check_y,
            width = check_width,
            height= check_height
        )

        tk.Checkbutton(
            self.root,
            text = 'Gen. III',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_three_var
        ).place(
            x = check_x,
            y = check_y + check_height,
            width = check_width,
            height= check_height
        )
        tk.Checkbutton(
            self.root,
            text = 'Gen. IV',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_four_var
        ).place(
            x = check_x + check_width,
            y = check_y + check_height,
            width = check_width,
            height= check_height
        )

        tk.Checkbutton(
            self.root,
            text = 'Gen. V',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_five_var
        ).place(
            x = check_x,
            y = check_y + check_height*2,
            width = check_width,
            height= check_height
        )
        tk.Checkbutton(
            self.root,
            text = 'Gen. VI',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_six_var
        ).place(
            x = check_x + check_width,
            y = check_y + check_height*2,
            width = check_width,
            height= check_height
        )

        self.gamertag_button = tk.Button(
            self.root,
            text = 'Choose!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                13
            ),
            command = self.send_gamertag
        )
        self.gamertag_button.place(
            x = 105,
            y = 340,
            width = 90,
            height = 60
        )

    def send_gamertag(self):
        gamertag = str(self.gamertag_entry.get().upper())

        if gamertag == 'KKK':
            self.gamertag_input_label['text'] = 'Choose a different\ngamertag, thank you.'

        elif len(gamertag) == 3 and gamertag.isalpha():
            self.gamertag_input_label['text'] = 'Your gamertag\nwill be ' + gamertag

            if len(self.gen_choice) > 0:
                self.gen_choice.clear()

            self.gen_choice.extend((self.gen_one_var.get(),
                                self.gen_two_var.get(),self.gen_three_var.get(),
                                self.gen_four_var.get(),self.gen_five_var.get(),
                                self.gen_six_var.get()))


            gen_value = 0
            for i in range(6):
                gen_value += self.gen_choice[i]
            if gen_value < 1:
                self.gamertag_input_label['text'] = 'Choose at least\none generation!'
            else:
                if gen_value > 5:
                    new_gamemode = Gamemode(self.gen_choice)
                    player_score = Player(gamertag, new_gamemode)
                    self.checkbox_info_label['text'] = ('Generations chosen:\n1-6')
                else:
                    new_gamemode = Gamemode(self.gen_choice)
                    player_score = Player(gamertag, new_gamemode)
                    self.checkbox_info_label['text'] = ('Generations chosen: \n' +
                                                        new_gamemode.get_generations_string())

                play_button = tk.Button(
                self.root,
                text = 'PLAY!',
                bg = '#0f4d88',
                fg = '#ffcb05',
                font = (
                    'Helvetica',
                    20
                ),
                command = lambda: self.gamertag_button_action(player_score)
                )
                play_button.place(
                x = 280,
                y = 170,
                width = 155,
                height = 100
                )
        else:
            self.gamertag_input_label['text'] = 'Your gamertag must consist\nof three letters (A-Ö)'
            self.gamertag_input_label['font'] = ('Helvetica', 10)

    def close_frame(self):
        self.frame.destroy()
