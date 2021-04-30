import tkinter as tk
from gameplay.hiscore_save import initialize_hiscore_dataframe

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

def create_hiscore_table(frame):
    hiscore_df = initialize_hiscore_dataframe().sort_values(by = ['points'], ascending = False)
    cell_width = 65
    cell_height = 30
    cell_x = 30
    cell_y = 120

    gamertag_title = tk.Label(
        frame,
        text = 'Gamertag',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    gamertag_title.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y - cell_height
    )
    points_title = tk.Label(
        frame,
        text = 'Points',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    points_title.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y - cell_height
    )
    correct_answers_title = tk.Label(
        frame,
        text = '# correct',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    correct_answers_title.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y - cell_height
    )
    gens_title = tk.Label(
        frame,
        text = 'Gens',
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10, 'bold')
    )
    gens_title.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y - cell_height
    )

    row1_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[0][0]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row1_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y
    )
    row1_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[0][1]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row1_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y
    )
    row1_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[0][2]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row1_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y
    )
    row1_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[0][3]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row1_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y
    )

    row2_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[1][0]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row2_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height
    )
    row2_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[1][1]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row2_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height
    )
    row2_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[1][2]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row2_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height
    )
    row2_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[1][3]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row2_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height
    )

    row3_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[2][0]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row3_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height*2
    )
    row3_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[2][1]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row3_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height*2
    )
    row3_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[2][2]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row3_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height*2
    )
    row3_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[2][3]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row3_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height*2
    )

    row4_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[3][0]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row4_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height*3
    )
    row4_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[3][1]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row4_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height*3
    )
    row4_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[3][2]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row4_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height*3
    )
    row4_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[3][3]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row4_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height*3
    )

    row5_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[4][0]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row5_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height*4
    )
    row5_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[4][1]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row5_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height*4
    )
    row5_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[4][2]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row5_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height*4
    )
    row5_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[4][3]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row5_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height*4
    )
    row6_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[5][0]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row6_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height*5
    )
    row6_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[5][1]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row6_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height*5
    )
    row6_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[5][2]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row6_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height*5
    )
    row6_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[5][3]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row6_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height*5
    )
    row7_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[6][0]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row7_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height*6
    )
    row7_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[6][1]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row7_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height*6
    )
    row7_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[6][2]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row7_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height*6
    )
    row7_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[6][3]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row7_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height*6
    )
    row8_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[7][0]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row8_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height*7
    )
    row8_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[7][1]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row8_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height*7
    )
    row8_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[7][2]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row8_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height*7
    )
    row8_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[7][3]),
        bg = '#0f4d88',
        fg = '#ffcb05',
        font = ('Helvetica', 10)
    )
    row8_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height*7
    )
    row9_cell1 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[8][0]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row9_cell1.place(
        width = cell_width,
        height = cell_height,
        x = cell_x,
        y = cell_y + cell_height*8
    )
    row9_cell2 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[8][1]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row9_cell2.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width,
        y = cell_y + cell_height*8
    )
    row9_cell3 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[8][2]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row9_cell3.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*2,
        y = cell_y + cell_height*8
    )
    row9_cell4 = tk.Label(
        frame,
        text = str(hiscore_df.iloc[8][3]),
        bg = '#ec3025',
        fg = '#0f4d88',
        font = ('Helvetica', 10)
    )
    row9_cell4.place(
        width = cell_width,
        height = cell_height,
        x = cell_x + cell_width*3,
        y = cell_y + cell_height*8
    )
