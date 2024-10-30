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

# greeting
# frames section
greeting_frame = tk.Frame(root, bg=color1)
btn_frame = tk.Frame(root, bg=color1)
# placement of frames
greeting_frame.pack(fill='both', expand=1)
btn_frame.pack(fill='both', side='bottom')

# content
text_of_greeting = ('Welcome to a little penguin quiz. You will be asked three questions to assess your knowledge in '
                    'this area. To continue, click the button below.')
MyLabel(greeting_frame, 'Welcome!', color1, color2, ('Arial', 28, 'bold'), 350,
        'center', 0, (75, 50))  # heading
MyLabel(greeting_frame, text_of_greeting, color1, color2, ('Arial', 16, 'italic'), 340,
        'left',  5, 25)  # greeting
# buttons
MyButton(btn_frame, 'Next >>', color2, color1, 0, color1, color2, ('Arial', 14),
         5, 0, lambda: print('go to the next frame'))  # to next frame
MyButton(btn_frame, '<< Exit', color2, color1, 0, color1, color2, ('Arial', 14),
         5, 5, lambda: root.destroy())  # close window

# first question
# frame section
first_question_frame = tk.Frame(root, bg=color1)
btn_fq_frame = tk.Frame(root, bg=color1)

# content
# label section
fq_text = 'How many species are there in the penguin group?'
label_title_fq = MyLabel(first_question_frame, 'Question №1', color1, color2, ('Arial', 28, 'bold'),
                         350, 'left', 0, (50, 25))
label_fq = MyLabel(first_question_frame, fq_text, color1, color2, ('Arial', 16, 'italic'), 340,
                   'left',  5, (0, 35))
# radiobutton section
fq_options = tk.StringVar()  # common variable for first question
fq_option_1 = MyRadiobutton(first_question_frame, '876', fq_options, 1)
fq_option_2 = MyRadiobutton(first_question_frame, '23', fq_options, 2)
fq_option_3 = MyRadiobutton(first_question_frame, '17', fq_options, 3)
# button section
MyButton(btn_fq_frame, 'Next >>', color2, color1, 0, color1, color2, ('Arial', 14),
                       5, 0, lambda: print('Go to the next frame'))  # to next frame
MyButton(btn_fq_frame, '<< Back', color2, color1, 0, color1, color2, ('Arial', 14),
         5, 5, lambda: print('Go to the previous frame'))  # to previous frame

# second question
# frame section
second_question_frame = tk.Frame(root, bg=color1)
btn_sq_frame = tk.Frame(root, bg=color1)

# content
# label section
sq_text = 'How long have penguins been around?'
MyLabel(second_question_frame, 'Question №2', color1, color2, ('Arial', 28, 'bold'),
        350, 'left', 0, (50, 25))
MyLabel(second_question_frame, sq_text, color1, color2, ('Arial', 16, 'italic'), 340,
        'left',  5, (0, 60))
# radiobutton section
sq_options = tk.StringVar()  # common variable for second question
sq_option_1 = MyRadiobutton(second_question_frame, '50 million years ago', sq_options, 1)
sq_option_2 = MyRadiobutton(second_question_frame, '60 million years ago', sq_options, 2)
sq_option_3 = MyRadiobutton(second_question_frame, '30 million years ago', sq_options, 3)
# button section
MyButton(btn_sq_frame, 'Next >>', color2, color1, 0, color1, color2, ('Arial', 14),
         5, 0, lambda: print('Go to the next frame'))  # to the next frame
MyButton(btn_sq_frame, '<< Back', color2, color1, 0, color1, color2, ('Arial', 14),
         5, 5, lambda: print('Go to the previous frame'))  # to the previous frame

# third question
# frame section
third_question_frame = tk.Frame(root, bg=color1)
btn_tq_frame = tk.Frame(root, bg=color1)

# content
# label section
text_tq = 'In which hemisphere do penguins live?'
MyLabel(third_question_frame, 'Question №3', color1, color2, ('Arial', 28, 'bold'),
        350, 'left', 0, (50, 25))
MyLabel(third_question_frame, text_tq, color1, color2, ('Arial', 16, 'italic'), 340,
        'left',  5, (0, 35))
# radiobutton section
tq_options = tk.StringVar()  # common variable for third question
tq_option_1 = MyRadiobutton(third_question_frame, 'North', tq_options, 1)
tq_option_2 = MyRadiobutton(third_question_frame, 'Both', tq_options, 2)
tq_option_3 = MyRadiobutton(third_question_frame, 'South', tq_options, 3)
# button section
MyButton(btn_tq_frame, 'Show result >>', color2, color1, 0, color1, color2,  ('Arial', 14),
         5, 0, lambda: print('Show the result'))  # show the result
MyButton(btn_tq_frame, '<< Back', color2, color1, 0, color1, color2, ('Arial', 14),
         5, 5, lambda: print('Go to the previous frame'))  # to the previous frame

root.mainloop()  # display window
