# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Gallery')
root.geometry('800x600')
root.config(bg='#0d0d0d')

# widget section
# canvas
can = tk.Canvas(root, bg='#2b2b2b',  border=0, highlightthickness=0, width=800, height=550)
can.pack()

# button
open_btn = tk.Button(root, text='Open Photo', bg='#2b2b2b', font=('Arial', 17), bd=0, fg='#c9c9c9',
                     activebackground='#0d0d0d', activeforeground='#2b2b2b')
open_btn.pack(fill='both', expand=1, padx=5, pady=5)

root.mainloop()  # display window
