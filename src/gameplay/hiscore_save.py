import pandas as pd

def initialize_hiscore_dataframe():

    try:
        hiscore_df = pd.read_csv('src/data/hiscores.csv', sep=',')
    except FileNotFoundError:
        data = {'gamertag':['NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN', 'NAN'],
                'points':[0, 0, 0, 0, 0, 0, 0, 0, 0],
                'correct_answers':[0, 0, 0, 0, 0, 0, 0, 0, 0]}
        hiscore_df = pd.DataFrame(data)
        hiscore_df.to_csv(r'src/data/hiscores.csv', index = False)
    return hiscore_df

def points_qualify_for_hiscore(points):

    hiscore_df = initialize_hiscore_dataframe().sort_values(by=['points'])
    point_qualification = False

    for i in hiscore_df.index:
        row_points = hiscore_df.at[i, 'points']
        if points > row_points:
            point_qualification = True
    return point_qualification

def add_hiscore(gamertag, points, correct_answers):
    initialize_hiscore_dataframe()
    hiscore_df = pd.read_csv('src/data/hiscores.csv', sep=',')
    hiscore_df = hiscore_df.sort_values(by=['points'])

    for i in hiscore_df.index:
        row_points = hiscore_df.at[i, 'points']

        if points > row_points:
            hiscore_df.at[i, 'gamertag'] = str(gamertag)
            hiscore_df.at[i, 'points'] = int(points)
            hiscore_df.at[i, 'correct_answers'] = int(correct_answers)
            break

    hiscore_df.to_csv(r'src/data/hiscores.csv', index = False)
