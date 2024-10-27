# import modules
import tkinter as tk
from tkinter import messagebox as mb


# function section
def show_translate():  # display messagebox with translate
    if listbox.curselection() == ():
        mb.showerror('Error', 'None of the options are selected')
    else:
        translate = options_translate[listbox.curselection()[0]]  # get translation for current word
        mb.showinfo(f'{listbox.get(listbox.curselection()[0])}', f'Word translation: {translate}')


# root window
root = tk.Tk()
root.title('Translate')
root.geometry('280x325')

# widgets section
listbox = tk.Listbox(root)
scroll = tk.Scrollbar(root, orient='vertical', command=listbox.yview)
btn_translate = tk.Button(root, text='Translate', command=show_translate)

# widgets style
listbox.config(yscrollcommand=scroll.set, font=('Arial', 18), width=20)
btn_translate.config(font=('Arial', 16))

# placement of widgets
listbox.grid()
scroll.grid(column=1, row=0, sticky='news')
btn_translate.grid(columnspan=2, row=1, sticky='news')

# options for listbox
options = ['artichoke', 'eggplant', 'bobs', 'ginger', 'marrow', 'cabbage', 'cauliflower', 'broccoli', 'brussels sprout',
           'apricot', 'avocado', 'pine apple', 'orange', 'watermelon', 'banana', 'blackberry']
# translate for options
options_translate = ['артишок', 'баклажан', 'бобы', 'имбирь', 'кабачок', 'капуста', 'цветная капуста', 'брокколи',
                     'брюссельская капуста', 'абрикос', 'авокадо', 'ананас', 'апельсин', 'арбуз', 'банан', 'ежевика']
# insert options into listbox
i = 0  # counter
for option in options:
    listbox.insert(i, option)
    i += 1

root.mainloop()  # display window
