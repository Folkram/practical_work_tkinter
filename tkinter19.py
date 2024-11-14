# import module
import tkinter as tk
from PIL import ImageTk, Image

# root window
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open('img/boykisser.png'))  # img for label
root_width = img.width()  # img width
root_height = img.height()  # img height
root.title('Gallery')
root.geometry(f'{root_width}x{root_height}')
root.config(bg='#0d0d0d')

# widget section
# label
label = tk.Label(root, image=img)
label.pack()

root.mainloop()  # display window
