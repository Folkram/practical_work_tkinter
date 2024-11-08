# import module
import tkinter as tk

# root window
root = tk.Tk()
root_wight = root.winfo_screenwidth()  # width user screen
root_height = root.winfo_screenheight()  # height user screen
root.geometry(f'{root_wight}x{root_height}')
root.resizable(False, False)
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

root.mainloop()  # display window
