class Pokemon:
    '''A class that depicts a random Pokémon that changes with each round

    Attributes:
        id: Unique id of the Pokémon in question
        pdno: Pokedex number (National) of the Pokémon in question
        name: Name of the Pokémon (Excluding special forms except mega,
                                    gigantamax and regional forms)
        secondary_name: Secondary evolution name of the Pokémon
        gen: Generation the Pokémon is introduced in (Mega, Gigantamax and
                                                    regionals have their own
                                                    listed generations)

    '''

    def __init__(self, pokemon_id, pdno, name, secondary_name, gen):
        '''Class constructor for a new random Pokémon

            Args:
                pokedex:
                    pokemon_id: Unique id of the Pokémon
                    pdno: National pokedex number
                    name: Primary name of the Pokémon
                    secondary_name: Secondary form name of the Pokémon
                    gen: The generation Pokémon is introduced in
        '''
        self.pokemon_id = pokemon_id
        self.pdno = pdno
        self.name = name
        self.secondary_name = secondary_name
        self.gen = gen

    def get_id(self):
        '''Returns the unique string ID of the Pokémon in question

            Args:
                self

            Returns:
                String value of Pokémon's unique ID'''
        return str(self.pokemon_id)

    def get_pdno(self):
        '''Returns the national pokedex number of the Pokémon in question

            Args:
                self

            Returns:
                integer value marking the pokedex number'''
        return self.pdno

    def get_picture_fp(self):
        '''Returns the filepath within the repository where Pokémon's full-color
        image is found

            Args:
                self

            Returns:
                A string value describing the filepath to the png image'''
        filepath = 'src/data/png/' + self.pokemon_id + '.png'
        return filepath

    def get_silhouette_fp(self):
        '''Returns the filepath within the repository where Pokémon's silhouette
        image is found

            Args:
                self

            Returns:
                A string value describing the filepath to the png image'''
        filepath = 'src/data/png/black_' + self.pokemon_id + '.png'
        return filepath

    def get_name(self):
        '''Returns the Pokémon's simple name (The name used to match user's guess)

            Args:
                self

            Returns:
                A string value describing the simple name of the Pokémon'''
        return self.name

    def set_name(self, new_name):
        '''Changes the Pokémon's simple name (This is used to match answers to Pokémon
        with same evolution forms between multiple Pokémon)

            Args:
                self

            Returns:
                A string value describing the simple name of the Pokémon'''
        self.name = new_name

    def get_secondary_name(self):
        '''Returns the Pokémon's possible secondary name (The name to be
        attached when describing the answer correctness)

            Args:
                self

            Returns:
                A string value describing the secondary name of the Pokémon.
                If Pokémon doesn't have a secondary evolution/form name,
                the value is a single dash symbol: "-" '''
        return self.secondary_name

    def get_full_name(self):
        '''Returns the Pokémon's simple name and full name combined and stylized

            Args:
                self

            Returns:
                A string value describing the full name of the Pokémon in the form
                of "name (secondary name)" '''
        name = self.get_name()
        name2 = self.get_secondary_name()
        if name2 != '-':
            name += ' (' + name2 + ')'
        return name

    def get_gen(self):
        '''Returns the Pokémon's generation. Possible generations are either 1-8
        or in the case of special evolutions: gen number+evolution marker,
        for example '1mega', '8giga', '1alola'

            Args:
                self

            Returns:
                A string value describing the generation of the Pokémon'''
        return str(self.gen)
