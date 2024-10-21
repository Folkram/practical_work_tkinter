# import moduls
import tkinter as tk


class NewPosition:
    # create constructor
    def __init__(self, win_name, win_size, first_side, second_side, third_side, fourth_side):
        # root window
        self.root = tk.Tk()
        self.root.title(win_name)
        self.root.geometry(win_size)

        # widgets section
        self.first_item = tk.Label(self.root, text='1')
        self.second_item = tk.Label(self.root, text='2')
        self.third_item = tk.Label(self.root, text='3')
        self.fourth_item = tk.Label(self.root, text='4')

        # widgets style
        self.first_item.config(font=('Arial', 24, 'bold'), bg='gray', width=8, height=3)
        self.second_item.config(font=('Arial', 24, 'bold'), bg='gray', width=8, height=3)
        self.third_item.config(font=('Arial', 24, 'bold'), bg='gray', width=8, height=3)
        self.fourth_item.config(font=('Arial', 24, 'bold'), bg='gray', width=8, height=3)

        # placement of widgets
        self.first_item.pack(side=first_side, padx=5, pady=5)
        self.second_item.pack(side=second_side, padx=5, pady=5)
        self.third_item.pack(side=third_side, padx=5, pady=5)
        self.fourth_item.pack(side=fourth_side, padx=5, pady=5)

        self.root.mainloop()  # launch main loop


# create instances with different widget positions
NewPosition('position 1', '250x510', 'top', 'top', 'top', 'top')
NewPosition('position 2', '250x510', 'bottom', 'bottom', 'bottom',
            'bottom')
NewPosition('position 3', '675x200', 'left', 'left', 'left',
            'left')
NewPosition('position 4', '675x200', 'right', 'right', 'right',
            'right')
NewPosition('position 5', '500x275', 'left', 'right', 'top',
            'bottom')
NewPosition('position 6', '350x400', 'top', 'bottom', 'right',
            'left')
