import random as rd
from gameplay.pokemon import Pokemon

class Pokedex:
    '''A class that depicts a pokedex filled with pokemon user has to guess

    Attributes:
        gamemode: Dataframe of user's pokemon

    '''

    def __init__(self, pokedex_df):
        '''Class constructor, chooses a new pokemon

            Args:
                pokedex: A dataframe created by gamemode class. Includes the
                generations of Pokemon the user is playing with.
        '''

        self.pokedex_df = pokedex_df

    def get_pokedex_df(self):
        '''Returns the dataframe of all the Pokemon left in the pokedex

            Args:
                self

            Returns:
                Dataframe from curent pokedex object'''

        return self.pokedex_df

    def is_empty(self):
        '''Check whether the pokedex played with has any rows left

            Args:
                self

            Returns:
                True: Pokedex is empty
                False: Pokedex is not empty'''

        return self.pokedex_df.empty

    def erase_pokemon(self, pokemon):
        '''Erases a row with pokemon data set to the function when called

            Args:
                self
                pokemon: pokemon object to be removed

            Returns:
                None'''

        id_erase = pokemon.get_id()
        self.pokedex_df = self.pokedex_df[self.pokedex_df.id != id_erase]
        self.pokedex_df = self.pokedex_df.reset_index(drop=True)

    def get_random_pokemon(self):
        '''Returns a random pokemon from the current pokedex

            Args:
                self

            Returns:
                pokemon object picked at random from pokedex dataframe'''

        random_int = rd.randint(0, len(self.pokedex_df)-1)
        random_row = self.pokedex_df.loc[random_int, : ]

        pokemon_id = random_row['id']
        pdno = random_row['pdno']
        name = random_row['name']
        name2 = random_row['secondary_name']
        gen = random_row['gen']

        pokemon = Pokemon(pokemon_id,pdno,name,name2,gen)
        return pokemon
