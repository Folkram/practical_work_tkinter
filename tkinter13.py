# import module
import tkinter as tk
import random as rm
from tkinter import filedialog as fd
from tkinter import messagebox as mb


# functions section
# setting function
def get_fullscreen():
    global fullscreen
    root.geometry('+0+0')
    fullscreen = not fullscreen
    root.overrideredirect(fullscreen)


def get_800x600():
    root.geometry('800x600+0+0')


def get_1280x720():
    root.geometry('1280x720+0+0')


def get_1920x1080():
    root.geometry('1920x1080+0+0')


# page switching functions
def to_home():  # switch to home page
    # close another frames
    first_task_frame.forget()
    second_task_frame.forget()
    third_task_frame.forget()
    fourth_task_frame.forget()
    fifth_task_frame.forget()
    sixth_task_frame.forget()

    # open home_frame
    home_frame.pack(fill='both', expand=1)


def to_first():  # switch to first task page
    # close another frames
    home_frame.forget()
    second_task_frame.forget()
    third_task_frame.forget()
    fourth_task_frame.forget()
    fifth_task_frame.forget()
    sixth_task_frame.forget()

    # open first_task
    first_task_frame.pack(fill='both', expand=1)


def to_second():  # switch to second task page
    # close another frames
    home_frame.forget()
    first_task_frame.forget()
    third_task_frame.forget()
    fourth_task_frame.forget()
    fifth_task_frame.forget()
    sixth_task_frame.forget()

    # open second_task
    second_task_frame.pack(fill='both', expand=1)


def to_third():  # switch to third task page
    # close another frames
    home_frame.forget()
    first_task_frame.forget()
    second_task_frame.forget()
    fourth_task_frame.forget()
    fifth_task_frame.forget()
    sixth_task_frame.forget()

    # open third_task
    third_task_frame.pack(fill='both', expand=1)


def to_fourth():  # switch to fourth task page
    # close another frames
    home_frame.forget()
    first_task_frame.forget()
    second_task_frame.forget()
    third_task_frame.forget()
    fifth_task_frame.forget()
    sixth_task_frame.forget()

    # open fourth_task
    fourth_task_frame.pack(fill='both', expand=1)


def to_fifth():
    # close another frames
    home_frame.forget()
    first_task_frame.forget()
    second_task_frame.forget()
    third_task_frame.forget()
    fourth_task_frame.forget()
    sixth_task_frame.forget()

    # open fifth_task
    fifth_task_frame.pack(fill='both', expand=1)


def to_sixth():
    # close another frames
    home_frame.forget()
    first_task_frame.forget()
    second_task_frame.forget()
    third_task_frame.forget()
    fourth_task_frame.forget()
    fifth_task_frame.forget()

    # open sixth_task
    sixth_task_frame.pack(fill='both', expand=1)


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


# fourth task function
def add_item():
    list_item_id = list(catalog.curselection())
    for item_id in list_item_id:
        cart.insert('end', catalog.get(item_id))


def delete_item():
    cart.delete(cart.curselection())


def delete_all_item():
    cart.delete(0, 'end')


def make_order():
    file_name = fd.asksaveasfilename(filetypes=[('Text Files', '*.txt')], defaultextension='txt')
    file = open(file_name, 'w')
    content = ''
    items = list(cart.get(0, 'end'))
    for item in set(items):
        content += f'{item}: {items.count(item)}\n'
    file.write(content)
    file.close()


# fifth task function
def work_array():
    multiplier = multipliers.get()
    output.config(state='normal')
    output.delete(8.0, 'end')
    output.insert('end', f'\n\nModified array\nElement №1: {1*multiplier}\nElement №2: '
                         f'{2*multiplier}\nElement №3: {3*multiplier}\nElement №4: {4*multiplier}\nElement №5: '
                         f'{5*multiplier}\nElement №6: {6*multiplier}')
    if option_amount.get() == 1:
        output.insert('end', f'\n\nSum of all elements: {(1+2+3+4+5+6)*multiplier}')
    if option_composition.get() == 1:
        if option_amount.get() == 1:
            output.insert('end', f'\nProduct of all elements: {(1*2*3*4*5*6)*multiplier}')
        else:
            output.insert('end', f'\n\nProduct of all elements: {(1 * 2 * 3 * 4 * 5 * 6) * multiplier}')
    if option_min.get() == 1:
        if option_amount.get() == 1 or option_composition.get() == 1:
            output.insert('end', f'\nMinimum element: {1*multiplier}')
        else:
            output.insert('end', f'\n\nMaximum element: {1 * multiplier}')
    if option_max.get() == 1:
        if option_amount.get() == 1 or option_composition.get() == 1 or option_min.get() == 1:
            output.insert('end', f'\nMaximum element: {6*multiplier}')
        else:
            output.insert('end', f'\n\nMinimum element: {6 * multiplier}')
    output.config(state='disabled')


# sixth task function
def open_file():
    file_name = fd.askopenfilename()
    if file_name == '':
        mb.showerror('Error!', 'You have not selected a file!')
    else:
        file = open(file_name)
        file_text = file.read()
        output_file.insert('end', file_text)
        file.close()


