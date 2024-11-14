# import module
import tkinter as tk
from PIL import ImageTk, Image

# root window
root = tk.Tk()
root_wight = root.winfo_screenwidth()  # width user screen
root_height = root.winfo_screenheight()  # height user screen
root.geometry(f'{root_wight}x{root_height}')
root.attributes('-fullscreen', True)  # fullscreen mode
root.title('TERMINAL')
root.config(bg='black')
main_color = '#64da3d'

# split root window into columns
for i in range(6):  # 6 columns of same size
    root.columnconfigure(i, minsize=round(root_wight/6))
# row config
root.rowconfigure(0, minsize=100)
root.rowconfigure(1, minsize=root_height-100)

# widget section
title = tk.Label(root, text='BATTLE SIMULATION', bg='black', fg=main_color, font=('Fallout Regular', 40))
title.grid(column=1, columnspan=5, row=0, sticky='NEWS')

main_frame = tk.Label(root, bg=main_color)
main_frame.grid(columnspan=6, row=1, sticky='NEWS')

# split the main_frame into columns of the same size
for i in range(6):
    main_frame.columnconfigure(i, minsize=round(root_wight/6))
# split the main_frame into rows of the same size
for i in range(10):
    main_frame.rowconfigure(i, minsize=round((root_height - 100) / 10))

# data display terminal
terminal = tk.Frame(main_frame, bg='black')
terminal.grid(column=1, columnspan=5, rowspan=10, sticky='NEWS', pady=10)

# buttons for sidebar
simulation_btn = tk.Button(main_frame, text='SIMULATION')  # go to the simulation section
fight_btn = tk.Button(main_frame, text='TYPE OF BATTLE')  # go to choosing the type of battle
weapon_btn = tk.Button(main_frame, text='WEAPON')  # go to choosing the weapon
enemy_btn = tk.Button(main_frame, text='ENEMY')  # go to choosing the enemy
checks_btn = tk.Button(main_frame, text='CHECKS')  # go to the checks section
options_btn = tk.Button(main_frame, text='SETTING')  # go to the setting
close_btn = tk.Button(main_frame, text='EXIT', command=lambda: root.destroy())  # close window

# buttons style
simulation_btn.config(bg='black', fg=main_color, font=('Fallout Regular', 35), border=0, activebackground=main_color,
                      activeforeground='black')
fight_btn.config(bg='black', fg=main_color, font=('Fallout Regular', 35), border=0, activebackground=main_color,
                 activeforeground='black')
weapon_btn.config(bg='black', fg=main_color, font=('Fallout Regular', 35), border=0, activebackground=main_color,
                  activeforeground='black')
enemy_btn.config(bg='black', fg=main_color, font=('Fallout Regular', 35), border=0, activebackground=main_color,
                 activeforeground='black')
checks_btn.config(bg='black', fg=main_color, font=('Fallout Regular', 35), border=0, activebackground=main_color,
                  activeforeground='black')
options_btn.config(bg='black', fg=main_color, font=('Fallout Regular', 35), border=0, activebackground=main_color,
                   activeforeground='black')
close_btn.config(bg='black', fg=main_color, font=('Fallout Regular', 35), border=0, activebackground=main_color,
                 activeforeground='black')

# button layout
simulation_btn.grid(column=0, row=0, sticky='NEWS', padx=10, pady=(10, 5))
fight_btn.grid(column=0, row=1, sticky='NEWS', padx=10, pady=(5, 5))
weapon_btn.grid(column=0, row=2, sticky='NEWS', padx=10, pady=(5, 5))
enemy_btn.grid(column=0, row=3, sticky='NEWS', padx=10, pady=(5, 5))
checks_btn.grid(column=0, row=4, sticky='NEWS', padx=10, pady=(5, 5))
options_btn.grid(column=0, row=5, sticky='NEWS', padx=10, pady=(5, 5))
close_btn.grid(column=0, row=6, sticky='NEWS', padx=10, pady=(5, 10))

img = ImageTk.PhotoImage(Image.open("img/logo.png"))
panel = tk.Label(main_frame, image=img, bg='black')
panel.grid(column=0, row=7, rowspan=3, sticky='NEWS', padx=(0, 10))

root.mainloop()  # display window
