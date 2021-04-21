import random
import pandas as pd
from PIL import Image, ImageTk

def get_random_filename():
    '''Returns the png-filename of a random pokemon'''
    directory_df = pd.read_csv('src/data/directory_list.csv', sep = ',')
    random_integer = random.randint(0,len(directory_df)-1)
    filename = directory_df.at[random_integer, 'file']

    return filename

def get_silhouette(filename):
    '''Returns the silhouette image file of a given pokemon image file'''
    silhouette_filepath = 'src/data/png/black_' + filename
    return silhouette_filepath

def get_pokemon_full_name(filename):
    '''Returns the name and the type of possible secondary form (string)\
        Requires the filename of said pokemon (string)'''
    pokedex_df = pd.read_csv('src/data/pokedex_list.csv', sep = ',')
    filename = filename[:-4]
    filename_s = filename.split('-')
    filenumber = int(filename_s[0])-1

    if len(filename_s) > 1:
        second_part = filename_s[1]
        first_part = pokedex_df.at[filenumber, 'pokemon']

        pokemon_full_name_string = first_part + ' (' + second_part + ')'

    else:

        pokemon_full_name_string = pokedex_df.at[filenumber, 'pokemon']

    return pokemon_full_name_string

def get_silhouette_photoimage(silhouette_filename):
    '''returns a ready made photoimage of the silhouette merged with \
        the background. Takes the filename of the silhouette in \
        src/data/png folder'''
    silhouette_image = Image.open(silhouette_filename).convert('RGBA')
    image_background = Image.open('src/data/png/image_background.png').convert('RGBA')
    image_background.paste(silhouette_image, (0, 0), silhouette_image)
    silhouette_photoimage = ImageTk.PhotoImage(image_background)
    return silhouette_photoimage

def get_pokemon_photoimage(filename):
    '''returns a ready made photoimage of the pokemon
    merged with the background. requires the filename of
    the pokemon in src/data/png folder'''
    pokemon_image = Image.open('src/data/png/' + filename).convert('RGBA')
    image_background = Image.open('src/data/png/image_background.png').convert('RGBA')
    image_background.paste(pokemon_image, (0, 0), pokemon_image)
    pokemon_photoimage = ImageTk.PhotoImage(image_background)
    return pokemon_photoimage

def check_answer(pokemon_full_name_string, answer):
    '''returns a a boolean value of answer correctness. requires
    the pokemon_full_name and user input as string values'''

    correct = False
    pokemon_name = pokemon_full_name_string.split(' ')[0].lower()

    if answer.lower() == pokemon_name.lower():
        correct = True

    return correct

def get_health_photoimage(player_score):
    '''returns a ready made photoimage of player's health merged with
    the background. Requires the current player_score as a variable'''

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

def get_pokemon_data():
    '''Returns Pokémon name(string), Pokémon full name (string),
    silhouette image w/ background (photoimage) and Pokémon image
    w/ background (photoimage)'''
    random_filename = get_random_filename()
    silhouette_filename = get_silhouette(random_filename)
    pokemon_full_name_string = get_pokemon_full_name(random_filename)
    silhouette_photoimage = get_silhouette_photoimage(silhouette_filename)
    pokemon_photoimage = get_pokemon_photoimage(random_filename)

    return pokemon_full_name_string, silhouette_photoimage, pokemon_photoimage