def save_file():
    file_name = fd.asksaveasfilename(filetypes=[('Text files', '*.txt')], defaultextension='.txt')
    if file_name == '':
        mb.showerror('Error!', "You didn't specify the file!")
    else:
        file = open(file_name, 'w')
        text = output_file.get('1.0', 'end')
        file.write(text)
        file.close()


def clear_output():
    answer = mb.askyesno('Clearing the text field', 'Do you really want to clear the field?')
    if answer:
        output_file.delete(1.0, 'end')
    else:
        pass


def clear_terminal():
    output.config(state='normal')
    output.delete(9.0, 'end')
    output.config(state='disabled')

    multiplier_2.select()

    check_amount.deselect()
    check_composition.deselect()
    check_min.deselect()
    check_max.deselect()


def close():
    to_home()


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
resolution.add_command(label='800x600', command=get_800x600)
resolution.add_command(label='1280x720', command=get_1280x720)
resolution.add_command(label='1920x1080', command=get_1920x1080)
options.add_cascade(label='Change resolution', menu=resolution)
options.add_command(label='Fullscreen', command=get_fullscreen)
options.add_separator()
options.add_command(label='Exit', command=lambda: root.destroy())
main_menu.add_cascade(label='Settings', menu=options)

# list of tasks
tasks = tk.Menu(root, tearoff=0)
main_menu.add_cascade(label='Tasks', menu=tasks)
tasks.add_command(label='Task №1', command=to_first)
tasks.add_command(label='Task №2', command=to_second)
tasks.add_command(label='Task №3', command=to_third)
tasks.add_command(label='Task №4', command=to_fourth)
tasks.add_command(label='Task №5', command=to_fifth)
tasks.add_command(label='Task №6', command=to_sixth)

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

# task №4
fourth_task_frame = tk.Frame(root)

for column in range(4):
    fourth_task_frame.columnconfigure(column, weight=round(800/4))

label_fourth_task = tk.Label(fourth_task_frame, text='Task №4: Cart')
label_fourth_task.config(font=('Arial', 18, 'bold'))
label_fourth_task.grid(columnspan=4, row=0, pady=(10, 25), sticky='news')

label_catalog = tk.Label(fourth_task_frame, text='Catalog', font=('Arial', 14, 'bold'), bg='#d7d7d7')
label_catalog.grid(column=0, columnspan=2, row=1, padx=(10, 15), pady=(10, 5), sticky='news')

label_cart = tk.Label(fourth_task_frame, text='Cart', font=('Arial', 14, 'bold'), bg='#d7d7d7')
label_cart.grid(column=2, columnspan=2, row=1, padx=(10, 10), pady=(10, 5), sticky='news')

# add items to catalog
catalog = tk.Listbox(fourth_task_frame, font=('Arial', 12), selectmode='extended')
catalog.insert(0, 'Drill')
catalog.insert(1, 'Hammer')
catalog.insert(3, 'Screwdriver')
catalog.insert(4, 'Spoon')
catalog.insert(5, 'Fork')
catalog.insert(6, 'Chair')
catalog.insert(7, 'Table')
catalog.insert(8, 'Door')
catalog.insert(9, 'Lock')
catalog.insert(10, 'Pillow')
catalog.insert(11, 'Blank')
catalog.insert(12, 'Bed')

scroll = tk.Scrollbar(fourth_task_frame, orient='vertical', command=catalog.yview)
catalog.config(yscrollcommand=scroll.set)
catalog.grid(column=0, columnspan=2, row=2, padx=(10, 10), sticky='news')
scroll.grid(column=1, row=2, padx=(0, 10), sticky='nes')

cart = tk.Listbox(fourth_task_frame, font=('Arial', 12))
cart.grid(column=2, columnspan=2, row=2, padx=(10, 10), sticky='news')

btn_add = tk.Button(fourth_task_frame, text='Add to cart', font=('Arial', 12), bg='#d7d7d7', border=0, command=add_item)
btn_add.grid(column=0, columnspan=2, row=3, pady=(10, 0), padx=(10, 5), sticky='news')
btn_delete_item = tk.Button(fourth_task_frame, text='Delete', font=('Arial', 12), bg='#d7d7d7', border=0,
                            command=delete_item)
btn_delete_item.grid(column=2, columnspan=2, row=3, pady=(10, 0), padx=(5, 10), sticky='news')
btn_delete_all = tk.Button(fourth_task_frame, text='Delete all', font=('Arial', 12), bg='#d7d7d7', border=0,
                           command=delete_all_item)
btn_delete_all.grid(column=0, columnspan=2, row=4, padx=(10, 5), pady=(5, 0), sticky='news')
btn_order = tk.Button(fourth_task_frame, text='Order', font=('Arial', 12), bg='#d7d7d7', border=0, command=make_order)
btn_order.grid(column=2, columnspan=2, row=4, padx=(5, 10), pady=(5, 0), sticky='news')

# task №5
fifth_task_frame = tk.Frame(root)

for column in range(8):
    fifth_task_frame.columnconfigure(column, weight=round(800/8))

