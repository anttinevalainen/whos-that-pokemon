from src.interface.index import Index_page
from src.interface.play import Play_page
from src.interface.hiscores import Hiscore_page

class UI:
    def __init__(self,root):
        self.root  = root
        self.page  = None

    def show_index(self):
        self.close_page()
        self.page  = Index_page(
            self.root,
        )

    def show_play(self):
        self.close_page()
        self.page  = Play_page(
            self.root
        )

    def show_hiscores(self):
        self.close_page()
        self.page  = Hiscore_page(
            self.root,
        )

    def close_page(self):
        if self.page:
            self.page.close_frame()

        self.page  = None

    def start(self):
        self.show_play()