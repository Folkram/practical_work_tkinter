# import module
import tkinter as tk


# function section
def aim(event):
    field.delete('aim')
    field.create_line(event.x, event.y+15, event.x, event.y-15, width=5, fill='black', tags='aim')
    field.create_line(event.x-15, event.y, event.x+15, event.y, width=5, fill='black', tags='aim')


def shoot(event):  # shooting at tank
    # tank's coordination
    tank_x1 = field.coords('tank')[0]
    tank_y1 = field.coords('tank')[1]
    tank_x2 = field.coords('tank')[2]
    tank_y2 = field.coords('tank')[3]

    # aim's coordination
    aim_x1 = field.coords('aim')[0]
    aim_y1 = field.coords('aim')[1]

    if tank_x1 < aim_x1 < tank_x2 and tank_y1 < aim_y1 < tank_y2:  # if tank's and aim's coordination match
        text = field.create_text(aim_x1 + 10, aim_y1 - 15, text='BOOM', font=('Fixedsys', 17), fill='orange')
        root.after(100, lambda e: field.delete('tank'), field)  # delete tank
        root.after(500, lambda e: field.delete(text), field)  # display text 'BOOM' for 5 second
    else:  # if tank's and aim's coordination don't match
        text = field.create_text(aim_x1 + 10, aim_y1 - 15, text='miss', font=('Fixedsys', 17))
        root.after(300, lambda e: field.delete(text), field)  # display text 'miss' for 3 second


# root window
root = tk.Tk()
root.title('Tanks')
root.geometry('800x600')
root.config(cursor="none")  # remove cursor

field = tk.Canvas(root, border=0, highlightthickness=0, bg='#383838', width=800, height=600)
field.focus_set()
field.pack()

# tank
body = field.create_rectangle(375, 275, 425, 325, fill='green', width=5, outline='#042b00', tags='tank')
barrel = field.create_rectangle(397.5, 275, 402.5, 230, fill='#042b00', tags='tank')
left_track = field.create_rectangle(360, 270, 372, 330, width=2, outline='black', fill='#212121', tags='tank')
right_track = field.create_rectangle(428, 270, 440, 330, width=2, outline='black', fill='#212121', tags='tank')

# tank movement
field.bind('<Up>', lambda e: field.move('tank', 0, -10))
field.bind('<Down>', lambda e: field.move('tank', 0, 10))
field.bind('<Left>', lambda e: field.move('tank', -10, 0))
field.bind('<Right>', lambda e: field.move('tank', 10, 0))

# aim
field.bind('<Motion>', aim)

field.tag_bind('aim', '<Button-1>', shoot)  # shooting function

root.mainloop()  # display window
