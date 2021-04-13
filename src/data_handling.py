import tkinter as tk
from PIL import Image
import random
import pandas as pd

def get_random_filename():
    '''Returns the png-filename of a random pokemon'''
    directory_df = pd.read_csv('data/directory_list.csv', sep = ',')
    random_integer = random.randint(0,len(directory_df))
    filename = directory_df.at[random_integer, 'file']
    return filename

def get_silhouette(filename):
    '''Returns the silhouette image file of a given pokemon image file'''
    silhouette_filepath = 'data/png/black_' + filename
    return silhouette_filepath

def get_pokemon_name(filename):
    '''Returns the name of the pokemon with given filepath'''
    pokedex_df = pd.read_csv('data/pokedex_list.csv', sep = ',')
    filename = filename[:-4]
    filename_s = filename.split('-')

    pokemon_name_string = pokedex_df.at[int(filename_s[0])-1, 'pokemon']
        
    return pokemon_name_string

def get_pokemon_full_name(filename):
    '''Returns the name and the type of possible secondary form of the pokemon with given filepath'''
    pokedex_df = pd.read_csv('data/pokedex_list.csv', sep = ',')
    filename = filename[:-4]
    filename_s = filename.split('-')
    
    if len(filename_s) > 1:
        pokemon_full_name_string = pokedex_df.at[int(filename_s[0])-1, 'pokemon'] + ' (' + filename_s[1] + ')'
    else:
        pokemon_full_name_string = pokedex_df.at[int(filename_s[0])-1, 'pokemon']
        
    return pokemon_full_name_string

def get_silhouette_photoimage(silhouette_filename):
    silhouette_image = Image.open(silhouette_filename).convert('RGBA')
    image_background = Image.open('data/png/image_background.png').convert("RGBA")
    image_background.paste(silhouette_image, (0, 0), silhouette_image)
    silhouette_image_label = tk.PhotoImage(image_background)
    return silhouette_image_label

def get_pokemon_photoimage(filename):
    pokemon_image = Image.open('data/png/' + filename).convert('RGBA')
    image_background = Image.open('data/png/image_background.png').convert("RGBA")
    image_background.paste(pokemon_image, (0, 0), pokemon_image)
    pokemon_image_label = tk.PhotoImage(image_background)
    return pokemon_image_label

def get_silhouette_image(silhouette_filename):
    silhouette_image = Image.open(silhouette_filename).convert('RGBA')
    return silhouette_image

def get_pokemon_image(filename):
    pokemon_image = Image.open('data/png/' + filename).convert('RGBA')
    return pokemon_image

def get_correct_answer(pokemon_name_string):
    background = tk.PhotoImage(file = 'data/png/text_background.png')
    text = "CORRECT!/nIt's " + pokemon_name_string + '!'
    return background, text

def get_incorrect_answer(pokemon_name_string):
    background = tk.PhotoImage(file = 'data/png/text_background.png')
    text = "WRONG!/nIt's " + pokemon_name_string + '!'
    return background, text
    
def get_pokemon_data():
    random_filename = get_random_filename()
    silhouette_filename = get_silhouette(random_filename)
    pokemon_name_string = get_pokemon_name(random_filename)
    pokemon_full_name_string = get_pokemon_full_name(random_filename)
    silhouette_image = get_silhouette_image(silhouette_filename)
    pokemon_image = get_pokemon_image(random_filename)
    silhouette_photoimage = get_silhouette_photoimage(silhouette_filename)
    pokemon_photoimage = get_pokemon_photoimage(random_filename)
    return random_filename, silhouette_filename, pokemon_name_string, pokemon_full_name_string, silhouette_image, pokemon_image, silhouette_photoimage, pokemon_photoimage