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

root.mainloop()  # display window
