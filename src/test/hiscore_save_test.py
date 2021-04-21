import unittest
import os
import pandas as pd
import gameplay.hiscore_save as hs
from gameplay.player_score import Player

class TestHiscoreSave(unittest.TestCase):
    def setUp(self):
        self.table_filepath = 'src/data/hiscores.csv'

    def test_initialization_creates_hiscore_table_if_doesnt_exist(self):
        if os.path.exists(self.table_filepath):
            table_copy = pd.read_csv(self.table_filepath, sep=',')
            os.remove(self.table_filepath)

        hs.initialize_hiscore_dataframe()
        hiscore_df = pd.read_csv(self.table_filepath, sep=',')
        row_gamertag = hiscore_df.at[3, 'gamertag']
        row_points = hiscore_df.at[3, 'points']
        row_answers = hiscore_df.at[3, 'correct_answers']

        self.assertTrue(os.path.exists(self.table_filepath))
        self.assertTrue(row_gamertag == 'NAN')
        self.assertTrue(row_points == 0)
        self.assertTrue(row_answers == 0)

        try:
            table_copy.to_csv(self.table_filepath, index = False)
        except NameError:
            pass

    def test_initialization_wont_create_new_hiscore_if_one_exists(self):
        if os.path.exists(self.table_filepath):
            table_copy = pd.read_csv(self.table_filepath, sep=',')
            os.remove(self.table_filepath)

        data = {'gamertag':['AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA'],
                'points':[1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
                'correct_answers':[1, 1, 1, 1, 1, 1, 1, 1, 1]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(self.table_filepath, index = False)

        hs.initialize_hiscore_dataframe()
        row_gamertag = hiscore_df.at[3, 'gamertag']
        row_points = hiscore_df.at[3, 'points']
        row_answers = hiscore_df.at[3, 'correct_answers']
        self.assertTrue(row_gamertag == 'AAA')
        self.assertTrue(row_points == 1000)
        self.assertTrue(row_answers == 1)

        try:
            table_copy.to_csv(self.table_filepath, index = False)
        except NameError:
            pass

    def test_app_initializes_hiscores_if_csv_file_size_not_correct_size(self):
        if os.path.exists(self.table_filepath):
            table_copy = pd.read_csv(self.table_filepath, sep=',')
            os.remove(self.table_filepath)

        gamertags = ['AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA']
        points = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
        answers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        fourth_values = ['?', '?', '?', '?', '?', '?', '?', '?', '?', '?']
        data = {'gamertag':gamertags,
                'points': points,
                'correct_answers': answers,
                'fourth_value': fourth_values}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(self.table_filepath, index = False)

        self.assertEqual(len(hiscore_df), 10)
        self.assertEqual(len(hiscore_df.columns), 4)

        hs.initialize_hiscore_dataframe()
        hiscore_df = pd.read_csv(self.table_filepath, sep=',')

        self.assertEqual(len(hiscore_df), 9)
        self.assertEqual(len(hiscore_df.columns), 3)

        try:
            table_copy.to_csv(self.table_filepath, index = False)
        except NameError:
            pass

    def test_zero_score_wont_qualify_for_empty_hiscores(self):
        if os.path.exists(self.table_filepath):
            table_copy = pd.read_csv(self.table_filepath, sep=',')
            os.remove(self.table_filepath)

        qualification = hs.points_qualify_for_hiscore(0)
        self.assertFalse(qualification)

        try:
            table_copy.to_csv(self.table_filepath, index = False)
        except NameError:
            pass

    def test_score_too_low_wont_qualify_for_hiscores(self):
        if os.path.exists(self.table_filepath):
            table_copy = pd.read_csv(self.table_filepath, sep=',')
            os.remove(self.table_filepath)

        data = {'gamertag':['AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA'],
                'points':[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],
                'correct_answers':[10, 10, 10, 10, 10, 10, 10, 10, 10]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(self.table_filepath, index = False)

        qualification = hs.points_qualify_for_hiscore(1000)
        qualification2 = hs.points_qualify_for_hiscore(5000)
        qualification3 = hs.points_qualify_for_hiscore(9999)
        self.assertFalse(qualification)
        self.assertFalse(qualification2)
        self.assertFalse(qualification3)

        qualification4 = hs.points_qualify_for_hiscore(10001)
        self.assertTrue(qualification4)

        try:
            table_copy.to_csv(self.table_filepath, index = False)
        except NameError:
            pass

    def test_score_too_low_not_added_to_hiscores(self):
        if os.path.exists(self.table_filepath):
            table_copy = pd.read_csv(self.table_filepath, sep=',')
            os.remove(self.table_filepath)

        new_player = Player('EVO')
        new_player.correct_answer()

        new_gamertag = new_player.get_gamertag()
        new_points = new_player.get_points()
        new_answers = new_player.get_correct_answers()

        data = {'gamertag':['AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA', 'AAA'],
                'points':[10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],
                'correct_answers':[10, 10, 10, 10, 10, 10, 10, 10, 10]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(self.table_filepath, index = False)

        hs.add_hiscore(new_gamertag, new_points, new_answers)

        for i in hiscore_df.index:
            row_gamertag = hiscore_df.at[i, 'gamertag']
            row_points = hiscore_df.at[i, 'points']
            row_answers = hiscore_df.at[i, 'correct_answers']
            self.assertNotEqual(row_gamertag, new_gamertag)
            self.assertNotEqual(row_points, new_points)
            self.assertNotEqual(row_answers, new_answers)

        try:
            table_copy.to_csv(self.table_filepath, index = False)
        except NameError:
            pass

    def test_new_score_replaces_only_the_worst_score(self):
        if os.path.exists(self.table_filepath):
            table_copy = pd.read_csv(self.table_filepath, sep=',')
            os.remove(self.table_filepath)

        data = {'gamertag':['EKA', 'TOK', 'KOL', 'NEL', 'VII', 'KUU', 'SEI', 'KAH', 'YHD'],
                'points':[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],
                'correct_answers':[1, 2, 3, 4, 5, 6, 7, 8, 9]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(self.table_filepath, index = False)
        print(len(hiscore_df))
        print(len(hiscore_df.columns))

        new_player = Player('AAA')
        for i in range(10):
            new_player.correct_answer()

        new_gamertag = new_player.get_gamertag()
        new_points = new_player.get_points()
        new_answers = new_player.get_correct_answers()
        print(new_gamertag)
        print(type(new_gamertag))
        print(new_points)
        print(type(new_points))
        print(new_answers)
        print(type(new_answers))

        hs.add_hiscore(new_gamertag, new_points, new_answers)
        hiscore_df = pd.read_csv(self.table_filepath, sep=',')

        for i in hiscore_df.index:
            row_gamertag = hiscore_df.at[i, 'gamertag']
            row_points = hiscore_df.at[i, 'points']
            row_answers = hiscore_df.at[i, 'correct_answers']

            self.assertNotEqual(row_gamertag, 'EKA')
            self.assertNotEqual(row_points, 1000)
            self.assertNotEqual(row_answers, 1)

        try:
            table_copy.to_csv(self.table_filepath, index = False)
        except NameError:
            pass
