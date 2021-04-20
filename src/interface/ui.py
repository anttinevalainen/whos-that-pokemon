from interface.index import IndexPage
from interface.play import PlayPage
from interface.hiscores import HiscorePage
from interface.gamertag_input import GamertagPage
from interface.game_over import GameOverPage
class UI:
    def __init__(self,root):
        self.root  = root
        self.page  = None

    def show_index(self):
        self.close_page()
        self.page  = IndexPage(
            self.root,
            self.show_gamertag_input,
            self.show_hiscores
        )

    def show_gamertag_input(self):
        self.close_page()
        self.page  = GamertagPage(
            self.root,
            self.show_play,
            self.show_index
        )

    def show_play(self, player_score):
        self.close_page()
        self.page  = PlayPage(
            self.root,
            player_score,
            self.show_index,
            self.show_game_over
        )

    def show_game_over(self, player_score):
        self.close_page()
        self.page  = GameOverPage(
            self.root,
            player_score,
            self.show_index,
            self.show_play
        )

    def show_hiscores(self):
        self.close_page()
        self.page  = HiscorePage(
            self.root,
            self.show_index
        )

    def close_page(self):
        if self.page:
            self.page.close_frame()

        self.page  = None

    def start(self):
        self.show_index()
