# import module
import tkinter as tk


# function section
def movement():  # movement of figure in straight line
    can.move('figure', 5, 0)
    if can.coords('figure')[2] < root_width:
        root.after(10, movement)
    else:  # if shape reaches border of window
        can.delete('figure')  # delete figure


# root window
root = tk.Tk()
root.title('Animation')
root_width = root.winfo_screenwidth()  # window width
root_height = root.winfo_screenwidth()  # window height
root.geometry(f'{root_width}x{root_height}')
root.attributes("-fullscreen", True)  # fullscreen

# widget section
can = tk.Canvas(root, bg='black', border=0, highlightthickness=0, width=root_width, height=root_height)
can.pack()

# figure
# size
fig_width = root_width/9
fig_height = root_width/12

# parts (figure consists of six parts)
can.create_rectangle(0, 0, fig_width/6, fig_height, width=0, fill='lime', tags='figure')  # part 1
can.create_rectangle(fig_width/6, 0, fig_width*2/6, fig_height, width=0, fill='yellow', tags='figure')  # part 2
can.create_rectangle(fig_width*2/6, 0, fig_width*3/6, fig_height, width=0, fill='red', tags='figure')  # part 3
can.create_rectangle(fig_width*3/6, 0, fig_width*4/6, fig_height, width=0, fill='blue', tags='figure')  # part 4
can.create_rectangle(fig_width*4/6, 0, fig_width*5/6, fig_height, width=0, fill='purple', tags='figure')  # part 5
can.create_rectangle(fig_width*5/6, 0, fig_width, fig_height, width=0, fill='pink', tags='figure')  # part 6

root.mainloop()  # display window
