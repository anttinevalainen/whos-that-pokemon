import unittest
import random as rd
from gameplay.player_score import Player
from gameplay.gamemode import Gamemode

class TestPlayerScore(unittest.TestCase):
    def setUp(self):
        print('Player score test initiation')

    def test_new_player_initializes_correctly(self):
        generation_choice = []
        generation_choice.append(1)

        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)
        rd.shuffle(generation_choice)

        new_gamemode = Gamemode(generation_choice)
        new_player = Player('FFF', new_gamemode)

        gamertag = new_player.get_gamertag()
        points = new_player.get_points()
        answers = new_player.get_correct_answers()
        health = new_player.get_health()
        gamemode = new_player.get_gamemode()
        number_of_gens = gamemode.get_number_of_generations()

        self.assertEqual(gamertag, 'FFF')
        self.assertEqual(points, 0)
        self.assertEqual(answers, 0)
        self.assertEqual(health, 3)
        self.assertEqual(number_of_gens, generation_choice.count(1))

    def test_correct_answer_raises_points_and_answers(self):
        generation_choice = []
        generation_choice.append(1)

        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)
        rd.shuffle(generation_choice)

        new_gamemode = Gamemode(generation_choice)
        new_player = Player('FFF', new_gamemode)

        new_player.correct_answer()
        new_player.correct_answer()
        new_player.correct_answer()

        gamemode = new_player.get_gamemode()
        number_of_gens = gamemode.get_number_of_generations()
        first_round_points = number_of_gens*50*3

        points1 = new_player.get_points()
        answers = new_player.get_correct_answers()
        self.assertEqual(points1, first_round_points)
        self.assertEqual(answers, 3)

        new_player.correct_answer()
        new_player.correct_answer()

        second_round_points = number_of_gens*50*2

        points2 = new_player.get_points()
        answers = new_player.get_correct_answers()
        self.assertTrue(points2 > points1)
        self.assertEqual(points2, first_round_points + second_round_points)
        self.assertEqual(answers, 5)

    def test_incorrect_answer_lowers_health(self):
        generation_choice = []
        generation_choice.append(1)

        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)
        rd.shuffle(generation_choice)

        new_gamemode = Gamemode(generation_choice)
        new_player = Player('FFF', new_gamemode)

        new_player.incorrect_answer()

        health = new_player.get_health()
        self.assertTrue(health == 2)

        new_player.incorrect_answer()
        new_player.incorrect_answer()

        health = new_player.get_health()
        self.assertTrue(health == 0)

    def test_incorrect_wont_make_health_negative(self):
        generation_choice = []
        generation_choice.append(1)

        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)
        rd.shuffle(generation_choice)

        new_gamemode = Gamemode(generation_choice)
        new_player = Player('FFF', new_gamemode)

        new_player.incorrect_answer()
        new_player.incorrect_answer()
        new_player.incorrect_answer()
        new_player.incorrect_answer()

        health = new_player.get_health()
        self.assertTrue(health == 0)

    def test_gamemode_gives_correct_points(self):
        generation_choice1 = [1,1,1,1,1,0]
        gamemode1 = Gamemode(generation_choice1)
        player1 = Player('AAA', gamemode1)

        generation_choice2 = [1,1,1,1,0,0]
        gamemode2 = Gamemode(generation_choice2)
        player2 = Player('BBB', gamemode2)

        generation_choice3 = [1,1,1,0,0,0]
        gamemode3 = Gamemode(generation_choice3)
        player3 = Player('CCC', gamemode3)

        generation_choice4 = [1,1,0,0,0,0]
        gamemode4 = Gamemode(generation_choice4)
        player4 = Player('DDD', gamemode4)

        generation_choice5 = [1,0,0,0,0,0]
        gamemode5 = Gamemode(generation_choice5)
        player5 = Player('EEE', gamemode5)

        player1.correct_answer()
        player2.correct_answer()
        player3.correct_answer()
        player4.correct_answer()
        player5.correct_answer()

        self.assertEqual(player1.get_points(), 250)
        self.assertEqual(player2.get_points(), 200)
        self.assertEqual(player3.get_points(), 150)
        self.assertEqual(player4.get_points(), 100)
        self.assertEqual(player5.get_points(), 50)

        generation_choice = []
        generation_choice.append(1)

        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)
        rd.shuffle(generation_choice)

        new_gamemode = Gamemode(generation_choice)
        new_player = Player('FFF', new_gamemode)

        new_player.correct_answer()

        gamemode = new_player.get_gamemode()
        number_of_gens = gamemode.get_number_of_generations()
        correct_answer_points = number_of_gens*50
        points1 = new_player.get_points()

        self.assertEqual(points1, correct_answer_points)
