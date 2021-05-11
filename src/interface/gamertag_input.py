import tkinter as tk
from gameplay.player import Player
from gameplay.pokedex import Pokedex
from gameplay.gamemode import Gamemode
import interface.create_widget as cw
import services.gamemode_service as gs

class GamertagPage:
    '''A class for the gamertag/gamemode choosing -page of the
        graphic interface

    Attributes:
        root: The main root of the game
        gamertag_button_action: Action to start a new round
        index_button_action: Action to return to index page
    '''

    def __init__(self, root, gamertag_button_action, index_button_action):
        '''Class constructor for the gamertag page

            Args:
                self
                root: The main window for the whole interface
                gamertag_button_action: Action for the button used to choose
                    the gamertag/gamemode profile picked at the page and start
                    a new game
                index_button_action: Action for the button used to return to
                    the index page
        '''

        self.root = root
        self.gamertag_button_action = gamertag_button_action
        self.index_button_action = index_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the gamertag page

        Args:
            Self

        Returns:
            None'''

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
            y = 20,
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
            y = 90,
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
            y = 160,
            width = 180,
            height = 60
        )

        check_x = 60
        check_y = 225
        check_height = 20
        check_width = 90

        self.gen_one_var = tk.IntVar(value=1)
        self.gen_two_var = tk.IntVar(value=1)
        self.gen_three_var = tk.IntVar(value=1)
        self.gen_four_var = tk.IntVar(value=1)
        self.gen_five_var = tk.IntVar(value=1)
        self.gen_six_var = tk.IntVar(value=1)
        self.gen_seven_var = tk.IntVar(value=1)
        self.gen_eight_var = tk.IntVar(value=1)
        self.mega_var = tk.IntVar(value=1)
        self.giga_var = tk.IntVar(value=1)
        self.alola_var = tk.IntVar(value=1)
        self.galaria_var = tk.IntVar(value=1)
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

        tk.Checkbutton(
            self.root,
            text = 'Gen. VII',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_seven_var
        ).place(
            x = check_x,
            y = check_y + check_height*3,
            width = check_width,
            height= check_height
        )
        tk.Checkbutton(
            self.root,
            text = 'Gen. VIII',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.gen_eight_var
        ).place(
            x = check_x + check_width,
            y = check_y + check_height*3,
            width = check_width,
            height= check_height
        )

        tk.Checkbutton(
            self.root,
            text = 'Mega',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.mega_var
        ).place(
            x = check_x,
            y = check_y + check_height*4,
            width = check_width,
            height= check_height
        )
        tk.Checkbutton(
            self.root,
            text = 'Gigantamax',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.giga_var
        ).place(
            x = check_x + check_width,
            y = check_y + check_height*4,
            width = check_width,
            height= check_height
        )

        tk.Checkbutton(
            self.root,
            text = 'Alolan',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.alola_var
        ).place(
            x = check_x,
            y = check_y + check_height*5,
            width = check_width,
            height= check_height
        )
        tk.Checkbutton(
            self.root,
            text = 'Galarian',
            bg = '#ffcb05',
            fg = '#0f4d88',
            font = (
                'Helvetica',
                7,
                'bold'
            ),
            variable = self.galaria_var
        ).place(
            x = check_x + check_width,
            y = check_y + check_height*5,
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
            y = 360,
            width = 90,
            height = 60
        )

        self.revision_var = tk.IntVar(value=0)
        tk.Checkbutton(
            self.root,
            text = 'REVISION MODE*',
            bg = '#0f4d88',
            fg = '#ffcb05',
            font = (
                'Helvetica',
                10,
                'bold'
            ),
            variable = self.revision_var
        ).place(
            x = 80,
            y = 430,
            width = 140,
            height= 30
        )
        tk.Label(
            self.root,
            text = ('*In revision mode, name of each pokemon ' +
                    'will be displayed on the screen.' + '\n' +
                    'When using the app in revision mode, ' +
                    'your score cannot be sent to hiscores'),
            bg = '#0f4d88',
            fg = '#ffcb05',
            font = (
                'Helvetica',
                7,
                'bold'
            )
        ).place(
            x = 290,
            y = 455,
            width = 350,
            height = 25
        )

        self.root.bind("<Return>", lambda x: self.send_gamertag())

    def send_gamertag(self):
        '''Actions expressed after user has sent chosen their gamertag and
        gamemode and pressed 'Choose!' button

        Args:
            Self

        Returns:
            None'''

        revision = False
        gamertag = str(self.gamertag_entry.get().upper())

        if gamertag == 'KKK':
            self.gamertag_input_label['text'] = 'Choose a different\ngamertag, thank you.'

        elif len(gamertag) == 3 and gamertag.isalpha():
            self.gamertag_input_label['text'] = 'Your gamertag\nwill be ' + gamertag

            if len(self.gen_choice) > 0:
                self.gen_choice.clear()

            self.gen_choice.extend((self.gen_one_var.get(), self.gen_two_var.get(),
                                self.gen_three_var.get(), self.gen_four_var.get(),
                                self.gen_five_var.get(), self.gen_six_var.get(),
                                self.gen_seven_var.get(), self.gen_eight_var.get(),
                                self.mega_var.get(), self.giga_var.get(),
                                self.alola_var.get(), self.galaria_var.get()))
            if self.revision_var.get() == 1:
                revision = True


            gen_value = 0
            for i in range(12):
                gen_value += self.gen_choice[i]
            if gen_value < 1:
                self.gamertag_input_label['text'] = 'Choose at least\none generation!'
            else:
                gamemode = Gamemode(self.gen_choice, revision)
                new_pokedex = gs.create_pokedex_df(self.gen_choice)
                pokedex = Pokedex(new_pokedex)
                player = Player(gamertag, gamemode, pokedex)

                self.checkbox_info_label['text'] = ('Generations chosen: \n' +
                                                    gamemode.get_generations_string()
                                                    )
                self.checkbox_info_label['font'] = ('Helvetica', 10, 'bold')

                play_button = tk.Button(
                self.root,
                text = 'PLAY!',
                bg = '#0f4d88',
                fg = '#ffcb05',
                font = (
                    'Helvetica',
                    20
                ),
                command = lambda: self.gamertag_button_action(player)
                )
                play_button.place(
                x = 280,
                y = 170,
                width = 155,
                height = 100
                )
                self.root.bind(
                    "<Return>",
                    lambda x: self.gamertag_button_action(player))
        else:
            self.gamertag_input_label['text'] = 'Your gamertag must consist\nof three letters (A-Ö)'
            self.gamertag_input_label['font'] = ('Helvetica', 10)

    def close_frame(self):
        '''Actions to close the frame of the gamertag page

        Args:
            Self

        Returns:
            None'''

        self.frame.destroy()
