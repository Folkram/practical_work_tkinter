# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Diagrams')
root.geometry('800x600')

# widget section
can = tk.Canvas(root, width=800, height=600, border=0, highlightthickness=0)
can.pack()

# diagram
# columns
can.create_rectangle(75, 500, 175, 150, fill='blue', width=3, outline='#032773')  # first column
can.create_rectangle(225, 500, 325, 350, fill='yellow', width=3, outline='#736b03')  # second column
can.create_rectangle(375, 500, 475, 250, fill='green', width=3, outline='#147303')  # third column
can.create_rectangle(525, 500, 625, 450, fill='red', width=3, outline='#730303')  # fourth column

root.mainloop()  # display window
