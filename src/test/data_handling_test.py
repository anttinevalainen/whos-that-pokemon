import unittest
import os.path
import pandas as pd
import data.data_handling as dh

class TestDataHandling(unittest.TestCase):
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

        name = dh.get_pokemon_full_name(filename).split(' ')[0].lower()

        self.assertTrue(pokemon_by_number == name)

    def test_data_handling_gives_data_of_single_pokemon(self):
        random_pokemon_fp = dh.get_random_filename()
        random_silhouette_fp = dh.get_silhouette(random_pokemon_fp)
        pokemon_full_name = dh.get_pokemon_full_name(random_pokemon_fp)

        pokemon_name = pokemon_full_name.split(' ')[0].lower()
        pokemon_number = random_pokemon_fp[:-4].split('-')[0]
        silhouette_number = random_silhouette_fp[19:-4].split('-')[0]

        pokedex_df = pd.read_csv('src/data/pokedex_list.csv', sep = ',')

        for index, row in pokedex_df.iterrows():
            row_pokemon = pokedex_df.at[index, 'pokemon'].lower()
            if row_pokemon == pokemon_name:
                row_number = pokedex_df.at[index, 'pdno']
                self.assertTrue(
                    int(row_number) ==
                    int(pokemon_number) ==
                    int(silhouette_number)
                )
