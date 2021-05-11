import tkinter as tk
import services.player_service as ps
import services.pokemon_service as pks
import interface.create_widget as cw

class PlayPage:
    '''A class for the gameplay page of the graphic interface

    Attributes:
        root: The main root of the game
        player: The current player object
        index_button_action: Action to return to index page
        game_over_action: Action to move to the game over -page
    '''

    def __init__(self, root, player, index_button_action, game_over_action):
        '''Class constructor for the gameplay page

            Args:
                self
                root: The main window for the whole interface
                player: current player profile
                index_button_action: Action for the button used to return to
                    the index page
                game_over_action: Action to switch the page to game over and
                    end the game
        '''

        self.root = root
        self.player = player
        self.gamemode = self.player.get_gamemode()
        self.index_button_action = index_button_action
        self.game_over_action = game_over_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the hiscore page

        Args:
            Self

        Returns:
            None'''

        self.frame = tk.Frame(self.root)
        cw.create_background_label(self.root)

        self.pokedex = self.player.get_pokedex()
        self.pokemon = self.pokedex.get_random_pokemon()

        self.pokemon_name = self.pokemon.get_name()

        self.s_filename = self.pokemon.get_silhouette_fp()
        self.p_filename = self.pokemon.get_picture_fp()

        self.s_photoimage = pks.get_pokemon_photoimage(self.s_filename)
        self.p_photoimage = pks.get_pokemon_photoimage(self.p_filename)

        self.health_photoimage = ps.get_health_photoimage(self.player)

        cw.create_health_label(self.root, self.health_photoimage)
        cw.create_progress_label(self.root, self.player)
        cw.create_pokemon_label(self.root, self.s_photoimage)

        tk.Button(
            self.root,
            text = 'Return to index!',
            bg = '#0f4d88',
            fg = '#ffcb05',
            font = ('Helvetica', 10),
            command  = self.index_button_action
        ).place(
            x = 520,
            y = 20,
            width = 100,
            height = 45
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
        #self.answer.insert(index = 0, string = self.pokemon_name)

        self.send_answer_button = tk.Button(
            self.root,
            text = '!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = ('Helvetica', 20),
            command = self.send_answer
        )
        self.send_answer_button.place(
            x = 230,
            y = 395,
            width = 45,
            height = 45
        )

        if self.gamemode.get_revision():
            tk.Label(
                self.root,
                text = "Psst...! It's " + self.pokemon_name + '!',
                bg = '#ec3025',
                fg = '#0f4d88',
                font = ('Helvetica', 10, 'bold')
            ).place(
                x=0,
                y=460,
                width=200,
                height=20
            )

        self.root.bind("<Return>", lambda x: self.send_answer())
        self.answer.focus_set()

    def send_answer(self):
        '''Actions expressed after user has sent their answer with '!'
        button

        Args:
            Self

        Returns:
            None'''

        self.background = tk.PhotoImage(file = 'src/data/png/text_background.png')
        self.correct, self.text = ps.check_answer(self.pokemon, self.answer.get())

        if self.correct:
            ps.correct_answer(self.player, self.pokemon)
        else:
            ps.incorrect_answer(self.player, self.pokemon)

        cw.create_answer_canvas(self.root, self.text, self.background)
        cw.create_pokemon_label(self.root, self.p_photoimage)

        self.health_photoimage = ps.get_health_photoimage(self.player)
        cw.create_health_label(self.root, self.health_photoimage)

        self.send_answer_button['text'] = 'Next!'
        self.send_answer_button['font'] = ('Helvetica', 10)
        self.send_answer_button['command'] = self.next_button_pressed
        self.root.bind("<Return>", lambda x: self.next_button_pressed())

    def next_button_pressed(self):
        '''Actions expressed after user gotten the answer correct or incorrect
        and pressed the 'Next!'-button

        Args:
            Self

        Returns:
            None'''

        if self.player.get_health() < 1 or self.pokedex.is_empty():
            self.game_over_action(self.player)
        else:
            self.close_frame()
            self.initialize()

    def close_frame(self):
        '''Actions to close the frame of the hiscore page

        Args:
            Self

        Returns:
            None'''

        self.frame.destroy()
