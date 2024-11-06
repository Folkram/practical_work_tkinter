# import moduls
import tkinter as tk


class LabelLayout:
    # create constructor
    def __init__(self, win_name, fill, expand, anchor):
        # root window
        self.root = tk.Tk()
        self.root.title(win_name)
        self.root.geometry('500x400+0+0')

        # widgets section
        label = tk.Label(text='ВТСТ')

        # widgets style
        label.config(font=('Arial', 26, 'bold'), fg='white', bg='black')

        # placement of widgets
        label.pack(fill=fill, expand=expand, anchor=anchor)

        self.root.mainloop()  # display window


# create instances with different label layout
LabelLayout('layout 1', 'none', 0, 'center')
LabelLayout('layout 2', 'x', 0, 'center')
LabelLayout('layout 3', 'y', 1, 'center')
LabelLayout('layout 4', 'both', 1, 'center')
LabelLayout('layout 5.1', 'none', 0, 'nw')
LabelLayout('layout 5.2', 'none', 0, 'ne')
LabelLayout('layout 5.3', 'none', 1, 'sw')
LabelLayout('layout 5.4', 'none', 1, 'se')
LabelLayout('layout 5.5', 'none', 1, 'center')
