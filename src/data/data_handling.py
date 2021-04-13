import tkinter as tk
from PIL import Image, ImageTk
import random
import pandas as pd

def get_random_filename():
    '''Returns the png-filename of a random pokemon'''
    directory_df = pd.read_csv('src//data/directory_list.csv', sep = ',')
    random_integer = random.randint(0,len(directory_df))
    filename = directory_df.at[random_integer, 'file']
    return filename

def get_silhouette(filename):
    '''Returns the silhouette image file of a given pokemon image file'''
    silhouette_filepath = 'src//data/png/black_' + filename
    return silhouette_filepath

def get_pokemon_name(filename):
    '''Returns the name of the pokemon with given filepath'''
    pokedex_df = pd.read_csv('src//data/pokedex_list.csv', sep = ',')
    filename = filename[:-4]
    filename_s = filename.split('-')

    pokemon_name_string = pokedex_df.at[int(filename_s[0])-1, 'pokemon']
        
    return pokemon_name_string

def get_pokemon_full_name(filename):
    '''Returns the name and the type of possible secondary form of the pokemon with given filepath'''
    pokedex_df = pd.read_csv('src//data/pokedex_list.csv', sep = ',')
    filename = filename[:-4]
    filename_s = filename.split('-')
    
    if len(filename_s) > 1:
        pokemon_full_name_string = pokedex_df.at[int(filename_s[0])-1, 'pokemon'] + ' (' + filename_s[1] + ')'
    else:
        pokemon_full_name_string = pokedex_df.at[int(filename_s[0])-1, 'pokemon']
        
    return pokemon_full_name_string

def get_silhouette_photoimage(silhouette_filename):
    '''returns a ready made photoimage of the silhouette merged with the background.'''
    '''takes the filename of the silhouette in src//data/png folder'''
    silhouette_image = Image.open(silhouette_filename).convert('RGBA')
    image_background = Image.open('src//data/png/image_background.png').convert("RGBA")
    image_background.paste(silhouette_image, (0, 0), silhouette_image)
    silhouette_image_label = ImageTk.PhotoImage(image_background)
    return silhouette_image_label

def get_pokemon_photoimage(filename):
    '''returns a ready made photoimage of the pokemon merged with the background.'''
    '''takes the filename of the pokemon in src//data/png folder'''
    pokemon_image = Image.open('src//data/png/' + filename).convert('RGBA')
    image_background = Image.open('src//data/png/image_background.png').convert("RGBA")
    image_background.paste(pokemon_image, (0, 0), pokemon_image)
    pokemon_image_label = ImageTk.PhotoImage(image_background)
    return pokemon_image_label

def get_correct_answer(pokemon_name_string):
    '''returns a photoimage of the label background and the string to be placed on top of it when user inputs correct name'''
    '''takes the pokemon name as a string, returns photoimage and a string'''
    background = tk.PhotoImage(file = 'src//data/png/text_background.png')
    text = "CORRECT! \n It's " + pokemon_name_string + '!'
    return background, text

def get_incorrect_answer(pokemon_name_string):
    '''returns a photoimage of the label background and the string to be placed on top of it when user inputs incorrect name'''
    '''takes the pokemon name as a string, returns photoimage and a string'''
    background = tk.PhotoImage(file = 'src//data/png/text_background.png')
    text = "WRONG! \n It's " + pokemon_name_string + '!'
    return background, text
    
def get_pokemon_data():
    '''returns all the data stated in src//data/data_handling.py in one single get command revolving around a single random pokemon
    EXCLUDING: Random filename -string, silhouette filename -string and the correct/incorrect answer data'''
    random_filename = get_random_filename()
    silhouette_filename = get_silhouette(random_filename)
    pokemon_name_string = get_pokemon_name(random_filename)
    pokemon_full_name_string = get_pokemon_full_name(random_filename)
    silhouette_photoimage = get_silhouette_photoimage(silhouette_filename)
    pokemon_photoimage = get_pokemon_photoimage(random_filename)
    return pokemon_name_string, pokemon_full_name_string, silhouette_photoimage, pokemon_photoimage