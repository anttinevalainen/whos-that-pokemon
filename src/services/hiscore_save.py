import pandas as pd
import services.hiscore_init as hi

def points_qualify_for_hiscore(points):
    '''Checks whether user's points are high enough to be added to hiscores

        Args:
            User's current points (int)

        Returns:
            True: User has enough points for hiscores
            False: User does not have enough points for hiscores
        '''

    hiscore_df = hi.initialize_hiscore_dataframe().sort_values(by=['points'])
    point_qualification = False

    for i in hiscore_df.index:
        row_points = hiscore_df.at[i, 'points']
        if points > row_points:
            point_qualification = True
    return point_qualification

def add_hiscore(player_score):
    '''Adds the given user score profile to hiscores

        Args:
            User's current player object

        Returns:
            None
        '''

    hiscore_df = hi.initialize_hiscore_dataframe()
    hiscore_df = hiscore_df.sort_values(by=['points'])
    gamemode = player_score.get_gamemode()

    gamertag = player_score.get_gamertag()
    points = player_score.get_points()
    answers = player_score.get_correct_answers()
    number_of_gens = gamemode.get_number_of_generations()

    for i in hiscore_df.index:
        row_points = hiscore_df.at[i, 'points']
        if points > row_points:
            hiscore_df.at[i, 'gamertag'] = gamertag
            hiscore_df.at[i, 'points'] = points
            hiscore_df.at[i, 'correct_answers'] = answers
            hiscore_df.at[i, 'gens'] = number_of_gens
            break

    hiscore_df.to_csv('src/services/hiscores.csv', index = False)
