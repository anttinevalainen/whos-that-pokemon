import unittest
import random as rd
import tkinter as tk

from gameplay.player import Player
from gameplay.gamemode import Gamemode
from gameplay.pokedex import Pokedex
from gameplay.pokemon import Pokemon
import services.player_service as ps
import services.gamemode_service as gs

class TestPlayerService(unittest.TestCase):
    def setUp(self):
        print('Data handling test initiation')

    def test_check_answer_correct_answer(self):

        normal_pokemon = Pokemon('152',152,'Chikorita','-','2')
        normal_true = 'chikorita'
        correct, text = ps.check_answer(normal_pokemon, normal_true)
        self.assertTrue(correct)
        self.assertEqual(text, "Correct! It's\nCHIKORITA!")

        mega_pokemon = Pokemon('3mega',3,'Mega Venusaur','-','1mega')
        mega_true = 'mega venusaur'
        correct, text = ps.check_answer(mega_pokemon, mega_true)
        self.assertTrue(correct)
        self.assertEqual(text, "Correct! It's\nMEGA VENUSAUR!")

        mega2_pokemon = Pokemon('150mega-y',150,'Mega Mewtwo','y','1mega')
        mega2_true = 'mega mewtwo'
        correct, text = ps.check_answer(mega2_pokemon, mega2_true)
        self.assertTrue(correct)
        self.assertEqual(text, "Correct! It's\nMEGA MEWTWO (Y)!")

        normal2_pokemon = Pokemon('720-unbound',720,'Hoopa','Unbound','6')
        normal2_true = 'hoopa'
        correct, text = ps.check_answer(normal2_pokemon, normal2_true)
        self.assertTrue(correct)
        self.assertEqual(text, "Correct! It's\nHOOPA (UNBOUND)!")

        giga_pokemon = Pokemon('892giga-single_strike', 892,
                               'Gigantamax Urshifu', 'single strike',
                               '8giga')
        giga_true = 'gigantamax urshifu'
        correct, text = ps.check_answer(giga_pokemon, giga_true)
        self.assertTrue(correct)
        self.assertEqual(text, "Correct! It's\nGIGANTAMAX URSHIFU\n(SINGLE STRIKE)!")

    def test_check_answer_incorrect_answer(self):
        genchoice = [1,1,1,1,1,1,1,1,1,1,1,1]
        pokedex = Pokedex(gs.create_pokedex_df(genchoice))

        pokemon = pokedex.get_random_pokemon()
        wrong_answer = 'angemon'
        correct, text = ps.check_answer(pokemon, wrong_answer)
        self.assertFalse(correct)
        self.assertFalse('Correct!' in text)

        mega_pokemon = Pokemon('3mega',3,'Mega Venusaur','-','1mega')
        mega_false = 'venusaur'
        correct, text = ps.check_answer(mega_pokemon, mega_false)
        self.assertFalse(correct)
        self.assertFalse('Correct!' in text)

        mega2_pokemon = Pokemon('150mega-y',150,'Mega Mewtwo','y','1mega')
        mega2_false = 'mega mewtwo from pokemon y game'
        correct, text = ps.check_answer(mega2_pokemon, mega2_false)
        self.assertFalse(correct)
        self.assertFalse('Correct!' in text)

        normal2_pokemon = Pokemon('720-unbound',720,'Hoopa','Unbound','6')
        normal2_false = 'unbound hoopa'
        correct, text = ps.check_answer(normal2_pokemon, normal2_false)
        self.assertFalse(correct)
        self.assertFalse('Correct!' in text)

        giga_pokemon = Pokemon('892giga-rapid_strike', 892,
                               'Gigantamax Urshifu', 'rapid strike',
                               '8giga')
        giga_false = 'urshifu'
        correct, text = ps.check_answer(giga_pokemon, giga_false)
        self.assertFalse(correct)
        self.assertFalse('Correct!' in text)

    def test_check_answer_ignores_accents(self):
        genchoice = [1,1,1,1,1,1,1,1,1,1,1,1]
        pokedex = Pokedex(gs.create_pokedex_df(genchoice))

        pokemon = pokedex.get_random_pokemon()

        pokemon_name = pokemon.get_name()
        player_guess = pokemon.get_name().replace('a', 'á')
        player_guess = player_guess.replace('e', 'é')
        player_guess = player_guess.replace('i', 'í')
        player_guess = player_guess.replace('o', 'ó')
        player_guess = player_guess.replace('u', 'ú')
        player_guess = player_guess.replace('y', 'ý')

        correct, text = ps.check_answer(pokemon, player_guess)

        self.assertTrue(correct)
        self.assertTrue('Correct!' in text)
        self.assertNotEqual(player_guess, pokemon_name)

    def test_correct_answer_raises_points_and_answers(self):
        genchoice = []
        genchoice.append(1)

        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        pokedex = Pokedex(gs.create_pokedex_df(genchoice))
        player = Player('TTT', gamemode, pokedex)

        pokemon = pokedex.get_random_pokemon()
        ps.correct_answer(player, pokemon)
        pokemon = pokedex.get_random_pokemon()
        ps.correct_answer(player, pokemon)
        pokemon = pokedex.get_random_pokemon()
        ps.correct_answer(player, pokemon)

        gamemode = player.get_gamemode()
        number_of_gens = gamemode.get_number_of_generations()
        first_round_points = number_of_gens*50*3

        points1 = player.get_points()
        answers = player.get_correct_answers()
        self.assertEqual(points1, first_round_points)
        self.assertEqual(answers, 3)

        pokemon = pokedex.get_random_pokemon()
        ps.correct_answer(player, pokemon)
        pokemon = pokedex.get_random_pokemon()
        ps.correct_answer(player, pokemon)

        second_round_points = number_of_gens*50*2

        points2 = player.get_points()
        answers = player.get_correct_answers()
        self.assertTrue(points2 > points1)
        self.assertEqual(points2, first_round_points + second_round_points)
        self.assertEqual(answers, 5)

    def test_incorrect_answer_lowers_health(self):
        genchoice = []
        genchoice.append(1)

        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        pokedex = Pokedex(gs.create_pokedex_df(genchoice))
        player = Player('TTT', gamemode, pokedex)

        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)

        health = player.get_health()
        self.assertTrue(health == 2)

        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)

        health = player.get_health()
        self.assertTrue(health == 0)

    def test_incorrect_wont_make_health_negative(self):
        genchoice = []
        genchoice.append(1)

        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        pokedex = Pokedex(gs.create_pokedex_df(genchoice))
        player = Player('TTT', gamemode, pokedex)

        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)

        health = player.get_health()
        self.assertTrue(health == 0)

    def test_gamemode_gives_correct_points(self):
        genchoice = [1,1,1,1,1,1,1,1,1,1,1,1]
        for i in range(0,11):
            genchoice[i] = 0
            gamemode = Gamemode(genchoice, False)
            pokedex = Pokedex(gs.create_pokedex_df(genchoice))
            player = Player('TTT', gamemode, pokedex)
            point_multiplier = genchoice.count(1)

            pokemon = pokedex.get_random_pokemon()
            ps.correct_answer(player, pokemon)
            pokemon = pokedex.get_random_pokemon()
            ps.correct_answer(player, pokemon)
            pokemon = pokedex.get_random_pokemon()
            ps.correct_answer(player, pokemon)
            pokemon = pokedex.get_random_pokemon()
            ps.correct_answer(player, pokemon)

            points_should_be = point_multiplier * 50 * 4
            points_are = player.get_points()
            self.assertEqual(points_should_be, points_are)

    def test_photoimage_function_returns_photoimage(self):
        tk.Tk()

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

        three_heart_pi = ps.get_health_photoimage(player)
        three_heart_type = type(three_heart_pi)

        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        two_heart_pi = ps.get_health_photoimage(player)
        two_heart_type = type(two_heart_pi)

        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        one_heart_pi = ps.get_health_photoimage(player)
        one_heart_type = type(one_heart_pi)

        pokemon = pokedex.get_random_pokemon()
        ps.incorrect_answer(player, pokemon)
        zero_heart_pi = ps.get_health_photoimage(player)
        zero_heart_type = type(zero_heart_pi)

        self.assertEqual(str(three_heart_type), "<class 'PIL.ImageTk.PhotoImage'>")
        self.assertEqual(str(two_heart_type), "<class 'PIL.ImageTk.PhotoImage'>")
        self.assertEqual(str(one_heart_type), "<class 'PIL.ImageTk.PhotoImage'>")
        self.assertEqual(str(zero_heart_type), "<class 'PIL.ImageTk.PhotoImage'>")
