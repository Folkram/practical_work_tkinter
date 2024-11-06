# import module
import tkinter as tk
from tkinter import messagebox as mb


# function section
def close(event):  # close window
    option = mb.askyesno('Выход', 'Вы действительно хотите выйти на рабочий стол?')
    if option:
        root.destroy()


# root window
root = tk.Tk()
root.geometry('800x600')
root.title('События')
root.bind('<Escape>', close)  # закрытие окна при нажатии esc

for column in range(2):
    root.columnconfigure(column, weight=round((800/2)))


class PostText:
    def __init__(self):  # constructor
        self.text = tk.Text(root)
        self.text.bind('<Control-Return>', self.post_1)  # send content to Ctrl+Enter
        self.text.grid(columnspan=2, row=0, sticky='news')

        self.btn_post = tk.Button(root, text='Send')
        self.btn_change_font = tk.Button(root, text='Change font')
        self.btn_post.bind('<Button-1>', self.post_1)
        self.btn_change_font.bind('<Button-1>', lambda e, f='Comic Sans MS': self.change_font(e, f))
        self.btn_post.grid(column=0, row=1, sticky='news')
        self.btn_change_font.grid(column=1, row=1, sticky='news')

    # method section
    def post(self, event):  # отправка текста
        option = mb.askyesno('Sending text', 'Are you sure you want to send a text?')
        if option:
            self.text.delete(1.0, 'end')

    # the delay allows you not to leave an extra empty line after pressing Ctrl+Enter
    def post_1(self, event):
        root.after(10, self.post, self.text)

    def change_font(self, event, font):
        self.text.config(font=(font, 10))


PostText()  # use constructor

root.mainloop()  # display window
