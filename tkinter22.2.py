# import module
import tkinter as tk
import random as rm


# function section
def move_figure():  # move figure diagonally
    global vx, vy  # get speed

    x1, y1, x2, y2 = can.coords('figure')  # figure coords

    # check if the edges have been reached
    if x1 <= 0 or x2 >= 800:  # right or left edges
        for i in range(2, 8):  # iterating through all parts of figure
            color = f'#{rm.randint(0, 9)}{rm.randint(0, 9)}{rm.randint(0, 9)}'  # random color
            can.itemconfig(i, fill=color)  # set color
        vx *= -1
    if y1 <= 0 or y2 >= 600:  # top or bottom edges
        for i in range(2, 8):
            color = f'#{rm.randint(0, 9)}{rm.randint(0, 9)}{rm.randint(0, 9)}'  # random color
            can.itemconfig(i, fill=color)   # set color
        vy *= -1

    can.move('figure', vx, vy)
    can.after(10, move_figure)


# root window
root = tk.Tk()
root.title('Animation 2.0')
root.geometry('800x600')

# widget section
# canvas
can = tk.Canvas(root, bg='black', border=0, highlightthickness=0, width=800, height=600)
can.pack()

# figure
# speed
vx = 5
vy = 5

# size
fig_width = 800/6
fig_height = 600/7

# parts (figure consists of six parts)
can.create_rectangle(0, 0, fig_width, fig_height, width=0, tags='figure')  # hitbox
can.create_rectangle(0, 0, fig_width/6, fig_height, width=0, fill='gray', tags='figure')  # part 1
can.create_rectangle(fig_width/6, 0, fig_width*2/6, fig_height, width=0, fill='gray', tags='figure')  # part 2
can.create_rectangle(fig_width*2/6, 0, fig_width*3/6, fig_height, width=0, fill='gray', tags='figure')  # part 3
can.create_rectangle(fig_width*3/6, 0, fig_width*4/6, fig_height, width=0, fill='gray', tags='figure')  # part 4
can.create_rectangle(fig_width*4/6, 0, fig_width*5/6, fig_height, width=0, fill='gray', tags='figure')  # part 5
can.create_rectangle(fig_width*5/6, 0, fig_width, fig_height, width=0, fill='gray', tags='figure')  # part 6
# figure text
can.create_text(67, 40, text='no signal', font=('Fixedsys', 17, 'bold'), fill='black', justify='center', tags='figure')

can.move('figure', 10, 10)
move_figure()

root.mainloop()  # display window
