import unittest
import os.path
import random as rd

from gameplay.player import Player
from gameplay.gamemode import Gamemode
from gameplay.pokedex import Pokedex
from gameplay.pokemon import Pokemon
import services.gamemode_service as gs
import services.player_service as ps

class TestPokemon(unittest.TestCase):
    def setUp(self):
        print('Pokemon test initiation')

    def test_pokemon_initializes_correctly(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        pokedex_df = gs.create_pokedex_df(genchoice)
        pokedex = Pokedex(pokedex_df)
        pokemon = pokedex.get_random_pokemon()

        pokemon_id = pokemon.get_id()
        pokemon_pdno = pokemon.get_pdno()
        pokemon_name = pokemon.get_name()
        pokemon_name2 = pokemon.get_secondary_name()
        pokemon_gen = pokemon.get_gen()

        pokedex_df = pokedex_df[pokedex_df.id == pokemon_id]
        for index, row in pokedex_df.iterrows():

            self.assertEqual(pokemon_id, row['id'])
            self.assertEqual(pokemon_pdno, row['pdno'])
            self.assertEqual(pokemon_name, row['name'])
            self.assertEqual(pokemon_name2, row['secondary_name'])
            self.assertEqual(pokemon_gen, row['gen'])

    def test_randomizer_returns_existing_pokemon(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        pokedex_df = gs.create_pokedex_df(genchoice)
        pokedex = Pokedex(pokedex_df)
        pokemon = pokedex.get_random_pokemon()

        namelist = pokedex_df['name'].tolist()
        name_found = False
        pokemon_name = pokemon.get_name()
        for value in namelist:
            if value.lower() == pokemon_name.lower():
                name_found = True

        self.assertTrue(name_found)

    def test_randomizer_returns_existing_filename(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        pokedex_df = gs.create_pokedex_df(genchoice)
        pokedex = Pokedex(pokedex_df)
        pokemon = pokedex.get_random_pokemon()

        filepath = 'src/data/png/' + str(pokemon.get_id()) + '.png'
        pokemon_fp = pokemon.get_picture_fp()
        silhouette_fp = pokemon.get_silhouette_fp()

        self.assertTrue(os.path.isfile(filepath))
        self.assertTrue(os.path.isfile(pokemon_fp))
        self.assertTrue(os.path.isfile(silhouette_fp))

    def test_randomized_pokemon_erased_after_answers(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        pokedex_df = gs.create_pokedex_df(genchoice)
        start_length = len(pokedex_df)
        pokedex = Pokedex(pokedex_df)
        player = Player('TTT', gamemode, pokedex)

        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        pokedex = player.get_pokedex()
        pokedex_df = pokedex.get_pokedex_df()
        pokemon_id = str(pokemon.get_id())
        idlist = pokedex_df['id'].tolist()
        id_found = False
        for value in idlist:
            if str(value).lower() == pokemon_id.lower():
                id_found = True
        self.assertFalse(id_found)

        pokemon = pokedex.get_random_pokemon()
        ps.correct_answer(player, pokemon)
        pokedex = player.get_pokedex()
        pokedex_df = pokedex.get_pokedex_df()

        pokemon_id = str(pokemon.get_id())
        idlist = pokedex_df['id'].tolist()
        id_found = False
        for value in idlist:
            if str(value).lower() == pokemon_id.lower():
                id_found = True
        self.assertFalse(id_found)

        self.assertNotEqual(start_length, len(pokedex_df))
        self.assertEqual(start_length - 2, len(pokedex_df))

    def test_pokedex_dataframe_empties(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        pokedex_df = gs.create_pokedex_df(genchoice)
        pokedex = Pokedex(pokedex_df)
        player = Player('TTT', gamemode, pokedex)
        for i in range(0,len(pokedex_df)):
            pokemon = pokedex.get_random_pokemon()
            ps.incorrect_answer(player, pokemon)
        pokedex = player.get_pokedex()
        self.assertTrue(pokedex.is_empty())

    def test_set_name_changes_pokemon_name(self):
        pokemon = Pokemon('169',169,'Crobat','-','2')
        ex_name = pokemon.get_name()
        pokemon.set_name('Patamon')
        new_name = pokemon.get_name()
        self.assertNotEqual(ex_name, new_name)
        self.assertNotEqual(new_name, 'Crobat')
        self.assertEqual(new_name, 'Patamon')
