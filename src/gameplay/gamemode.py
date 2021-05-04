import pandas as pd

class Gamemode:
    '''A class that depicts user's gamemode based on the choices
        made in gamertag input page of UI
    Attributes:
        genchoicelist: A list object of user's generation choices
        revision: User's choice of playing with or without the revision mode
    '''

    def __init__(self, genchoicelist, revision):
        '''Class constructor, creates a new gamemode

            Args:
                genchoicelist: A list of six binaries (0-1).
                1: generation with list index has been chosen
                0: generation with list index has not been chosen

                revision: A boolean value depicting the use of revision mode.
                True: The revision mode is ON
                False: The revision mode is OFF
        '''

        self.genchoicelist = genchoicelist
        self.revision = revision

    def get_genchoice_list(self):
        '''Returns a list of user's generation choices made
        in the gamertag input page

        Args:
            self

        Returns:
            list object of 6 values (0-1)
        '''

        return self.genchoicelist

    def get_directory_dataframe(self):
        '''Returns a dataframe with only pokemon from the generations
        player has chosen in the gamertag input page

        Args:
            self

        Returns:
            a dataframe with pokemon from gen 1-6
        '''

        directory_df = pd.read_csv('src/data/directory_list.csv', sep = ',')
        gen_one_dir = pd.DataFrame()
        gen_two_dir = pd.DataFrame()
        gen_three_dir = pd.DataFrame()
        gen_four_dir = pd.DataFrame()
        gen_five_dir = pd.DataFrame()
        gen_six_dir = pd.DataFrame()

        for position, item in enumerate(self.genchoicelist):
            if position == 0 and item == 1:
                gen_one_dir = directory_df[0:171]
            elif position == 1 and item == 1:
                gen_two_dir = directory_df[171:277]
            elif position == 2 and item == 1:
                gen_three_dir = directory_df[277:437]
            elif position == 3 and item == 1:
                gen_four_dir = directory_df[437:563]
            elif position == 4 and item == 1:
                gen_five_dir = directory_df[563:737]
            elif position == 5 and item == 1:
                gen_six_dir = directory_df[737:818]

        gamemode_directory = pd.concat([gen_one_dir, gen_two_dir,
                            gen_three_dir, gen_four_dir,
                            gen_five_dir, gen_six_dir],
                            ignore_index=True
                            )

        return gamemode_directory

    def get_generations_string(self):
        '''Returns the user's generation choices as a string value

        Args:
            self

        Returns:
            a sting with chosen generations
        '''

        gen_number = 0
        gen_list = []

        for position, item in enumerate(self.genchoicelist):
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
        return value

    def get_number_of_pokemon(self):
        '''Returns a integer value of the number of normal and special
        pokemon player has chosen to use the app with

        Args:
            self

        Returns:
            Two string values depicting the number of normal and special pokemon
            the app is played with
        '''

        number_of_pokemon = 721
        number_of_special = 97
        for position, item in enumerate(self.genchoicelist):
            if position == 0 and item == 0:
                number_of_pokemon -= 151
                number_of_special -= 20
            elif position == 1 and item == 0:
                number_of_pokemon -= 100
                number_of_special -= 6
            elif position == 2 and item == 0:
                number_of_pokemon -= 135
                number_of_special -= 25
            elif position == 3 and item == 0:
                number_of_pokemon -= 107
                number_of_special -= 19
            elif position == 4 and item == 0:
                number_of_pokemon -= 156
                number_of_special -= 18
            elif position == 5 and item == 0:
                number_of_pokemon -= 72
                number_of_special -= 9

        return number_of_pokemon, number_of_special

    def get_number_of_generations(self):
        '''Returns a integer value of the amount of generations
        the user is playing with

        Args:
            self

        Returns:
            a integer value 1-6
        '''

        number_of_gens = 0
        for position, item in enumerate(self.genchoicelist):
            if position == 0 and item == 1:
                number_of_gens += 1
            elif position == 1 and item == 1:
                number_of_gens += 1
            elif position == 2 and item == 1:
                number_of_gens += 1
            elif position == 3 and item == 1:
                number_of_gens += 1
            elif position == 4 and item == 1:
                number_of_gens += 1
            elif position == 5 and item == 1:
                number_of_gens += 1
        return number_of_gens

    def get_revision(self):
        '''Checks whether user has chosen to use the revision mode

        Args:
            self

        Returns:
            True: The revision mode is ON
            False: The revision mode is OFF
        '''

        return self.revision
