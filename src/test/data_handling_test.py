import unittest
import os.path
import tkinter as tk
import pandas as pd
import data.data_handling as dh
from gameplay.player_score import Player
from gameplay.gamemode import Gamemode

class TestDataHandling(unittest.TestCase):
    def setUp(self):
        print('Data handling test initiation')

    def test_randomizer_returns_existing_filename(self):
        generation_choice = [1,0,1,0,1,0]
        new_gamemode = Gamemode(generation_choice, False)
        filename = dh.get_random_filename(new_gamemode)
        filepath = 'src/data/png/' + filename
        self.assertTrue(os.path.isfile(filepath))

    def test_get_silhouette_returns_existing_filename(self):
        generation_choice = [1,0,0,0,1,0]
        new_gamemode = Gamemode(generation_choice, False)
        filename = dh.get_random_filename(new_gamemode)
        silhouette_filename = dh.get_silhouette(filename)
        self.assertTrue(os.path.isfile(silhouette_filename))

    def test_get_name_matches_with_pokemon_number(self):
        generation_choice = [1,1,1,0,1,0]
        new_gamemode = Gamemode(generation_choice, False)
        filename = dh.get_random_filename(new_gamemode)
        pokedex_df = pd.read_csv('src/data/pokedex_list.csv', sep = ',')

        number = filename[:-4]
        number_s = number.split('-')
        number = number_s[0]
        pokemon_by_number = pokedex_df.at[int(number)-1, 'pokemon'].lower()

        name = dh.get_pokemon_full_name(filename).lower()
        print(pokemon_by_number)
        print(name)

        self.assertTrue(pokemon_by_number in name)

    def test_get_name_returns_multipart_name(self):
        megaevol_fp = '3-mega.png'
        correct_full_name = 'mega venusaur'
        full_name = dh.get_pokemon_full_name(megaevol_fp).lower()
        self.assertEqual(correct_full_name, full_name)

        megaevol_fp = '150-mega_y.png'
        correct_full_name = 'mega mewtwo (y)'
        full_name = dh.get_pokemon_full_name(megaevol_fp).lower()
        self.assertEqual(correct_full_name, full_name)

        special_fp = '720-unbound.png'
        correct_full_name = 'hoopa (unbound)'
        full_name = dh.get_pokemon_full_name(special_fp).lower()
        self.assertEqual(correct_full_name, full_name)

    def test_data_handling_gives_data_of_single_pokemon(self):
        generation_choice = [1,0,1,0,1,1]
        new_gamemode = Gamemode(generation_choice, False)
        random_pokemon_fp = dh.get_random_filename(new_gamemode)
        random_silhouette_fp = dh.get_silhouette(random_pokemon_fp)
        pokemon_full_name = dh.get_pokemon_full_name(random_pokemon_fp)

        pokemon_name = pokemon_full_name.split(' ')[0].lower()
        pokemon_number = random_pokemon_fp[:-4].split('-')[0]
        silhouette_number = random_silhouette_fp[19:-4].split('-')[0]

        pokedex_df = pd.read_csv('src/data/pokedex_list.csv', sep = ',')

        for index in pokedex_df.index:
            row_pokemon = pokedex_df.at[index, 'pokemon'].lower()
            if row_pokemon == pokemon_name:
                row_pdno = pokedex_df.at[index, 'pdno']
                self.assertTrue(
                    int(row_pdno) ==
                    int(pokemon_number) ==
                    int(silhouette_number)
                )

    def test_check_answer_correct_answer(self):
        normal_fp = '152.png'
        correct_name = dh.get_pokemon_full_name(normal_fp).lower()
        normal_true = 'chikorita'
        self.assertTrue(dh.check_answer(correct_name, normal_true))

        megaevol_fp = '3-mega.png'
        megaevol_name = dh.get_pokemon_full_name(megaevol_fp).lower()
        megaevol_true = 'mega venusaur'
        self.assertTrue(dh.check_answer(megaevol_name, megaevol_true))

        megaevol_fp = '150-mega_y.png'
        megaevol_name = dh.get_pokemon_full_name(megaevol_fp).lower()
        megaevol_true = 'mega mewtwo'
        self.assertTrue(dh.check_answer(megaevol_name, megaevol_true))

        special_fp = '720-unbound.png'
        correct_name = dh.get_pokemon_full_name(special_fp).lower()
        special_true = 'hoopa'
        self.assertTrue(dh.check_answer(correct_name, special_true))

    def test_check_answer_incorrect_answer(self):
        new_gamemode = Gamemode([0,0,0,1,0,1], False)
        random_pokemon_fp = dh.get_random_filename(new_gamemode)
        pokemon_full_name = dh.get_pokemon_full_name(random_pokemon_fp)
        wrong_answer = 'angemon'
        self.assertFalse(dh.check_answer(pokemon_full_name, wrong_answer))

        megaevol_fp = '3-mega.png'
        megaevol_name = dh.get_pokemon_full_name(megaevol_fp).lower()
        megaevol_wrong = 'venusaur'
        self.assertFalse(dh.check_answer(megaevol_name, megaevol_wrong))

        megaevol_fp = '150-mega_y.png'
        megaevol_name = dh.get_pokemon_full_name(megaevol_fp).lower()
        megaevol_wrong = 'mega mewtwo from pokemon y game'
        self.assertFalse(dh.check_answer(megaevol_name, megaevol_wrong))

        special_fp = '720-unbound.png'
        correct_name = dh.get_pokemon_full_name(special_fp).lower()
        wrong_name = 'unbound hoopa'
        self.assertFalse(dh.check_answer(correct_name, wrong_name))

    def test_photoimage_functions_return_photoimages(self):
        tk.Tk()

        generation_choice = [1,0,0,0,0,0]
        new_gamemode = Gamemode(generation_choice, False)
        new_player = Player('AAA', new_gamemode)

        three_heart_pi = dh.get_health_photoimage(new_player)
        three_heart_type = type(three_heart_pi)

        new_player.incorrect_answer()
        two_heart_pi = dh.get_health_photoimage(new_player)
        two_heart_type = type(two_heart_pi)

        new_player.incorrect_answer()
        one_heart_pi = dh.get_health_photoimage(new_player)
        one_heart_type = type(one_heart_pi)

        new_player.incorrect_answer()
        zero_heart_pi = dh.get_health_photoimage(new_player)
        zero_heart_type = type(zero_heart_pi)

        pokemon_fp = dh.get_random_filename(new_player.get_gamemode())
        pokemon_pi = dh.get_pokemon_photoimage(pokemon_fp)
        pokemon_type = type(pokemon_pi)

        silhouette_fp = dh.get_silhouette(pokemon_fp)
        silhouette_pi = dh.get_pokemon_photoimage(silhouette_fp)
        silhouette_type = type(silhouette_pi)

        self.assertTrue(three_heart_type ==
                        two_heart_type ==
                        one_heart_type ==
                        zero_heart_type ==
                        pokemon_type ==
                        silhouette_type)

    def test_random_filepath_matches_with_gamemode(self):
        gamemode1 = Gamemode([1,1,1,1,1,1], False)
        gamemode2 = Gamemode([1,0,0,0,0,0], False)
        gamemode3 = Gamemode([1,0,0,1,0,1], False)

        number1 = int(dh.get_random_filename(gamemode1)[:-4].split('-')[0])
        number2 = int(dh.get_random_filename(gamemode2)[:-4].split('-')[0])
        number3 = int(dh.get_random_filename(gamemode3)[:-4].split('-')[0])

        self.assertGreaterEqual(number1, 1)
        self.assertLessEqual(number1, 721)

        self.assertGreaterEqual(number2, 1)
        self.assertLessEqual(number2, 151)

        self.assertTrue((number3 >= 1 and number3 <= 151) or
                        (number3 >= 387 and number3 <= 493) or
                        (number3 >= 650 and number3 <= 721))

    def test_mrmime_mimejr_and_porygonz(self):
        mrmime_fp = '122.png'
        mimejr_fp = '439.png'
        porygonz_fp = '474.png'

        porygonz_full_name = dh.get_pokemon_full_name(porygonz_fp).lower()
        mrmime_full_name = dh.get_pokemon_full_name(mrmime_fp).lower()
        mimejr_full_name = dh.get_pokemon_full_name(mimejr_fp).lower()

        self.assertEqual(porygonz_full_name, 'porygon-z')
        self.assertEqual(mrmime_full_name, 'mr. mime')
        self.assertEqual(mimejr_full_name, 'mime jr.')

        self.assertTrue(dh.check_answer(mrmime_full_name, 'mr mime'))
        self.assertTrue(dh.check_answer(mimejr_full_name, 'mime jr'))
        self.assertTrue(dh.check_answer(porygonz_full_name, 'porygon z'))
