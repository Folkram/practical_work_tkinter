# import module
import tkinter as tk


# function section
def change_bg_color():
    if btn_change_bg_color['text'] == 'Light theme':
        root.config(bg='#1c1c1c')
        btn_change_bg_color['text'] = 'Dark theme'
    else:
        root.config(bg='white')
        btn_change_bg_color['text'] = 'Light theme'


# root window
root = tk.Tk()
root.geometry('500x300')

# widgets section
btn_change_bg_color = tk.Button(root, text='Light theme', command=change_bg_color)
btn_close = tk.Button(root, text='Close window', command=lambda: root.destroy())  # close window

# set the number and size of columns and rows
for i in range(3):
    root.columnconfigure(i, weight=round(500/3))
    root.rowconfigure(i, weight=round(300/3))

# widgets style
btn_change_bg_color.config(bg='gray', width=15, font=('Arial', 16, 'bold'))
btn_close.config(bg='gray', width=12)

# placement of widgets
btn_change_bg_color.grid(column=1, row=1, sticky='ew')
btn_close.grid(column=1, row=2, sticky='nwe')

root.mainloop()  # display window
