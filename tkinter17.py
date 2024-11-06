# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Tanks')
root.geometry('800x600')

field = tk.Canvas(root, border=0, highlightthickness=0, bg='black', width=800, height=600)
field.pack()

root.mainloop()  # display window
