# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Form')
root.geometry('350x400')
# default values
def_font_size = 10
def_width = 40
def_height = 10

# widgets section
main_frame = tk.Frame(root)
label_main = tk.Label(main_frame, text='Form')
label_text_about_yourself = tk.Label(main_frame, text='Tell about yourself')
text_about_yourself = tk.Text(main_frame)

# widgets style
label_main.config(font=('Arial', round(def_font_size*2.5), 'bold'))
label_text_about_yourself.config(font=('Arial', round(def_font_size*1.2), 'italic'))
text_about_yourself.config(width=def_width, height=def_height, wrap='word', font=('Arial', def_font_size))

# placement of widgets
main_frame.pack(expand=1)
label_main.grid(columnspan=2, row=0, pady=10)
label_text_about_yourself.grid(columnspan=2, row=1, sticky='w')
text_about_yourself.grid(columnspan=2, row=2, pady=(0, 10))

root.mainloop()  # display window
