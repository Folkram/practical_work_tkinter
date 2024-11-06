# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Tanks')
root.geometry('800x600')

field = tk.Canvas(root, border=0, highlightthickness=0, bg='#383838', width=800, height=600)
field.focus_set()
field.pack()

# tank
body = field.create_rectangle(375, 275, 425, 325, fill='green', width=5, outline='#042b00', tags='tank')
barrel = field.create_rectangle(397.5, 275, 402.5, 230, fill='#042b00', tags='tank')
left_track = field.create_rectangle(360, 270, 372, 330, width=2, outline='black', fill='#212121', tags='tank')
right_track = field.create_rectangle(428, 270, 440, 330, width=2, outline='black', fill='#212121', tags='tank')

root.mainloop()  # display window
