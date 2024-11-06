# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Purple Guy')
root.geometry('400x500')
root.maxsize(400, 530)
root.minsize(400, 500)

# widget section
canvas = tk.Canvas(root, border=0, highlightthickness=0)
canvas.config(bg='black', width=400, height=530)
canvas.pack()

# purple guy
# head
canvas.create_rectangle(75, 35, 300, 75, fill='#6f4b95', width=0)
canvas.create_rectangle(50, 75, 350, 400, fill='#6f4b95', width=0)
canvas.create_rectangle(75, 400, 300, 450, fill='#6f4b95', width=0)

# eyes
canvas.create_rectangle(50, 200, 150, 250, fill='black', width=0)
canvas.create_rectangle(200, 200, 300, 250, fill='black', width=0)
canvas.create_rectangle(50, 175, 100, 250, fill='white', width=0)
canvas.create_rectangle(200, 175, 250, 250, fill='white', width=0)

# smile
canvas.create_rectangle(65, 320, 325, 340, fill='black', width=0)
canvas.create_rectangle(90, 325, 285, 425, fill='black', width=0)

# text
canvas.create_text(175, 510, text="I always come back", fill='#6f4b95', font=('Fixedsys', 20))

root.mainloop()  # display window