label_fifth_task = tk.Label(fifth_task_frame, text='Task №5: Working with an array of numbers')
label_fifth_task.config(font=('Arial', 18, 'bold'))
label_fifth_task.grid(columnspan=8, row=0, pady=(10, 25), sticky='news')

label_multiplier = tk.Label(fifth_task_frame, text='Select multiplier', font=('Arial', 10, 'bold'))
label_multiplier.grid(column=0, row=1, sticky='news')

multipliers = tk.IntVar()
multiplier_2 = tk.Radiobutton(fifth_task_frame, text='x2', value=2, variable=multipliers)
multiplier_2.grid(column=0, row=2, sticky='news')
multiplier_3 = tk.Radiobutton(fifth_task_frame, text='x3', value=3, variable=multipliers)
multiplier_3.grid(column=0, row=3, sticky='news')
multiplier_4 = tk.Radiobutton(fifth_task_frame, text='x4', value=4, variable=multipliers)
multiplier_4.grid(column=0, row=4, sticky='news')
multiplier_5 = tk.Radiobutton(fifth_task_frame, text='x5', value=5, variable=multipliers)
multiplier_5.grid(column=0, row=5, sticky='news')

multiplier_2.select()

label_multiplier = tk.Label(fifth_task_frame, text='Output settings', font=('Arial', 10, 'bold'))
label_multiplier.grid(column=1, row=1, sticky='nws')

option_amount = tk.IntVar()
option_composition = tk.IntVar()
option_min = tk.IntVar()
option_max = tk.IntVar()

check_amount = tk.Checkbutton(fifth_task_frame, text='Display amount', onvalue=1, offvalue=0, variable=option_amount)
check_amount.grid(column=1, row=2, sticky='nws')
check_composition = tk.Checkbutton(fifth_task_frame, text='Display composition', onvalue=1, offvalue=0,
                                   variable=option_composition)
check_composition.grid(column=1, row=3, sticky='nws')
check_min = tk.Checkbutton(fifth_task_frame, text='Minimum element', onvalue=1, offvalue=0,  variable=option_min)
check_min.grid(column=1, row=4, sticky='nws')
check_max = tk.Checkbutton(fifth_task_frame, text='Maximum element', onvalue=1, offvalue=0,  variable=option_max)
check_max.grid(column=1, row=5, sticky='nws')

label_multiplier = tk.Label(fifth_task_frame, text='Terminal', font=('Arial', 10, 'bold'))
label_multiplier.grid(column=2, columnspan=6, row=1, sticky='nws')

output = tk.Text(fifth_task_frame, bg='white', wrap='word', height=10, width=50)
scroll = tk.Scrollbar(fifth_task_frame, orient='vertical', command=output.yview)
output.insert('end', 'Initial array\nElement №1: 1\nElement №2: 2\nElement №3: 3\nElement №4: 4\n'
                     'Element №5: 5\nElement №6: 6\n')
output.config(state='disabled', yscrollcommand=scroll.set)
output.grid(column=2, columnspan=6, row=2, rowspan=6, sticky='news', padx=(0, 10))
scroll.grid(column=7, row=2, rowspan=6, sticky='nes', padx=(0, 10))

frame_btn_menu = tk.Frame(fifth_task_frame)
frame_btn_menu.grid(column=0, columnspan=2, row=7, sticky='news', pady=(10, 0))
for column in range(3):
    frame_btn_menu.columnconfigure(column, weight=round(((800/15)*2)/3))
btn_execute = tk.Button(frame_btn_menu, text='Execute', command=work_array)
btn_execute.grid(column=0, row=0, sticky='news', padx=(10, 5))
btn_clear = tk.Button(frame_btn_menu, text='Clear', command=clear_terminal)
btn_clear.grid(column=1, row=0, sticky='news', padx=5)
btn_close = tk.Button(frame_btn_menu, text='Exit', command=close)
btn_close.grid(column=2, row=0, sticky='news', padx=(5, 10))

# task №6
sixth_task_frame = tk.Frame(root)

for column in range(3):
    sixth_task_frame.columnconfigure(column, weight=round(800/3))

label_sixth_task = tk.Label(sixth_task_frame, text='Task №6: Working with files')
label_sixth_task.config(font=('Arial', 18, 'bold'))
label_sixth_task.grid(columnspan=3, row=0, pady=(10, 25), sticky='news')

output_file = tk.Text(sixth_task_frame, width=100, height=20)
output_file.grid(column=0, columnspan=3, row=1, sticky='news', padx=10, pady=(0, 10))
btn_open_file = tk.Button(sixth_task_frame, text='Open file', command=open_file)
btn_open_file.grid(column=0, row=2, sticky='news', padx=(10, 5))
btn_save_file = tk.Button(sixth_task_frame, text='Save file', command=save_file)
btn_save_file.grid(column=1, row=2, sticky='news', padx=(5, 5))
btn_clear_file = tk.Button(sixth_task_frame, text='Clear', command=clear_output)
btn_clear_file.grid(column=2, row=2, sticky='news', padx=(5, 10))

root.mainloop()  # show window
