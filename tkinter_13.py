# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Result')
root.geometry('800x600')
fullscreen = False

# menu section
main_menu = tk.Menu(root)
root.config(menu=main_menu)

main_menu.add_command(label='Home')  # go to home page

# settings
options = tk.Menu(root, tearoff=0)
resolution = tk.Menu(root, tearoff=0)
resolution.add_command(label='800x600')
resolution.add_command(label='1280x720')
resolution.add_command(label='1920x1080')
options.add_cascade(label='Change resolution')
options.add_command(label='Fullscreen')
options.add_separator()
options.add_command(label='Exit', command=lambda: root.destroy())
main_menu.add_cascade(label='Settings', menu=options)

# list of tasks
tasks = tk.Menu(root, tearoff=0)
main_menu.add_cascade(label='Tasks', menu=tasks)
tasks.add_command(label='Task №1')
tasks.add_command(label='Task №2',)
tasks.add_command(label='Task №3')
tasks.add_command(label='Task №4')
tasks.add_command(label='Task №5')
tasks.add_command(label='Task №6')

root.mainloop()
