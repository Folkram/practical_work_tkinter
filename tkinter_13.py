# import module
import tkinter as tk


# functions section
def to_home():  # switch to home page
    # open home_frame
    home_frame.pack(fill='both', expand=1)


# root window
root = tk.Tk()
root.title('Result')
root.geometry('800x600')
fullscreen = False

# menu section
main_menu = tk.Menu(root)
root.config(menu=main_menu)

main_menu.add_command(label='Home', command=to_home)  # go to home page

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

# home page
# widgets section
home_frame = tk.Frame(root)
home_title = tk.Label(home_frame, text='Welcome!')
home_label_info = tk.Label(home_frame,
                           text='Here you can select one of the tasks in the top menu and look at its functionality')

# widgets style
home_title.config(font=('home_frame', 20))
home_label_info.config(font=('Arial', 11))

# widgets layout
home_frame.pack(fill='both', expand=1)
home_title.pack(fill='both', pady=(25, 0))
home_label_info.pack()

root.mainloop()
