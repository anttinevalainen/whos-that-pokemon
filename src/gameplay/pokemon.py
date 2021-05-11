class Pokemon:
    '''A class that depicts a random pokemon that changes with each round

    Attributes:
        id: Unique id of the Pokemon in question
        pdno: Pokedex number (National) of the Pokemon in question
        name: Name of the Pokemon (Excluding special forms except mega,
                                    gigantamax and regional forms)
        secondary_name: Secondary evolution name of the Pokemon
        gen: Generation the Pokemon is introduced in (Mega, Gigantamax and
                                                    regionals have their own
                                                    listed generations)

    '''

    def __init__(self, pokemon_id, pdno, name, secondary_name, gen):
        '''Class constructor, chooses a new pokemon

            Args:
                pokedex:
                    pokemon_id: Unique id of the pokemon
                    pdno: National pokedex number
                    name: Primary name of the Pokemon
                    secondary_name: Secondary form name of the Pokemon
                    gen: The generation Pokemon is introduced in
        '''
        self.pokemon_id = pokemon_id
        self.pdno = pdno
        self.name = name
        self.secondary_name = secondary_name
        self.gen = gen

    def get_id(self):
        '''Returns the unique string ID of the pokemon in question

            Args:
                self

            Returns:
                String value of pokemon's unique ID'''
        return str(self.pokemon_id)

    def get_pdno(self):
        '''Returns the national pokedex number of the Pokemon in question

            Args:
                self

            Returns:
                integer value marking the pokedex number'''
        return self.pdno

    def get_picture_fp(self):
        '''Returns the filepath within the repository where pokemon's full-color
        image is found

            Args:
                self

            Returns:
                A string value describing the filepath to the png image'''
        filepath = 'src/data/png/' + self.pokemon_id + '.png'
        return filepath

    def get_silhouette_fp(self):
        '''Returns the filepath within the repository where pokemon's silhouette
        image is found

            Args:
                self

            Returns:
                A string value describing the filepath to the png image'''
        filepath = 'src/data/png/black_' + self.pokemon_id + '.png'
        return filepath

    def get_name(self):
        '''Returns the pokemon's simple name (The name used to match user's guess)

            Args:
                self

            Returns:
                A string value describing the simple name of the pokemon'''
        return self.name

    def get_secondary_name(self):
        '''Returns the pokemon's possible secondary name (The name to be
        attached when describing the answer correctness)

            Args:
                self

            Returns:
                A string value describing the secondary name of the pokemon.
                If pokemon doesn't have a secondary evolution/form name,
                the value is a single dash symbol: "-" '''
        return self.secondary_name

    def get_full_name(self):
        '''Returns the pokemon's simple name and full name combined and stylized

            Args:
                self

            Returns:
                A string value describing the full name of the pokemon in the form
                of "name (secondary name)" '''
        name = self.get_name()
        name2 = self.get_secondary_name()
        if name2 != '-':
            name += ' (' + name2 + ')'
        return name

    def get_gen(self):
        '''Returns the pokemon's generation. Possible generations are either 1-8
        or in the case of special evolutions: gen number+evolution marker,
        for example '1mega', '8giga', '1alola'

            Args:
                self

            Returns:
                A string value describing the generation of the pokemon'''
        return str(self.gen)
