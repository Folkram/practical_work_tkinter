# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Animation 2.0')
root.geometry('800x600')

# widget section
# canvas
can = tk.Canvas(root, bg='black', border=0, highlightthickness=0, width=800, height=600)
can.pack()

root.mainloop()  # display window
