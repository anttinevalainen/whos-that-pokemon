import tkinter as tk

import services.hiscore_service as hs

def create_pokemon_label(frame, photoimage):
    '''Creates and displays a label with Pokémon's/silhouette's image
    combined with interface background

            Args:
                frame: The frame image is displayed upon
                photoimage: A photoimage object of the image created with
                function in pokemon_service.py

            Returns:
                None'''
    pokemon_label = tk.Label(
        frame,
        image = photoimage,
        bd = 0,
        highlightthickness = 0,
        relief = 'ridge'
    )
    pokemon_label.place(
        x = 33,
        y = 104
    )

def create_health_label(frame, photoimage):
    '''Creates and displays a label with user's health level expressed
    with three heart symbols, combined with interface background

            Args:
                frame: The frame image is displayed upon
                photoimage: A photoimage object of the image created with
                function in player_service.py

            Returns:
                None'''
    tk.Label(
        frame,
        image = photoimage,
        bd = 0,
        highlightthickness = 0,
        relief = 'ridge'
    ).place(
        x = 10,
        y = 10
    )

def create_progress_label(frame, player):
    '''Creates and displays a label with user's progress. The label
    tells how many correct answers user has got and their current points

            Args:
                frame: The frame image is displayed upon
                player: Current user object

            Returns:
                None'''
    points = player.get_points()
    answers = player.get_correct_answers()

    tk.Label(
            frame,
            text = 'Points: ' + str(points) + \
                '\n' + 'Correct answers: ' + str(answers),
            bg = '#ec3025',
            fg = '#0f4d88',
            font = ('Helvetica', 13)
    ).place(
        x = 340,
        y = 20,
        width = 160,
        height = 45
    )

def create_background_label(frame):
    '''Creates and displays the background for the page

            Args:
                frame: The frame image is displayed upon

            Returns:
                None'''
    background_image = tk.PhotoImage(file = 'src/data/png/whos_that_pokemon.png')
    background_label = tk.Label(frame,image = background_image)
    background_label.image = background_image
    background_label.place(x = 0,y = 0,width = 640,height = 480)


def create_answer_canvas(frame, text, background):
    '''Creates and displays a label with user's health level expressed
    with three heart symbols, combined with interface background

            Args:
                frame: The frame image is displayed upon
                text: The text displayed within the label, created with the
                check_answer function in player_service.py
                background: Background photoimage the text is displayed on

            Returns:
                None'''
    text_canvas = tk.Canvas(
        frame,
        bd = 0,
        highlightthickness = 0,
        relief = 'ridge',
    )
    text_canvas.place(
        x = 20,
        y = 400,
        width = 200,
        height = 60
    )
    text_canvas.create_image(
        200/2,
        60/2,
        image = background
    )
    text_canvas.create_text(
        200/2,
        20,
        text = text,
        font = ('Helvetica', 10, 'bold'),
        fill = '#0f4d88'
    )

def create_hiscore_table(frame):
    '''Creates and displays the hiscore table in the hiscore page. The table
    size is 4x10 including the column names

            Args:
                frame: The frame image is displayed upon

            Returns:
                None'''
    hiscore_df = hs.initialize_hiscore_dataframe().sort_values(
        by = ['points'],
        ascending = False)

    table_cell_width = 65
    table_cell_height = 30
    table_cell_x = 30
    table_cell_y = 120

    for index in range(len(hiscore_df.columns)):
        table_label = hiscore_df.columns[index].capitalize()
        tk.Label(
            frame,
            text = table_label,
            bg = '#0f4d88',
            fg = '#ffcb05',
            font = ('Helvetica', 10, 'bold')
        ).place(
            width = table_cell_width,
            height = table_cell_height,
            x = table_cell_x + (table_cell_width * index),
            y = table_cell_y - table_cell_height
        )

    for index in range(len(hiscore_df)):
        for column in range(len(hiscore_df.columns)):
            if index % 2 == 0:
                tk.Label(
                    frame,
                    text = str(hiscore_df.iloc[index][column]),
                    bg = '#ec3025',
                    fg = '#0f4d88',
                    font = ('Helvetica', 10)
                ).place(
                    width = table_cell_width,
                    height = table_cell_height,
                    x = table_cell_x + (table_cell_width * column),
                    y = table_cell_y + (table_cell_height * index)
                )
            else:
                tk.Label(
                    frame,
                    text = str(hiscore_df.iloc[index][column]),
                    bg = '#0f4d88',
                    fg = '#ffcb05',
                    font = ('Helvetica', 10)
                ).place(
                    width = table_cell_width,
                    height = table_cell_height,
                    x = table_cell_x + (table_cell_width * column),
                    y = table_cell_y + (table_cell_height * index)
                )
