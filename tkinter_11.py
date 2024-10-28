# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Quiz about penguins')
root.geometry('350x500')
root.resizable(width=False, height=False)
# colors
color1 = '#7df0ff'
color2 = '#00063d'
color3 = '#010d7a'

# greeting frame
# widgets section
greeting_frame = tk.Frame(root)
btn_frame = tk.Frame(root)

# widgets style
greeting_frame.config(bg=color1)
btn_frame.config(bg=color1)

# placement of widgets
greeting_frame.pack(fill='both', expand=1)
btn_frame.pack(fill='both', side='bottom')

root.mainloop()  # display window
