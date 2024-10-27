# import module
import tkinter as tk

# root window
root = tk.Tk()
root.title('Translate')
root.geometry('280x325')

# widgets section
listbox = tk.Listbox(root)
scroll = tk.Scrollbar(root, orient='vertical', command=listbox.yview)
btn_translate = tk.Button(root, text='Translate')

# widgets style
listbox.config(yscrollcommand=scroll.set, font=('Arial', 18), width=20)
btn_translate.config(font=('Arial', 16))

# placement of widgets
listbox.grid()
scroll.grid(column=1, row=0, sticky='news')
btn_translate.grid(columnspan=2, row=1, sticky='news')

root.mainloop()  # display window
