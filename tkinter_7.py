# import modules
import tkinter as tk

# root window
root = tk.Tk()
root.title('Working with files')
root.geometry('600x500')
root.resizable(width=False, height=False)  # don't resize
# colors
color_1 = '#262626'
color_2 = '#999'

# widgets section
main_frame = tk.Frame()
# columns and rows
main_frame.columnconfigure(0, weight=300)
main_frame.columnconfigure(1, weight=300)
main_frame.rowconfigure(0, weight=400)
main_frame.rowconfigure(1, weight=100)

text = tk.Text(main_frame)
btn_file_open = tk.Button(main_frame, text='Open text file')
btn_file_record = tk.Button(main_frame, text='Save text file')

# widgets style
main_frame.config(bg=color_1)
text.config(wrap='word', font=('Arial', 10), bg=color_2, fg=color_1, border=0)
btn_file_open.config(font=('Arial', 14), border=0, bg=color_1, fg=color_2,
                     activebackground=color_2, activeforeground=color_1)
btn_file_record.config(font=('Arial', 14), border=0, bg=color_1, fg=color_2,
                       activebackground=color_2, activeforeground=color_1)

# placement of widgets
main_frame.pack(fill='both', expand=1)
text.grid(columnspan=2, row=0, sticky='news')
btn_file_open.grid(column=0, row=1, sticky='news')
btn_file_record.grid(column=1, row=1, sticky='news')

root.mainloop()  # display window
