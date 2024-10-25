# import module
import tkinter as tk


# functions section
def pattern():  # insert pattern into all fields
    text_about_yourself.delete(1.0, 'end')
    text_about_yourself.insert(1.0, "A good and honest man \n"
                                    "who is also very hardworking,\n"
                                    "but that's not all! I'm also very humble.\n"
                                    "This is your best chance not to miss someone like me!")
    entry_name.insert(1, 'Oleg')
    entry_password.insert(1, 'OlegIsGood')

    # line-by-line formatting
    text_about_yourself.tag_add('second', 2.0, '2.end')
    text_about_yourself.tag_config('second', font=('Arial', round(def_font_size * 0.9)))
    text_about_yourself.tag_add('third', 3.0, '3.end')
    text_about_yourself.tag_config('third', font=('Arial', round(def_font_size * 0.8)))
    text_about_yourself.tag_add('forth', 4.0, '4.end')
    text_about_yourself.tag_config('forth', font=('Arial', round(def_font_size * 0.7)))
    text_about_yourself.tag_add('fifth', 5.0, '5.end')
    text_about_yourself.tag_config('fifth', font=('Arial', round(def_font_size * 0.6)))


def show_password():  # show or hide password
    if button_show_password['text'] == 'Show password':
        entry_password['show'] = ''
        button_show_password['text'] = 'Hide password'
    else:
        entry_password['show'] = '*'
        button_show_password['text'] = 'Show password'


# root window
root = tk.Tk()
root.title('Form')
root.geometry('350x400')
# default values
def_font_size = 10
def_width = 40
def_height = 10

# widgets section
main_frame = tk.Frame(root)
label_main = tk.Label(main_frame, text='Form')
label_text_about_yourself = tk.Label(main_frame, text='Tell about yourself')
text_about_yourself = tk.Text(main_frame)
label_name = tk.Label(main_frame, text='Enter your name')
entry_name = tk.Entry(main_frame)
label_password = tk.Label(main_frame, text='Enter your password')
entry_password = tk.Entry(main_frame, show='*')
button_pattern = tk.Button(main_frame, text='Pattern', command=pattern)
button_show_password = tk.Button(main_frame, text='Show password', command=show_password)
button_post = tk.Button(main_frame, text='Send')
button_clear = tk.Button(main_frame, text='Clear')

# widgets style
label_main.config(font=('Arial', round(def_font_size*2.5), 'bold'))
label_text_about_yourself.config(font=('Arial', round(def_font_size*1.2), 'italic'))
text_about_yourself.config(width=def_width, height=def_height, wrap='word', font=('Arial', def_font_size))
label_name.config(font=('Arial', def_font_size, 'italic'))
label_password.config(font=('Arial', def_font_size, 'italic'))
button_pattern.config(width=round(def_width/2), font=('Arial', round(def_font_size*0.9)))
button_show_password.config(width=round(def_width/2), font=('Arial', round(def_font_size*0.9)))
button_post.config(width=round(def_width/2), font=('Arial', round(def_font_size*0.9)))
button_clear.config(width=round(def_width/2), font=('Arial', round(def_font_size*0.9)))

# placement of widgets
main_frame.pack(expand=1)
label_main.grid(columnspan=2, row=0, pady=10)
label_text_about_yourself.grid(columnspan=2, row=1, sticky='w')
text_about_yourself.grid(columnspan=2, row=2, pady=(0, 10))
label_name.grid(column=0, row=3, sticky='w')
entry_name.grid(column=1, row=3, sticky='e')
label_password.grid(column=0, row=4, sticky='w')
entry_password.grid(column=1, row=4, sticky='e')
button_pattern.grid(column=0, row=5, pady=(10, 0), sticky='w')
button_show_password.grid(column=1, row=5, pady=(10, 0), sticky='e')
button_post.grid(column=0, row=6, pady=(5, 0), sticky='w')
button_clear.grid(column=1, row=6, pady=(5, 0), sticky='e')

root.mainloop()  # display window
