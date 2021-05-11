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
                'correct':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'gens':[12,12,12,12,12,12,12,12,12]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(r'src/data/hiscores.csv', index = False)

    hiscore_df = pd.read_csv('src/data/hiscores.csv', sep=',')

    if (len(hiscore_df) != 9) or (len(hiscore_df.columns) != 4):

        data = {'gamertag':['NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN'],
                'points':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'correct':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'gens':[12,12,12,12,12,12,12,12,12]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(r'src/data/hiscores.csv', index = False)

    return hiscore_df

def points_qualify_for_hiscore(points):
    '''Checks whether user's points are high enough to be added to hiscores

        Args:
            User's current points (int)

        Returns:
            True: User has enough points for hiscores
            False: User does not have enough points for hiscores
        '''

    hiscore_df = initialize_hiscore_dataframe().sort_values(by=['points'])
    point_qualification = False

    for i in hiscore_df.index:
        row_points = hiscore_df.at[i, 'points']
        if points > row_points:
            point_qualification = True
    return point_qualification

def add_hiscore(player):
    '''Adds the given user score profile to hiscores

        Args:
            User's current player object

        Returns:
            None
        '''

    hiscore_df = initialize_hiscore_dataframe()
    hiscore_df = hiscore_df.sort_values(by=['points'])

    gamemode = player.get_gamemode()
    gamertag = player.get_gamertag()
    points = player.get_points()
    answers = player.get_correct_answers()

    number_of_gens = gamemode.get_number_of_generations()

    for i in hiscore_df.index:
        row_points = hiscore_df.at[i, 'points']
        if points > row_points:
            hiscore_df.at[i, 'gamertag'] = gamertag
            hiscore_df.at[i, 'points'] = points
            hiscore_df.at[i, 'correct'] = answers
            hiscore_df.at[i, 'gens'] = number_of_gens
            break

    hiscore_df.to_csv('src/data/hiscores.csv', index = False)
