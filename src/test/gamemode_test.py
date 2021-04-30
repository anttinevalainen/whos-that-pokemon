import unittest
import random as rd
from gameplay.gamemode import Gamemode

class TestGamemode(unittest.TestCase):
    def setUp(self):
        print('Gamemode test initiation')

    def test_genchoice_list_initializes_correctly(self):
        generation_choice = []
        generation_choice.append(1)

        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)

        rd.shuffle(generation_choice)
        new_gamemode = Gamemode(generation_choice, False)

        self.assertEqual(generation_choice,
                        new_gamemode.get_genchoice_list())

    def test_directory_dataframe_correct_size(self):
        generation_choice = []
        generation_choice.append(1)
        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)
        rd.shuffle(generation_choice)
        new_gamemode = Gamemode(generation_choice, False)

        gm_dataframe = new_gamemode.get_directory_dataframe()
        gm_pokemon, gm_special = new_gamemode.get_number_of_pokemon()
        gm_number_of_pokemon = gm_pokemon + gm_special
        print(generation_choice)
        print(len(gm_dataframe))
        print(gm_number_of_pokemon)
        self.assertEqual(len(gm_dataframe), gm_number_of_pokemon)

    def test_generations_string_returns_right_numbers(self):
        i = 0
        while i <= 6:
            generation_choice = []
            while len(generation_choice) < 6:
                random_number = rd.randint(0, 1)
                generation_choice.append(random_number)
            generation_choice.insert(i, 1)
            new_gamemode = Gamemode(generation_choice, False)

            gen_string = new_gamemode.get_generations_string()

            gen_number = 0
            gen_list = []
            value = ''

            for position, item in enumerate(generation_choice):
                if item == 1:
                    gen_number += 1
                    gen_list.append(str(position+1))

            if gen_number == 6:
                value = '1-6'
            else:
                value = ''

                for position, item in enumerate(gen_list):
                    if len(gen_list) < 2:
                        value += item
                    elif position < len(gen_list)-2:
                        value += item + ', '
                    elif position == len(gen_list)-2:
                        value += item + ' & '
                    else:
                        value += item
            i +=1
            self.assertEqual(gen_string, value)

    def test_number_of_gens_matches_with_gamemode(self):
        generation_choice = []
        generation_choice.append(1)
        while len(generation_choice) < 6:
            random_number = rd.randint(0, 1)
            generation_choice.append(random_number)
        rd.shuffle(generation_choice)
        new_gamemode = Gamemode(generation_choice, False)

        number_of_gens = new_gamemode.get_number_of_generations()
        gen_choice_gens = generation_choice.count(1)
        self.assertEqual(number_of_gens, gen_choice_gens)
