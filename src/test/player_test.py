import unittest
import random as rd
import services.gamemode_service as gs
from gameplay.player import Player
from gameplay.gamemode import Gamemode
from gameplay.pokedex import Pokedex

class TestPlayer(unittest.TestCase):
    def setUp(self):
        print('Player score test initiation')

    def test_player_initializes_correctly(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        pokedex = Pokedex(gs.create_pokedex_df(genchoice))
        player = Player('TTT', gamemode, pokedex)

        gamertag = player.get_gamertag()
        points = player.get_points()
        answers = player.get_correct_answers()
        health = player.get_health()
        gamemode = player.get_gamemode()
        number_of_gens = gamemode.get_number_of_generations()

        self.assertEqual(gamertag, 'TTT')
        self.assertEqual(points, 0)
        self.assertEqual(answers, 0)
        self.assertEqual(health, 3)
        self.assertEqual(number_of_gens, genchoice.count(1))
