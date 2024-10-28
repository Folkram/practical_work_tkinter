# import module
import tkinter as tk


# class section
class MyLabel:  # create label
    def __init__(self, m_root, m_text, m_bg, m_fg, m_font, m_wraplength, m_justify, m_padx, m_pady):
        self.label = tk.Label(m_root, text=m_text, bg=m_bg, fg=m_fg, wraplength=m_wraplength, justify=m_justify,
                              font=m_font)
        self.label.pack(padx=m_padx, pady=m_pady)


class MyButton:  # create button
    def __init__(self, m_root, m_text, m_bg, m_fg, m_border, m_activebg, m_activefg, m_font, m_padx, m_pady, m_command):
        self.btn = tk.Button(m_root, text=m_text, bg=m_bg, fg=m_fg, border=m_border, activebackground=m_activebg,
                             activeforeground=m_activefg, font=m_font, command=m_command)
        self.btn.pack(fill='both', padx=m_padx, pady=m_pady)


class MyRadiobutton:  # create radiobutton
    def __init__(self, m_root, m_text, m_variable, m_value, m_indicatoron=False, m_bg='#00063d', m_fg='#7df0ff',
                 m_border=0, m_activebg='#010d7a', m_activefg='#7df0ff', m_selectcolor='#010d7a',
                 m_font=('Arial', 16, 'italic'), m_padx=5, m_pady=(5, 0)):
        self.radiobtn = tk.Radiobutton(m_root, text=m_text, variable=m_variable, value=m_value,
                                       indicatoron=m_indicatoron, bg=m_bg, fg=m_fg, border=m_border,
                                       activebackground=m_activebg, activeforeground=m_activefg,
                                       selectcolor=m_selectcolor, font=m_font)
        self.radiobtn.pack(fill='both', padx=m_padx, pady=m_pady)


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
