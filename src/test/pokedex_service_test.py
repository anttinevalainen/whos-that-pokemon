import unittest
import random as rd
import tkinter as tk

from gameplay.pokedex import Pokedex
import services.gamemode_service as gs
import services.pokemon_service as pks

class TestPokemonService(unittest.TestCase):
    def setUp(self):
        print('Pokedex service test initiation')

    def test_photoimage_functions_return_photoimages(self):

        tk.Tk()

        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)
        pokedex = Pokedex(gs.create_pokedex_df(genchoice))

        pokemon = pokedex.get_random_pokemon()
        pokemon_fp = pokemon.get_picture_fp()
        silhouette_fp = pokemon.get_silhouette_fp()

        pokemon_pi = pks.get_pokemon_photoimage(pokemon_fp)
        pokemon_type = type(pokemon_pi)

        silhouette_pi = pks.get_pokemon_photoimage(silhouette_fp)
        silhouette_type = type(silhouette_pi)

        self.assertEqual(str(pokemon_type), "<class 'PIL.ImageTk.PhotoImage'>")
        self.assertEqual(str(silhouette_type), "<class 'PIL.ImageTk.PhotoImage'>")
