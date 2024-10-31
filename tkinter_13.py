# import module
import tkinter as tk


# functions section
# page switching functions
def to_home():  # switch to home page
    # close first_task
    first_task_frame.forget()

    # open home_frame
    home_frame.pack(fill='both', expand=1)


def to_first():  # switch to first task page
    # close home_frame
    home_frame.forget()

    # open first_task
    first_task_frame.pack(fill='both', expand=1)


# task functions
# first task functions
def get_red():
    color_name['text'] = 'Red #ff0000'


def get_orange():
    color_name['text'] = 'Orange #ff8000'


def get_yellow():
    color_name['text'] = 'Yellow #ffff00'


def get_green():
    color_name['text'] = 'Green #00ff00'


def get_cyan():
    color_name['text'] = 'Cyan #00bfff'


def get_blue():
    color_name['text'] = 'Blue #0000ff'


def get_purple():
    color_name['text'] = 'Purple #8b00hh'


# root window
root = tk.Tk()
root.title('Result')
root.geometry('800x600')
fullscreen = False

# menu section
main_menu = tk.Menu(root)
root.config(menu=main_menu)

main_menu.add_command(label='Home', command=to_home)  # go to home page

# settings
options = tk.Menu(root, tearoff=0)
resolution = tk.Menu(root, tearoff=0)
resolution.add_command(label='800x600')
resolution.add_command(label='1280x720')
resolution.add_command(label='1920x1080')
options.add_cascade(label='Change resolution')
options.add_command(label='Fullscreen')
options.add_separator()
options.add_command(label='Exit', command=lambda: root.destroy())
main_menu.add_cascade(label='Settings', menu=options)

# list of tasks
tasks = tk.Menu(root, tearoff=0)
main_menu.add_cascade(label='Tasks', menu=tasks)
tasks.add_command(label='Task №1', command=to_first)
tasks.add_command(label='Task №2',)
tasks.add_command(label='Task №3')
tasks.add_command(label='Task №4')
tasks.add_command(label='Task №5')
tasks.add_command(label='Task №6')

# home page
# widgets section
home_frame = tk.Frame(root)
home_title = tk.Label(home_frame, text='Welcome!')
home_label_info = tk.Label(home_frame,
                           text='Here you can select one of the tasks in the top menu and look at its functionality')

# widgets style
home_title.config(font=('home_frame', 20))
home_label_info.config(font=('Arial', 11))

# widgets layout
home_frame.pack(fill='both', expand=1)
home_title.pack(fill='both', pady=(25, 0))
home_label_info.pack()

# task №1
# widgets section
first_task_frame = tk.Frame(root)
first_task_title = tk.Label(first_task_frame, text='task №1: Color palette')
color_name = tk.Label(first_task_frame, text='Choose a color')

# widgets style
first_task_title.config(font=('Arial', 18, 'bold'))
color_name.config(font=('Arial', 16))

for column in range(7):  # set the size of the column and row
    first_task_frame.columnconfigure(column, weight=round(800/7))

# widgets layout
first_task_title.grid(columnspan=7, row=0, pady=10, sticky='news')
color_name.grid(columnspan=7, row=1, pady=(10, 20), sticky='news')

# buttons
btn_red = tk.Button(first_task_frame, width=10, height=4, bg='red', command=get_red)
btn_orange = tk.Button(first_task_frame, width=10, height=4, bg='orange', command=get_orange)
btn_yellow = tk.Button(first_task_frame, width=10, height=4, bg='yellow', command=get_yellow)
btn_green = tk.Button(first_task_frame, width=10, height=4, bg='green', command=get_green)
btn_cyan = tk.Button(first_task_frame, width=10, height=4, bg='cyan', command=get_cyan)
btn_blue = tk.Button(first_task_frame, width=10, height=4, bg='blue', command=get_blue)
btn_purple = tk.Button(first_task_frame, width=10, height=4, bg='purple', command=get_purple)

# buttons layout
btn_red.grid(column=0, row=2)
btn_orange.grid(column=1, row=2)
btn_yellow.grid(column=2, row=2)
btn_green.grid(column=3, row=2)
btn_cyan.grid(column=4, row=2)
btn_blue.grid(column=5, row=2)
btn_purple.grid(column=6, row=2)

root.mainloop()
