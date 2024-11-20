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

# figure
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

root.mainloop()  # display window
