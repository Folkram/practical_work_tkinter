# import module
import tkinter as tk


# function section
def fullscreen_switch():
    global fullscreen
    fullscreen = not fullscreen
    root.overrideredirect(fullscreen)


def switch_theme():
    global dark_theme
    dark_theme = not dark_theme
    if dark_theme:
        root.config(bg='#212121')
    else:
        root.config(bg='#f2f2f2')


# root window
root = tk.Tk()
root_width = root.winfo_screenwidth()  # width user screen
root_height = root.winfo_screenheight()  # height user screen
root.geometry(f'{root_width}x{root_height}')
root.resizable(False, False)  # not resize
root.title('Program')
fullscreen = False
dark_theme = False

# widget section
main_menu = tk.Menu(root)  # создание основного меню
root.config(menu=main_menu)  # присваивание меню корневому окну

# add items to the main menu
info_menu = tk.Menu(main_menu, tearoff=0)  # submenu
# submenu for submenu
help_menu = tk.Menu(info_menu, tearoff=0)
# add items to a submenu for a submenu
help_menu.add_command(label='Local Help')
help_menu.add_command(label='On website')
# add items to the submenu
info_menu.add_cascade(label='Help', menu=help_menu)
info_menu.add_command(label='About program')
main_menu.add_cascade(label='Help', menu=info_menu)  # add an item from the submenu

config_menu = tk.Menu(main_menu, tearoff=0)  # submenu
# add items to a submenu
config_menu.add_command(label='Switch theme', command=switch_theme)
config_menu.add_command(label='Fullscreen mode', command=fullscreen_switch)
config_menu.add_separator()  # add separator
config_menu.add_command(label='Exit', command=lambda: root.destroy())
main_menu.add_cascade(label='Setting', menu=config_menu)  # add an item from the submenu

root.mainloop()  # show window
