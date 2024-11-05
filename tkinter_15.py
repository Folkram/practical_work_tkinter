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

root.mainloop()  # display window
