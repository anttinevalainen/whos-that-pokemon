import random
import pandas as pd
from PIL import Image, ImageTk

def get_random_filename(gamemode):
    '''Returns a png-filename by random from data/png folder

        Args:
            gamemode: gamemode object, with which the player is using the app

        Returns:
            png-filename as string
        '''

    directory_df = gamemode.get_directory_dataframe()
    random_integer = random.randint(0,len(directory_df)-1)
    filename = directory_df.at[random_integer, 'file']

    return filename

def get_silhouette(filename):
    '''Returns a silhouette version of a given png file

        Args:
            filename: name of a png-file from data/png folder

        Returns:
            png-filename as string
        '''

    silhouette_filepath = 'src/data/png/black_' + filename
    return silhouette_filepath

def get_pokemon_full_name(filename):
    '''Returns the name and the type of possible secondary
    form of pokemon with given filename

        Args:
            filename: name of a png-file from data/png folder

        Returns:
            full name of a pokemon in the following form:
            (mega) + name + (possible special form)
        '''

    pokedex_df = pd.read_csv('src/data/pokedex_list.csv', sep = ',')
    filename = filename[:-4]
    secondary_name = ''
    if filename == '474':
        filenumber = int(filename)-1
        pokemon_full_name = pokedex_df.at[filenumber, 'pokemon']
    else:
        filename_s = filename.split('-')
        filenumber = int(filename_s[0])-1

        if len(filename_s) > 1:
            base_name = pokedex_df.at[filenumber, 'pokemon'].capitalize()
            if 'mega' in filename_s[1]:
                base_name = 'Mega ' + base_name
            secondary_name = filename_s[1].replace('mega', '')
            secondary_name = secondary_name.replace('_', ' ')
            secondary_name = secondary_name.strip()

            if secondary_name != '':
                pokemon_full_name = base_name + ' (' + secondary_name + ')'
            else:
                pokemon_full_name = base_name
        else:
            pokemon_full_name = pokedex_df.at[filenumber, 'pokemon'].capitalize()

    return pokemon_full_name

def get_pokemon_photoimage(filename):
    '''returns a ready made photoimage of the pokemon picture merged with
        the background of the app. Can be used with either silhouette or
        pokemon image filepaths

        Args:
            filename: name of a png-file of the pokemon or its silhouette
            from data/png folder

        Returns:
            photoimage object of the image merged with same size piece of app
            background
        '''

    if 'black_' in filename:
        img = Image.open(filename).convert('RGBA')
    else:
        img = Image.open('src/data/png/' + filename).convert('RGBA')

    image_background = Image.open('src/data/png/image_background.png').convert('RGBA')
    image_background.paste(img, (0, 0), img)
    pokemon_photoimage = ImageTk.PhotoImage(image_background)
    return pokemon_photoimage

def check_answer(pokemon_full_name, answer):
    '''Returns a a boolean value of answer correctness.

        Args:
            pokemon_full_name: String value of Pokamon name,
            can be used with special forms and mega/gigantamax evolutions!
            answer: User input from play page

        Returns:
            True: If answer matches with pokemon name
            False: If answer does not match with pokemon name
    '''

    correct = False

    correct_answer = ''
    user_answer = ''

    pokemon_full_name = pokemon_full_name.lower()
    name_split = pokemon_full_name.split(' ')

    answer = answer.lower()

    if name_split[0] == 'mega':
        pokemon_name = name_split[0] + ' ' + name_split[1]
    elif (pokemon_full_name == 'mr. mime' or
        pokemon_full_name == 'mime jr.'):
        pokemon_name = pokemon_full_name
    else:
        pokemon_name = name_split[0]

    for character in pokemon_name:
        if character.isalnum():
            correct_answer += character

    for character in answer:
        if character.isalnum():
            user_answer += character

    if correct_answer == user_answer:
        correct = True

    return correct

def get_health_photoimage(player_score):
    '''returns a photoimage of player's health merged with
    the background.

        Args:
            Player_score: The current Player object

        Returns:
            Photoimage object of user's health as three heart
            symbols merged with a piece of app background
    '''


    heart_fp = 'src/data/png/heart.png'
    noheart_fp = 'src/data/png/noheart.png'
    background_fp = 'src/data/png/health_background.png'

    heart = Image.open(heart_fp).convert('RGBA')
    noheart = Image.open(noheart_fp).convert('RGBA')
    health = Image.open(background_fp).convert('RGBA')

    if player_score.get_health() == 3:
        health.paste(heart, (0, 0), heart)
        health.paste(heart, (74, 0), heart)
        health.paste(heart, (148, 0), heart)
    elif player_score.get_health() == 2:
        health.paste(heart, (0, 0), heart)
        health.paste(heart, (74, 0), heart)
        health.paste(noheart, (148, 0), noheart)
    elif player_score.get_health() == 1:
        health.paste(heart, (0, 0), heart)
        health.paste(noheart, (74, 0), noheart)
        health.paste(noheart, (148, 0), noheart)
    else:
        health.paste(noheart, (0, 0), noheart)
        health.paste(noheart, (74, 0), noheart)
        health.paste(noheart, (148, 0), noheart)

    health_photoimage = ImageTk.PhotoImage(image = health)
    return health_photoimage

def get_pokemon_data(gamemode):
    '''returns multiple pieces of information of a single
    random pokemon in one calling

        Args:
            gamemode: The current Gamemode object, which defines how many
            generations the user is playing with

        Returns:
            pokemon_full_name: full name of a single random pokemon
            silhouette_photoimage: silhouette photoimage of said pokemon
            pokemon_photoimage: photoimage of said pokemon
    '''

    random_filename = get_random_filename(gamemode)
    silhouette_filename = get_silhouette(random_filename)
    pokemon_full_name = get_pokemon_full_name(random_filename)
    silhouette_photoimage = get_pokemon_photoimage(silhouette_filename)
    pokemon_photoimage = get_pokemon_photoimage(random_filename)

    return pokemon_full_name, silhouette_photoimage, pokemon_photoimage
