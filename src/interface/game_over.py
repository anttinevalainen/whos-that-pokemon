import tkinter as tk

from gameplay.player import Player
from gameplay.pokedex import Pokedex
import interface.create_widget as cw
import services.hiscore_service as hs
import services.player_service as ps
import services.gamemode_service as gs

class GameOverPage:
    '''A class for the game over -page of the graphic interface

    Attributes:
        root: The main root of the game
        player: Current player profile
        index_button_action: Action to return to index page
        gamertag_button_action: Action to start a new round
    '''

    def __init__(self, root, player, index_button_action, gamertag_button_action):
        '''Class constructor for the game over page

            Args:
                self
                root: The main window for the whole interface
                player: current player profile
                index_button_action: Action for the button used to return to
                    the index page
                gamertag_button_action: Action for the button used to choose
                    to play the game again with same gamemode as before
        '''

        self.root = root
        self.player = player
        self.index_button_action = index_button_action
        self.gamertag_button_action = gamertag_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the game over page

        Args:
            Self

        Returns:
            None'''

        self.frame = tk.Frame(master = self.root)
        cw.create_background_label(self.root)

        self.health_photoimage = ps.get_health_photoimage(self.player)
        cw.create_health_label(self.root, self.health_photoimage)
        cw.create_progress_label(self.root, self.player)

        self.gamemode = self.player.get_gamemode()
        self.pokedex = self.player.get_pokedex()

        self.index_button = tk.Button(
            self.root,
            text = 'Return to index!',
            bg = '#0f4d88',
            fg = '#ffcb05',
            font = ('Helvetica', 10),
            command  = self.index_button_action
        )
        self.index_button.place(
            x = 520,
            y = 20,
            width = 100,
            height = 45
        )

        self.game_over_label = tk.Label(
                    self.root,
                    text = '',
                    bg = '#ec3025',
                    fg = '#0f4d88',
                    font = ('Helvetica', 10)
                )
        self.game_over_label.place(
                    x = 70,
                    y = 130,
                    width = 300,
                    height = 100
                )

        self.hiscore_page_button = tk.Button(
                self.root,
                text = 'Try again!',
                bg = '#ec3025',
                fg = '#0f4d88',
                font = ('Helvetica', 13),
                command = self.try_again_pressed
            )
        self.hiscore_page_button.place(
                x = 175,
                y = 250,
                width = 90,
                height = 60
            )
        self.root.bind(
                    "<Return>",
                    lambda x: self.try_again_pressed())

        if self.gamemode.get_revision():
            self.game_over_label['text'] = ('GAME OVER! No Pokémon left to show!\n' +
                                            "You're playing in revision mode\n" +
                                            'Score cannot be sent to hiscores')
            self.game_over_label['font'] = ('Helvetica', 10)

        elif hs.points_qualify_for_hiscore(self.player.get_points()):
            if self.pokedex.is_empty():
                self.game_over_label['text'] = ('GAME OVER!\n' +
                                            'No more Pokémon left\n' +
                                            'Send score to hiscores?')
            else:
                self.game_over_label['text'] = ('GAME OVER!\n' +
                                                '-\n' +
                                                'Send score to hiscores?')

            self.hiscore_page_button['text'] = 'Send Hiscore'
            self.hiscore_page_button['command'] = self.send_hiscore_pressed
            self.hiscore_page_button.place(
                x = 175,
                y = 250,
                width = 100,
                height = 60
            )
            self.root.bind(
                    "<Return>",
                    lambda x: self.send_hiscore_pressed())

        elif self.pokedex.is_empty():
            self.game_over_label['text'] = ('GAME OVER! No Pokémon left to show!\n' +
                                            'Not enough points for hiscores!\n' +
                                            'Try again?')
            self.game_over_label['font'] = ('Helvetica', 10)
        else:
            self.game_over_label['text'] = ('GAME OVER!\n' +
                                            'Not enough points for hiscores!\n' +
                                            'Try again?')

    def send_hiscore_pressed(self):
        '''Actions expressed after user has sent their hiscore to the leaderboards

        Args:
            Self

        Returns:
            None'''

        hs.add_hiscore(self.player)

        self.game_over_label['text'] = 'Hiscore sent! Try again??'
        self.hiscore_page_button['text'] = 'Try again!'
        self.hiscore_page_button['command'] = self.try_again_pressed
        self.root.bind(
                    "<Return>",
                    lambda x: self.try_again_pressed())


    def try_again_pressed(self):
        '''Actions expressed after user has pressed the try again -button

        Args:
            Self

        Returns:
            None'''

        gamertag = self.player.get_gamertag()
        gamemode = self.player.get_gamemode()
        genchoicelist = gamemode.get_genchoice()
        reset_pokedex = gs.create_pokedex_df(genchoicelist)
        pokedex = Pokedex(reset_pokedex)
        player = Player(gamertag, gamemode, pokedex)
        self.gamertag_button_action(player)

    def close_frame(self):
        '''Actions to close the frame of the game over page

        Args:
            Self

        Returns:
            None'''

        self.frame.destroy()
