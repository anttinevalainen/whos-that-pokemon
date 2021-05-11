import pandas as pd

def create_pokedex_df(genchoicelist):
    '''Returns a dataframe with only pokemon from the generations
    player has chosen in the gamertag input page

    Args:
        self

    Returns:
        a dataframe with pokemon of the generations user has chosen
    '''

    columns = ['id', 'pdno', 'name', 'secondary_name', 'gen']
    pokedex_df = pd.DataFrame(columns=columns)

    special_gens = ['mega', 'giga', 'alola', 'galar']

    filepath = 'src/data/pokedex.csv'
    full_pokedex = pd.read_csv(filepath, sep=',')

    for position, item in enumerate(genchoicelist):
        gen_pokedex = pd.DataFrame(columns=columns)

        if item == 1:
            gen = str(position + 1)

            if position in range(0, 8):
                gen_pokedex = full_pokedex[full_pokedex.gen == gen]

            else:
                gen_pokedex = full_pokedex[full_pokedex.gen.str.contains(
                    special_gens[position-8], case=False)]

        pokedex_df = pokedex_df.append(gen_pokedex, ignore_index=True)

    return pokedex_df
