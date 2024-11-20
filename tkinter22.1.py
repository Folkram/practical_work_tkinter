# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Diagrams')
root.geometry('700x600')

# widget section
can = tk.Canvas(root, width=800, height=600, border=0, highlightthickness=0)
can.pack()

# diagram
# columns
can.create_rectangle(75, 500, 175, 150, fill='blue', width=3, outline='#032773')  # first column
can.create_rectangle(225, 500, 325, 350, fill='yellow', width=3, outline='#736b03')  # second column
can.create_rectangle(375, 500, 475, 250, fill='green', width=3, outline='#147303')  # third column
can.create_rectangle(525, 500, 625, 450, fill='red', width=3, outline='#730303')  # fourth column

# column value
can.create_text(125, 520, text='350', font=('Arial', 15))  # first column value
can.create_text(275, 520, text='150', font=('Arial', 15))  # second column value
can.create_text(425, 520, text='250', font=('Arial', 15))  # third column value
can.create_text(575, 520, text='50', font=('Arial', 15))  # fourth column value

# scale
can.create_line(0, 500, 700, 500, width=3)  # bottom line
can.create_line(50, 500, 50, 100, width=3)  # scale
can.create_line(50, 450, 55, 450, width=3)  # mark 50
can.create_line(50, 400, 60, 400, width=3)  # mark 100
can.create_line(50, 350, 55, 350, width=3)  # mark 150
can.create_line(50, 300, 60, 300, width=3)  # mark 200
can.create_line(50, 250, 55, 250, width=3)  # mark 250
can.create_line(50, 200, 60, 200, width=3)  # mark 300
can.create_line(50, 150, 55, 150, width=3)  # mark 350
can.create_line(50, 100, 60, 100, width=3)  # mark 400

# mark value
can.create_text(25, 450, text='50', font=('Arial', 13))
can.create_text(25, 400, text='100', font=('Arial', 13))
can.create_text(25, 350, text='150', font=('Arial', 13))
can.create_text(25, 300, text='200', font=('Arial', 13))
can.create_text(25, 250, text='250', font=('Arial', 13))
can.create_text(25, 200, text='300', font=('Arial', 13))
can.create_text(25, 150, text='350', font=('Arial', 13))
can.create_text(25, 100, text='400', font=('Arial', 13))

root.mainloop()  # display window
