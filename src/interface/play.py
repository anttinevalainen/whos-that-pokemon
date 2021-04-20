import tkinter as tk
import data.data_handling as dh
import gameplay.create_widget as cw

class PlayPage:

    def __init__(self, root, player_score, index_button_action, game_over_button_action):
        self.root = root
        self.player_score = player_score
        self.index_button_action = index_button_action
        self.game_over_button_action = game_over_button_action
        self.initialize()

    def initialize(self):
        '''Initializes the graphic interface for the play page'''
        self.frame = tk.Frame(self.root)

        cw.create_background_label(self.root)

        (self.pokemon_full_name_string, self.silhouette_photoimage,
        self.pokemon_photoimage) = dh.get_pokemon_data()

        self.health_photoimage = dh.get_health_photoimage(self.player_score)

        cw.create_progress_label(self.root, self.player_score)

        cw.create_health_label(self.root, self.health_photoimage)

        cw.create_pokemon_label(self.root, self.silhouette_photoimage)

        index_button = tk.Button(
            self.root,
            text = 'Return to index!',
            bg = '#ec3025',
            fg = '#0f4d88',
            font = ('Helvetica', 10),
            command  = self.index_button_action
        )
        index_button.place(
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

    def send_answer(self):
        (self.background,
        self.text,
        self.correct)= dh.check_answer(self.pokemon_full_name_string, self.answer.get())

        if self.correct:
            self.player_score.correct_answer()
            cw.create_answer_canvas(self.root, self.background, self.text)
        else:
            self.player_score.incorrect_answer()
            cw.create_answer_canvas(self.root, self.background, self.text)

        cw.create_pokemon_label(self.root, self.pokemon_photoimage)

        self.send_answer_button['text'] = 'Next!'
        self.send_answer_button['font'] = ('Helvetica', 10)
        self.send_answer_button['command'] = self.next_button_pressed

    def next_button_pressed(self):
        if self.player_score.get_health() < 1:
            self.game_over_button_action(self.player_score)
        else:
            self.close_frame()
            self.initialize()

    def close_frame(self):
        self.frame.destroy()
