import unittest
from gameplay.player_score import Player

class TestPlayerScore(unittest.TestCase):
    def setUp(self):
        print('setup')

    def test_new_player_initializes_correctly(self):
        new_player = Player('FFF')
        gamertag = new_player.get_gamertag()
        points = new_player.get_points()
        answers = new_player.get_correct_answers()
        health = new_player.get_health()
        self.assertEqual(gamertag, 'FFF')
        self.assertEqual(points, 0)
        self.assertEqual(answers, 0)
        self.assertEqual(health, 3)

    def test_correct_answer_raises_points_and_answers(self):
        new_player = Player('FFF')

        new_player.correct_answer()
        new_player.correct_answer()
        new_player.correct_answer()

        points1 = new_player.get_points()
        answers = new_player.get_correct_answers()
        self.assertTrue(points1 > 0)
        self.assertEqual(answers, 3)

        new_player.correct_answer()
        new_player.correct_answer()

        points2 = new_player.get_points()
        answers = new_player.get_correct_answers()
        self.assertTrue(points2 > points1)
        self.assertEqual(answers, 5)

    def test_incorrect_answer_lowers_health(self):
        new_player = Player('FFF')

        new_player.incorrect_answer()

        health = new_player.get_health()
        self.assertTrue(health == 2)

        new_player.incorrect_answer()
        new_player.incorrect_answer()

        health = new_player.get_health()
        self.assertTrue(health == 0)

    def test_incorrect_wont_make_health_negative(self):
        new_player = Player('FFF')

        new_player.incorrect_answer()
        new_player.incorrect_answer()
        new_player.incorrect_answer()
        new_player.incorrect_answer()

        health = new_player.get_health()
        self.assertTrue(health == 0)
