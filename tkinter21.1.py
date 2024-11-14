# import module
import tkinter as tk

# root window
root = tk.Tk()
root.geometry('800x600')
root.title('Set the size')

# widget section
title = tk.Label(root, text='Set the size of the text field', font=('Arial', 17), )
width_label = tk.Label(root, text='Width', font=('Arial', 12))
height_label = tk.Label(root, text='Height', font=('Arial', 12))
ent1 = tk.Entry(root, width=4, font=('Arial', 12))
ent2 = tk.Entry(root, width=4, font=('Arial', 12))
btn = tk.Button(root, text='Set', font=('Arial', 12))
text = tk.Text(root)

# set columns size
for column in range(10):
    root.columnconfigure(column, weight=int(800/10))

# widget layout
title.grid(columnspan=10, sticky='news')
width_label.grid(column=0, row=1, sticky='w')
height_label.grid(column=0, row=2, sticky='w')
ent1.grid(column=0, row=1, sticky='e')
ent2.grid(column=0, row=2, sticky='e')
btn.grid(column=1, row=1, rowspan=2, sticky='news', padx=10)
text.grid(columnspan=10, sticky='news')

root.mainloop()  # display window
