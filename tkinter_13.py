# import module
import tkinter as tk
import random as rm
from tkinter import filedialog as fd


# functions section
# page switching functions
def to_home():  # switch to home page
    # close first_task, second_task and third_task
    first_task_frame.forget()
    second_task_frame.forget()
    third_task_frame.forget()

    # open home_frame
    home_frame.pack(fill='both', expand=1)


def to_first():  # switch to first task page
    # close home_frame, second_task and third_task
    home_frame.forget()
    second_task_frame.forget()
    third_task_frame.forget()

    # open first_task
    first_task_frame.pack(fill='both', expand=1)


def to_second():  # switch to second task page
    # close home_frame, first_task and third_task
    home_frame.forget()
    first_task_frame.forget()
    third_task_frame.forget()

    # open second_task
    second_task_frame.pack(fill='both', expand=1)


def to_third():  # switch to third task page
    # close home_frame, first_task and second_task
    home_frame.forget()
    first_task_frame.forget()
    second_task_frame.forget()

    # open third_task
    third_task_frame.pack(fill='both', expand=1)


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


# third task function
def list_input():  # add entry to list
    user_list.insert('end', user_input.get())
    user_input.delete(0, 'end')


def list_delete_select():  # delete selected rows
    list_delete = list(user_list.curselection())
    list_delete.sort(reverse=True)
    for i in list_delete:
        user_list.delete(i)


def record_file():  # save list to file
    file_name = fd.asksaveasfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')], defaultextension='txt')
    f = open(file_name, 'w')
    s = ''
    for i in user_list.get(0, 'end'):
        s += f'{str(i)}\n'
    f.write(s)
    f.close()


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
tasks.add_command(label='Task №2', command=to_second)
tasks.add_command(label='Task №3', command=to_third)
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

# task №2
# widgets section
second_task_frame = tk.Frame(root)

for column in range(4):  # set the size of the column and row
    second_task_frame.columnconfigure(column, weight=round(800/4))

second_task_title = tk.Label(second_task_frame, text='Task №2: Sorting')
second_task_title.config(font=('Arial', 18, 'bold'))
second_task_title.grid(columnspan=4, row=0, pady=10, sticky='news')


class GroupWidgets:  # create a constructor
    def __init__(self, m_root, m_font=('Arial', 10)):
        # widgets section
        self.entry = tk.Entry(m_root, font=m_font)
        self.entry.grid(columnspan=4, row=1, padx=10, pady=(10, 5), sticky='news')
        self.label = tk.Label(m_root, font=m_font, bg='black', fg='white', text='--')
        self.label.grid(columnspan=4, row=2, padx=10, pady=5, sticky='news')
        # buttons
        self.btn_sort_abc = tk.Button(m_root, font=m_font, text='Ascending order', command=self.sort_abc)
        self.btn_sort_abc.grid(column=0, row=3, padx=(10, 5), pady=5, sticky='news')
        self.btn_sort_zyx = tk.Button(m_root, font=m_font, text='descending order', command=self.sort_zyx)
        self.btn_sort_zyx.grid(column=1, row=3, padx=5, pady=5, sticky='news')
        self.btn_sort_rn = tk.Button(m_root, font=m_font, text='Random order', command=self.sort_random)
        self.btn_sort_rn.grid(column=2, row=3, padx=5, pady=5, sticky='news')
        self.btn_clear = tk.Button(m_root, font=m_font, text='Clear', command=self.clear)
        self.btn_clear.grid(column=3, row=3, padx=(5, 10), pady=5, sticky='news')

    def get_entry(self):  # get the data in the entry field
        return self.entry.get()

    def sort_abc(self):  # sort in ascending order
        text = list(self.get_entry())
        total_text = []
        for i in text:
            if i != ' ':
                total_text.append(i)
        self.label['text'] = sorted(total_text)

    def sort_zyx(self):  # sort in descending order
        text = list(self.get_entry())
        total_text = []
        for i in text:
            if i != ' ':
                total_text.append(i)
        self.label['text'] = sorted(total_text, reverse=True)

    def sort_random(self):  # sort in random order
        text = list(self.get_entry())
        total_text = []
        for i in text:
            if i != ' ':
                total_text.append(i)
        self.label['text'] = ''

        while len(total_text) != 0:
            random_id = rm.randint(0, len(total_text)-1)
            if len(total_text) == 1:
                self.label['text'] += f'{total_text[random_id]}'
            else:
                self.label['text'] += f'{total_text[random_id]} '
            total_text.pop(random_id)

    def clear(self):  # clear all fields
        self.entry.delete(0, 'end')
        self.label['text'] = ''


group_widgets = GroupWidgets(second_task_frame)  # use the constructor

# task №3
third_task_frame = tk.Frame(root)

for column in range(4):
    third_task_frame.columnconfigure(column, weight=round(800/4))

third_task_title = tk.Label(third_task_frame, text='Task №3: List')
third_task_title.config(font=('Arial', 18, 'bold'))
third_task_title.grid(columnspan=4, row=0, pady=(10, 25), sticky='news')

user_list = tk.Listbox(third_task_frame, selectmode='multiple', font=('Arial', 12))
scroll = tk.Scrollbar(third_task_frame, orient='vertical', command=user_list.yview)
user_list.config(yscrollcommand=scroll.set)
user_list.grid(column=1, columnspan=2, row=1, sticky='news', padx=(10, 20))
scroll.grid(column=2, row=1, sticky='nes')

user_input = tk.Entry(third_task_frame, font=('Arial', 12))
user_input.grid(column=1, columnspan=2, row=2,  sticky='news', padx=(10, 0), pady=(10, 0))

btn_input = tk.Button(third_task_frame, text='Add to list', font=('Arial', 12), command=list_input)
btn_input.grid(column=1, columnspan=2, row=3,  sticky='news', padx=(10, 0))
btn_delete = tk.Button(third_task_frame, text='Delete', font=('Arial', 12), command=list_delete_select)
btn_delete.grid(column=1, row=4,  sticky='news', padx=(10, 0))
btn_save = tk.Button(third_task_frame, text='Save', font=('Arial', 12), command=record_file)
btn_save.grid(column=2, row=4,  sticky='news')

root.mainloop()  # show window
