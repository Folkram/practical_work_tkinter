# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Purple Guy')
root.geometry('400x500')
root.resizable(False, False)

# widget section
canvas = tk.Canvas(root)
canvas.config(bg='black', width=400, height=500)
canvas.pack()

root.mainloop()  # display window
