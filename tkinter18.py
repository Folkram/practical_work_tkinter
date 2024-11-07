# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Animation')
root_width = root.winfo_screenwidth()  # window width
root_height = root.winfo_screenwidth()  # window height
root.geometry(f'{root_width}x{root_height}')
root.attributes("-fullscreen", True)  # fullscreen

root.mainloop()  # display window
