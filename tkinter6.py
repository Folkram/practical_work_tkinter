# import modules
import tkinter as tk
import tkinter.messagebox as mb


# functions section
def king_penguins_info():
    message = ('The King penguin is similar to the Emperor penguin, but slightly smaller in size and brighter in color.'
               ' The body length of the king penguin is up to 1 m. Adult birds have a gray back, large bright orange '
               'spots on the sides of the black head and on the chest. The belly is white.')
    mb.showinfo('Information about the King Penguins', message)


def warning_message():
    mb.showwarning('Warning', 'This message was created to warn you')


def error_message():
    mb.showerror('Error!', 'Error stop 0000')


def guessing():
    var = mb.askquestion('Question', 'Yes or no?')
    mb.showinfo('Let me guess...', f'You answered {var}')


def repeat():
    n = 1
    while 1:
        if mb.askretrycancel('Infinity', f'Attempt number {n}'):
            n += 1
        else:
            mb.showerror('Error!', 'You have interrupted this cycle... damn')
            break


def three_buttons():
    option = mb.showinfo('Three buttons', 'Three buttons', type='abortretryignore')
    mb.showinfo('Option', f'You chose {option}')


# root window
root = tk.Tk()
root.title('Message Box')
root.geometry('1200x200')


# constructor
class CreateButton:
    def __init__(self, win, btn_name, btn_func, column_num, row_num):
        self.btn = tk.Button(win, text=btn_name, command=btn_func)
        self.btn.config(font=('Arial', 14))
        self.btn.grid(column=column_num, row=row_num, padx=10, pady=10, sticky='news')


# widget section
label_frame = tk.LabelFrame(root, text='Button Menu', font=('Arial', 14))
label_frame.pack(fill='both', expand=1)

# set the number and size of columns and rows
for column in range(3):
    label_frame.columnconfigure(column, weight=400)
label_frame.rowconfigure(0, weight=100)
label_frame.rowconfigure(1, weight=100)

# create buttons
CreateButton(label_frame, 'Information Button', king_penguins_info, 0, 0)
CreateButton(label_frame, 'Warning Button', warning_message, 1, 0)
CreateButton(label_frame, 'Error Button', error_message, 2, 0)
CreateButton(label_frame, 'Guessing Button', guessing, 0, 1)
CreateButton(label_frame, 'Infinity Button', repeat, 1, 1)
CreateButton(label_frame, 'Three Buttons', three_buttons, 2, 1)

root.mainloop()  # display window
