import unittest
import random as rd
from gameplay.gamemode import Gamemode
import services.gamemode_service as gs

class TestGamemode(unittest.TestCase):
    def setUp(self):
        print('Gamemode test initiation')

    def test_gamemode_initializes_correctly(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)
        count_from_list = genchoice.count(1)

        gamemode = Gamemode(genchoice, revision = False)
        gamemode2 = Gamemode(genchoice, revision = True)
        count_from_obj = gamemode.get_genchoice().count(1)
        self.assertEqual(count_from_list, count_from_obj)
        self.assertFalse(gamemode.get_revision())
        self.assertTrue(gamemode2.get_revision())

    def test_genchoice_list_initializes_correctly(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        self.assertEqual(genchoice,
                        gamemode.get_genchoice())

        gamemode = Gamemode(genchoice, True)
        self.assertEqual(genchoice,
                        gamemode.get_genchoice())

    def test_directory_dataframe_correct_size(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)

        pokedex_df = gs.create_pokedex_df(genchoice)
        pokemon_number = gamemode.get_number_of_pokemon()
        self.assertEqual(len(pokedex_df), pokemon_number)

    def test_generations_string_returns_right_numbers(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)

        gamemode = Gamemode(genchoice, False)
        gen_string_function_output = gamemode.get_generations_string()

        gen_string = ''
        gen_number = 0
        gens = []
        specials = []
        other_gens = ['Mega', 'Giga', 'Alola', 'Galar']

        for position, item in enumerate(genchoice):
            if item == 1:
                gen_number += 1
                if position in range(0,8):
                    gens.append(str(position+1))
                else:
                    specials.append(other_gens[position-8])

        if gen_number == 12:
            gen_string = '1-8\n +Mega, Giga, Alola & Galar'
        else:
            gens_value = ''
            if len(gens) == 8:
                gens_value = '1-8'
            elif gens:
                for position, item in enumerate(gens):
                    if position < len(gens)-2:
                        gens_value += item + ', '
                    elif position == len(gens)-2:
                        gens_value += item + ' & '
                    else:
                        gens_value += item

            specials_value = ''
            if len(specials) == 4:
                specials_value = 'Mega, Giga, Alola & Galar'
            elif specials:
                for position, item in enumerate(specials):
                    if position < len(specials)-2:
                        specials_value += item + ', '
                    elif position == len(specials)-2:
                        specials_value += item + ' & '
                    else:
                        specials_value += item

            if gens_value and specials_value:
                gen_string = gens_value + '\n +' + specials_value

            elif specials_value:
                gen_string = specials_value
            else:
                gen_string = gens_value

        self.assertEqual(gen_string, gen_string_function_output)

        genchoice = [1,1,1,1,1,1,1,1,0,0,0,0]
        gamemode = Gamemode(genchoice, False)
        gen_string_function_output = gamemode.get_generations_string()
        gen_string = '1-8'
        self.assertEqual(gen_string, gen_string_function_output)

        genchoice = [0,0,0,0,0,0,0,0,1,1,1,1]
        gamemode = Gamemode(genchoice, False)
        gen_string_function_output = gamemode.get_generations_string()
        gen_string = 'Mega, Giga, Alola & Galar'
        self.assertEqual(gen_string, gen_string_function_output)

        genchoice = [0,0,0,0,0,0,0,1,1,0,0,0]
        gamemode = Gamemode(genchoice, False)
        gen_string_function_output = gamemode.get_generations_string()
        gen_string = '8\n +Mega'
        self.assertEqual(gen_string, gen_string_function_output)

    def test_number_of_gens_matches_with_gamemode(self):
        genchoice = []
        genchoice.append(1)
        while len(genchoice) < 12:
            random_number = rd.randint(0, 1)
            genchoice.append(random_number)
        rd.shuffle(genchoice)
        gamemode = Gamemode(genchoice, False)

        number_of_gens = gamemode.get_number_of_generations()
        gen_choice_gens = genchoice.count(1)
        self.assertEqual(number_of_gens, gen_choice_gens)
