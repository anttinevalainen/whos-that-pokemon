import tkinter as tk
import services.hiscore_init as hi

def create_pokemon_label(frame, photoimage):
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

def create_health_label(frame, health_photoimage):

    health_label = tk.Label(
        frame,
        image = health_photoimage,
        bd = 0,
        highlightthickness = 0,
        relief = 'ridge'
    )
    health_label.place(
        x = 10,
        y = 10
    )

def create_progress_label(frame, player_score):
    progress_label = tk.Label(
            frame,
            text = 'Points: ' + str(player_score.get_points()) + \
                '\n' + 'Correct answers: ' + str(player_score.get_correct_answers()),
            bg = '#ec3025',
            fg = '#0f4d88',
            font = ('Helvetica', 13)
    )
    progress_label.place(
        x = 340,
        y = 20,
        width = 160,
        height = 45
    )

def create_background_label(frame):
    background_image = tk.PhotoImage(file = 'src/data/png/whos_that_pokemon.png')
    background_label = tk.Label(frame,image = background_image)
    background_label.image = background_image
    background_label.place(x = 0,y = 0,width = 640,height = 480)


def create_answer_canvas(frame, text, background):
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
        font = ('Helvetica', 13, 'bold'),
        fill = '#0f4d88'
    )

def create_hiscore_table(frame, value):
    hiscore_df = hi.initialize_hiscore_dataframe().sort_values(by = [value], ascending = False)

    table_cell_width = 65
    table_cell_height = 30
    table_cell_x = 30
    table_cell_y = 120

    gamertag_label = tk.Label(
        frame,
        text = 'Gamertag',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    gamertag_label.place(
        width = table_cell_width,
        height = table_cell_height,
        x = table_cell_x,
        y = table_cell_y - table_cell_height
    )
    points_label = tk.Label(
        frame,
        text = 'Points',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    points_label.place(
        width = table_cell_width,
        height = table_cell_height,
        x = table_cell_x + table_cell_width,
        y = table_cell_y - table_cell_height
    )
    correct_answers_label = tk.Label(
        frame,
        text = '# correct',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    correct_answers_label.place(
        width = table_cell_width,
        height = table_cell_height,
        x = table_cell_x + table_cell_width*2,
        y = table_cell_y - table_cell_height
    )
    gens_label = tk.Label(
        frame,
        text = 'Gens',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    gens_label.place(
        width = table_cell_width,
        height = table_cell_height,
        x = table_cell_x + table_cell_width*3,
        y = table_cell_y - table_cell_height
    )
    for x in range(len(hiscore_df)):
        for y in range(len(hiscore_df.columns)):
            if x % 2 == 0:
                tk.Label(
                    frame,
                    text = str(hiscore_df.iloc[x][y]),
                    bg = '#ec3025',
                    fg = '#0f4d88',
                    font = ('Helvetica', 10)
                ).place(
                    width = table_cell_width,
                    height = table_cell_height,
                    x = table_cell_x + (table_cell_width * y),
                    y = table_cell_y + (table_cell_height * x)
                )
            else:
                tk.Label(
                    frame,
                    text = str(hiscore_df.iloc[x][y]),
                    bg = '#0f4d88',
                    fg = '#ffcb05',
                    font = ('Helvetica', 10)
                ).place(
                    width = table_cell_width,
                    height = table_cell_height,
                    x = table_cell_x + (table_cell_width * y),
                    y = table_cell_y + (table_cell_height * x)
                )

