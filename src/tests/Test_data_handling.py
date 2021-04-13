import unittest
import data.data_handling as dh
import os.path
import pandas as pd

class Test_data_handling(unittest.TestCase):
    def setUp(self):
        print('setup')

    def test_randomizer_returns_existing_filename(self):
        filename = dh.get_random_filename()
        filepath = 'src/data/png/' + filename
        self.assertTrue(os.path.isfile(filepath))

    def test_get_silhouette_returns_existing_filename(self):
        filename = dh.get_random_filename()
        silhouette_filename = dh.get_silhouette(filename)
        self.assertTrue(os.path.isfile(silhouette_filename))

    def test_get_name_matches_with_pokemon_number(self):
        filename = dh.get_random_filename()
        pokedex_df = pd.read_csv('src/data/pokedex_list.csv', sep = ',')

        number = filename[:-4]
        number_s = number.split('-')
        number = number_s[0]
        pokemon_by_number = pokedex_df.at[int(number)-1, 'pokemon'].lower()

        name = dh.get_pokemon_name(filename).lower()
        self.assertTrue(pokemon_by_number == name)

