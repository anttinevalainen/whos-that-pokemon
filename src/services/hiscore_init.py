import pandas as pd

def initialize_hiscore_dataframe():

    '''Creates a new dataframe for hiscores, if one does not exist already

        Args:
            None

        Returns:
            None
        '''

    try:

        hiscore_df = pd.read_csv('src/data/hiscores.csv', sep=',')

    except FileNotFoundError:

        data = {'gamertag':['NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN'],
                'points':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'correct_answers':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'gens':[6,6,6,6,6,6,6,6,6]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(r'src/data/hiscores.csv', index = False)

    hiscore_df = pd.read_csv('src/data/hiscores.csv', sep=',')

    if (len(hiscore_df) != 9) or (len(hiscore_df.columns) != 4):

        data = {'gamertag':['NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN'],
                'points':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'correct_answers':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'gens':[6,6,6,6,6,6,6,6,6]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(r'src/data/hiscores.csv', index = False)

    return hiscore_df