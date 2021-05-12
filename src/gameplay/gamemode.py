import services.gamemode_service as gs

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
                genchoicelist: A list of twelve binaries (0-1).
                    1: generation with list index has been chosen
                    0: generation with list index has not been chosen

                revision: A boolean value depicting the use of revision mode.
                    True: The revision mode is ON
                    False: The revision mode is OFF
        '''

        self.genchoicelist = genchoicelist
        self.revision = revision

    def get_genchoice(self):
        '''Returns a list of user's generation choices made
        in the gamertag input page

        Args:
            self

        Returns:
            list object of 12 binaries (0-1)
        '''

        return self.genchoicelist

    def get_revision(self):
        '''Checks whether user has chosen to use the revision mode

        Args:
            self

        Returns:
            True: The revision mode is ON
            False: The revision mode is OFF
        '''

        return self.revision

    def get_number_of_generations(self):
        '''Returns an integer value of the amount of generations
        the user is playing with

        Args:
            self

        Returns:
            An integer value 1-12
        '''

        number_of_gens = 0

        for item in self.genchoicelist:

            if item == 1:
                number_of_gens += 1

        return number_of_gens


    def get_number_of_pokemon(self):
        '''Returns an integer value of the amount of Pokémon
        the user is playing with

        Args:
            self

        Returns:
            An integer value 18-1085
        '''

        number_of_pokemon = 0
        gen_number_list = []

        for i in range(0, 12):
            genlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            genlist[i] = 1

            dataframe = gs.create_pokedex_df(genlist)
            gen_number_list.append(len(dataframe))

        for position, item in enumerate(self.genchoicelist):

            if item == 1:
                gen_length = gen_number_list[position]
                number_of_pokemon += gen_length

        return number_of_pokemon


    def get_generations_string(self):
        '''Returns the user's generation choices as a string value

        Args:
            self

        Returns:
            a string with chosen generations
        '''

        gen_string = ''
        gen_number = 0
        gens = []
        specials = []
        other_gens = ['Mega', 'Giga', 'Alola', 'Galar']

        for position, item in enumerate(self.genchoicelist):
            if item == 1:
                gen_number += 1

                if position in range(0, 8):
                    gens.append(str(position+1))

                else:
                    specials.append(other_gens[position-8])

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
        return gen_string
