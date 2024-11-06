# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Scrollable Notepad')
root.geometry('1300x925')

# widgets section
main_frame = tk.Frame()
text = tk.Text(main_frame)
scroll = tk.Scrollbar(main_frame, orient='vertical', command=text.yview)

# widgets style
text.config(font=("Comic Sans MS", 20), wrap='word', yscrollcommand=scroll.set)

# placement of widgets
main_frame.pack(fill='both', expand=1)
scroll.pack(side='right', fill='y')
text.pack(fill='both', expand=1)

root.mainloop()  # display window
