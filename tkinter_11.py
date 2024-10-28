# import module
import tkinter as tk


# class section
class MyLabel:  # create label
    def __init__(self, m_root, m_text, m_bg, m_fg, m_font, m_wraplength, m_justify, m_padx, m_pady):
        self.label = tk.Label(m_root, text=m_text, bg=m_bg, fg=m_fg, wraplength=m_wraplength, justify=m_justify,
                              font=m_font)
        self.label.pack(padx=m_padx, pady=m_pady)


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
