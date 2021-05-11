from PIL import Image, ImageTk

def get_pokemon_photoimage(filepath):
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

    img = Image.open(filepath).convert('RGBA')
    image_background = Image.open('src/data/png/image_background.png').convert('RGBA')

    image_background.paste(img, (0, 0), img)
    pokemon_photoimage = ImageTk.PhotoImage(image_background)

    return pokemon_photoimage
