from tkinter import *

"""
default_grid = [[0, 0, 4, | 0, 6, 0, | 0, 0, 5],
                [7, 8, 0, | 4, 0, 0, | 0, 2, 0],
                [0, 0, 2, | 6, 0, 1, | 0, 7, 8],
                -------------------------------
                [6, 1, 0, | 0, 7, 5, | 0, 0, 9],
                [0, 0, 7, | 5, 4, 0, | 0, 6, 1],
                [0, 0, 1, | 7, 5, 0, | 9, 3, 0],
                -------------------------------
                [0, 7, 0, | 3, 0, 0, | 0, 1, 0],
                [0, 4, 0, | 2, 0, 6, | 0, 0, 7],
                [0, 2, 0, | 0, 0, 7, | 4, 0, 0],]

answer_grid = [
[3, 5, 2, 4, 7, 6, 1, 8, 9], 
[1, 6, 8, 9, 5, 2, 7, 3, 4], 
[7, 4, 9, 8, 1, 3, 6, 2, 5], 
[4, 0, 0, 0, 0, 0, 8, 0, 0], 
[0, 8, 3, 2, 0, 1, 5, 9, 0], 
[0, 0, 1, 0, 0, 0, 0, 0, 2], 
[0, 9, 7, 3, 0, 5, 2, 4, 0], 
[2, 0, 0, 0, 0, 9, 0, 5, 6], 
[0, 0, 0, 1, 0, 0, 9, 7, 0]
]

"""


class Num_Button:

    def __init__(self, window_name, row, column):
        self.number = 0
        self.win = window_name
        self.row = row
        self.column = column
        self.button = Button(bg='green',
                             fg='black',
                             activebackground='green',
                             activeforeground='black',
                             font=('courier', 21, 'italic'))

    def button_real(self):
        self.button.bind("<Button-1>", self.update_num)
        self.button.config(text=' ',
                           relief=RAISED,
                           bd=3)
        self.button.grid(row=self.row, column=self.column)

    def button_preset(self):
        self.button.grid(row=self.row, column=self.column)

    def update_num(self, event):
        if self.number > 8:
            self.number = 0
        self.number += 1

        self.button.config(text=str(self.number))

        default_grid[self.row][self.column] = self.number

        if default_grid == answer_grid:
            label = Label(self.win,
                          text="You Win!",
                          font=('Arial', 35, 'bold'),
                          fg='black',
                          bg='cyan',
                          relief=SUNKEN,
                          bd=6)
            label.place(x=120, y=150)

            self.button.config(state=DISABLED)

        try:
            print(f"Number changed to '{self.number}' "
                  f"at Position({self.row}, {self.column})")
        except Exception as e:
            print('Cannot Display EVENT INFO.', '\n',
                  'Python v3.6 or above Required', '\n',
                  e)
        # else:
        # finally:


default_grid = [
    [0, 5, 2, '|', 0, 0, 6, '|', 0, 0, 0],
    [1, 6, 0, '|', 9, 0, 0, '|', 0, 0, 4],
    [0, 4, 9, '|', 8, 0, 3, '|', 6, 2, 0],
    ['-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-', ],
    [4, 0, 0, '|', 0, 0, 0, '|', 8, 0, 0],
    [0, 8, 3, '|', 2, 0, 1, '|', 5, 9, 0],
    [0, 0, 1, '|', 0, 0, 0, '|', 0, 0, 2],
    ['-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-', ],
    [0, 9, 7, '|', 3, 0, 5, '|', 2, 4, 0],
    [2, 0, 0, '|', 0, 0, 9, '|', 0, 5, 6],
    [0, 0, 0, '|', 1, 0, 0, '|', 9, 7, 0]
]

"""          Answer Finder        """

# PENDING!

