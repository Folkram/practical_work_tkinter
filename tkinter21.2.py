# import module
import tkinter as tk
import os


# function section
def get_directory_list(directory):
    directories = []
    for name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, name)):
            directories.append(name)
    return directories


def display_content(event):
    content_list.delete(0, 'end')
    for con in os.listdir(os.path.join('x:/', dir_list.get(dir_list.curselection()))):
        content_list.insert('end', con)


def delete():
    os.rmdir(os.path.join('x:/', dir_list.get(dir_list.curselection())))


# root window
root = tk.Tk()
root.geometry('800x500')
root.title('File Explorer')
root.resizable(False, False)
root.config(bg='#242424')

# set column size
root.columnconfigure(0, weight=200)
root.columnconfigure(1, weight=200)
root.columnconfigure(2, weight=200)
root.columnconfigure(3, weight=200)

# widget section
dir_title = tk.Label(root, text='Folder list', font=('Arial', 14), bg='#242424', fg='#d1d1d1')
content_title = tk.Label(root, text='Folder content', font=('Arial', 14), bg='#242424', fg='#d1d1d1')
dir_list = tk.Listbox(root, height=23, font=('Arial', 12), border=0, bg='#404040', highlightthickness=0, fg='#d1d1d1',
                      selectbackground='#242424', activestyle='none')
content_list = tk.Listbox(root, height=23, font=('Arial', 12), border=0, bg='#404040', highlightthickness=0,
                          fg='#d1d1d1', selectbackground='#242424', activestyle='none')

# insert values
for i in get_directory_list('x:/'):
    dir_list.insert('end', i)

# button section
open_btn = tk.Button(root, text='Open', font=('Arial', 14), border=0, bg='#242424', fg='#d1d1d1',
                     activebackground='#404040')
delete_btn = tk.Button(root, text='Delete', font=('Arial', 14), border=0, bg='#242424', fg='#d1d1d1',
                       activebackground='#404040', command=delete)
copy_btn = tk.Button(root, text='Copy', font=('Arial', 14), border=0, bg='#242424', fg='#d1d1d1',
                     activebackground='#404040')
update_btn = tk.Button(root, text='Update', font=('Arial', 14), border=0, bg='#242424', fg='#d1d1d1',
                       activebackground='#404040')

# bind function
dir_list.bind('<Double-Button-1>', display_content)
open_btn.bind('<Button-1>', display_content)

# widget layout
dir_title.grid(columnspan=2, row=0, sticky='news')
content_title.grid(column=2, columnspan=2, row=0, sticky='news')
dir_list.grid(columnspan=2, row=1, sticky='news', padx=(0, 5))
content_list.grid(column=2, columnspan=2, row=1, sticky='news', padx=(5, 0))
open_btn.grid(column=0, row=2, sticky='news')
delete_btn.grid(column=1, row=2, sticky='news')
copy_btn.grid(column=2, row=2, sticky='news')
update_btn.grid(column=3, row=2, sticky='news')

root.mainloop()  # display window
