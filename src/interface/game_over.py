import tkinter as tk
from gameplay.player_score import Player
import interface.create_widget as cw
import gameplay.hiscore_save as hs
import data.data_handling as dh

class GameOverPage:

    def __init__(self, root, player_score, index_button_action, gamertag_button_action):
        self.root = root
        self.player_score = player_score
        self.index_button_action = index_button_action
        self.gamertag_button_action = gamertag_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the game over page'''
        self.frame = tk.Frame(master = self.root)
        cw.create_background_label(self.root)

        self.health_photoimage = dh.get_health_photoimage(self.player_score)
        cw.create_health_label(self.root, self.health_photoimage)

        cw.create_progress_label(self.root, self.player_score)
        self.gamemode = self.player_score.get_gamemode()

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
                    font = ('Helvetica', 15)
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
                font = ('Helvetica', 10),
                command = self.try_again_pressed
            )
        self.hiscore_page_button.place(
                x = 175,
                y = 250,
                width = 90,
                height = 60
            )

        if self.gamemode.get_revision():
            self.game_over_label['text'] = ("GAME OVER!\n" +
                                            "You're playing in revision mode\n" +
                                            "Score cannot be sent to hiscores")

        elif hs.points_qualify_for_hiscore(self.player_score.get_points()):
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
        else:
            self.game_over_label['text'] = ('GAME OVER!\n' +
                                            'Not enough points for hiscores!\n' +
                                            'Try again?')

    def try_again_pressed(self):
        gamertag = self.player_score.get_gamertag
        gamemode = self.player_score.get_gamemode()
        player_score = Player(gamertag, gamemode)
        self.gamertag_button_action(player_score)

    def send_hiscore_pressed(self):
        hs.add_hiscore(self.player_score)

        self.game_over_label['text'] = 'Hiscore sent! Return to index?'
        self.hiscore_page_button.destroy()
        self.index_button.place(
            x = 175,
            y = 250,
            width = 100,
            height = 60
        )

    def close_frame(self):
        self.frame.destroy()