answer_grid = [
    [3, 5, 2, '|', 4, 7, 6, '|', 1, 8, 9],
    [1, 6, 8, '|', 9, 5, 2, '|', 7, 3, 4],
    [7, 4, 9, '|', 8, 1, 3, '|', 6, 2, 5],
    ['-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-', ],
    [4, 2, 5, '|', 6, 9, 7, '|', 8, 1, 3],
    [6, 8, 3, '|', 2, 4, 1, '|', 5, 9, 7],
    [9, 7, 1, '|', 5, 3, 8, '|', 4, 6, 2],
    ['-', '-', '-', '+', '-', '-', '-', '+', '-', '-', '-', ],
    [8, 9, 7, '|', 3, 6, 5, '|', 2, 4, 1],
    [2, 1, 4, '|', 7, 8, 9, '|', 3, 5, 6],
    [5, 3, 6, '|', 1, 2, 4, '|', 9, 7, 8]
]

buttons = []


def button_creator(win):
    global default_grid
    global answer_grid
    global buttons

    # Creating List of 81 Buttons!
    for r in range(11):
        row_lst = []
        for c in range(11):
            row_lst.append(Num_Button(win, r, c))
        buttons.append(row_lst)

    # Assigning the Real Values to Buttons in the List
    # from the default grid
    for i in range(11):
        for j in range(11):
            buttons[i][j].button.config(
                text=str(default_grid[i][j]))

    # Now, Assigning the Functionality for every Button...
    # according to its kind.
    for i in range(11):
        for j in range(11):
            text_val = buttons[i][j].button.cget('text')

            if text_val == '|' or text_val == '-' or text_val == '+':
                buttons[i][j].button.config(state=DISABLED,
                                            bg='#ebeaf7',
                                            relief=FLAT,
                                            font=('courier', 4))
                if text_val == '|':
                    buttons[i][j].button.config(pady=24)
                if text_val == '-':
                    buttons[i][j].button.config(padx=18)
                buttons[i][j].button_preset()

            elif 1 <= int(text_val) <= 9:
                buttons[i][j].button_preset()
                buttons[i][j].button.config(state=DISABLED,
                                            bg='black',
                                            relief=RAISED,
                                            bd=6,
                                            font=('courier', 20, 'bold'))
            else:
                buttons[i][j].button_real()
                buttons[i][j].button.config(font=('courier', 20, 'bold'),
                                            relief=RAISED,
                                            bd=6)


def game_window():
    main_menu.destroy()
    sudoku_window = Tk()
    # main_menu.geometry('1920x1080')
    sudoku_window.title("Button Sudoku")
    button_creator(sudoku_window)


if __name__ == '__main__':
    main_menu = Tk()
    main_menu.title()
    # main_menu.configure(background='blue')
    main_menu.attributes('-fullscreen', TRUE)
    """main_menu.geometry("{0}x{1}+0+0".format(
        main_menu.winfo_screenwidth()-3,
        main_menu.winfo_screenheight()-3))

    def toggle_geo(event):
        resize_geo = '400x400+0+0'
        geo = main_menu.winfo_geometry()
        print(geo, resize_geo)
        main_menu.geometry(resize_geo)
        resize_geo = geo

    main_menu.bind('<Escape>', toggle_geo)"""

    frame_logo = Frame(main_menu)
    frame_logo.place(x=460, y=130)

    game_name_label = Label(frame_logo,
                            text="Button Sudoku",
                            # segoe script,symbol,small fonts
                            font=('papyrus', 45),
                            padx=20)
    game_name_label.pack(side=TOP)

    play_button = Button(frame_logo,
                         text="Play",
                         font=('small fonts', 25),
                         fg='white',
                         bg='black',
                         activeforeground='white',
                         activebackground='black',
                         relief=RAISED,
                         bd=7,
                         command=game_window,
                         padx=50)
    play_button.pack(side=TOP)

    quit_button = Button(frame_logo,
                         text="Quit",
                         font=('small fonts', 25),
                         fg='white',
                         bg='black',
                         activeforeground='white',
                         activebackground='black',
                         relief=RAISED,
                         bd=7,
                         command=lambda: main_menu.destroy(),
                         padx=51)
    quit_button.pack(side=TOP)

    frame_version = Frame(main_menu)
    frame_version.pack(anchor='se', side=BOTTOM)

    version_label = Label(frame_version,
                          text='v.0 Beta',
                          font=('small font', 20, 'bold'))
    version_label.pack()

    main_menu.mainloop()
