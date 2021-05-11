from interface.index import IndexPage
from interface.play import PlayPage
from interface.hiscores import HiscorePage
from interface.gamertag_input import GamertagPage
from interface.game_over import GameOverPage

class UI:
    '''A class for the Who's that pokemon -app's graphic interface

    Attributes:
        root: The main root of the game
    '''

    def __init__(self,root):
        '''Class constructor for the gameplay page

            Args:
                self
                root: The main window for the whole interface
        '''

        self.root  = root
        self.page  = None

    def show_index(self):
        '''switches the page to index page

        Args:
            Self

        Returns:
            None'''

        self.close_page()
        self.page  = IndexPage(
            self.root,
            self.show_gamertag_input,
            self.show_hiscores
        )

    def show_gamertag_input(self):
        '''switches the page to gamertag page

        Args:
            Self

        Returns:
            None'''

        self.close_page()
        self.page  = GamertagPage(
            self.root,
            self.show_play,
            self.show_index
        )

    def show_play(self, player):
        '''switches the page to gameplay page

        Args:
            Self
            player: The Player object created at gamertag page

        Returns:
            None'''

        self.close_page()
        self.page  = PlayPage(
            self.root,
            player,
            self.show_index,
            self.show_game_over
        )

    def show_game_over(self, player):
        '''switches the page to game over page

        Args:
            Self
            player: The Player object of the current round

        Returns:
            None'''

        self.close_page()
        self.page  = GameOverPage(
            self.root,
            player,
            self.show_index,
            self.show_play
        )

    def show_hiscores(self):
        '''switches the page to hiscore page

        Args:
            Self

        Returns:
            None'''

        self.close_page()
        self.page  = HiscorePage(
            self.root,
            self.show_index
        )

    def close_page(self):
        '''closes the current page and resets the self.page variable

        Args:
            Self

        Returns:
            None'''

        if self.page:
            self.page.close_frame()

        self.page  = None

    def start(self):
        '''starts the graphic interface and moves to the index page

        Args:
            Self

        Returns:
            None'''

        self.show_index()
