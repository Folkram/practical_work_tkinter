# import module
import tkinter as tk


# function section
def show_pressed(event, button, color):  # change label text
    event_label['text'] = f'Detect {button}'  # event name
    event_label['fg'] = color  # font color


# root window
root = tk.Tk()
root.title('Events')
root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()
root_font = ('Arial', round(root_width/50), 'bold')
root.geometry(f'{root_width}x{root_height}')
root.overrideredirect(True)
root.config(bg='black')

# widget section
# button to close window
close_btn = tk.Button(root, text='EXIT', font=('Arial', round(root_width/150), 'bold'), bg='black', fg='white',
                      border=0, command=lambda: root.destroy())
close_btn.pack(anchor='ne')

# label to display pressed button or other event
event_label = tk.Label(root, text='Track events', font=root_font, bg='black', fg='white')
event_label.pack(fill='both', expand=1)

# events
event_label.bind('<Motion>', lambda e, b='Mouse motion', c='red': show_pressed(e, b, c))
event_label.bind('<Button-1>', lambda e, b='LMB', c='yellow': show_pressed(e, b, c))
event_label.bind('<Button-2>', lambda e, b='MMB', c='blue': show_pressed(e, b, c))
event_label.bind('<Button-3>', lambda e, b='RMB', c='green': show_pressed(e, b, c))
root.bind('f', lambda e, b='F', c='gray': show_pressed(e, b, c))
root.bind('1987', lambda e, b='FNaF', c='purple': show_pressed(e, b, c))
root.bind('<Return>', lambda e, b='Enter', c='pink': show_pressed(e, b, c))
root.bind('<Escape>', lambda e, b='Esc', c='orange': show_pressed(e, b, c))
root.bind('<Control-Return>', lambda e, b='Ctrl+Enter', c='lime': show_pressed(e, b, c))
root.bind('<Control-Alt-Return>', lambda e, b='Ctrl+Alt+Enter', c='cyan': show_pressed(e, b, c))

root.mainloop()  # display window
