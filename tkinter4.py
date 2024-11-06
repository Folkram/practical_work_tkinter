# import module
import tkinter as tk


# functions section
def counter():
    global i  # import counter
    i += 1

    if i == 1:
        label['text'] = f'Button pressed {i} time'
    elif i == 50:
        label['text'] = f'Button pressed {i} time'
        btn['text'] = 'Dont stop!'
    elif i >= 100:
        label['text'] = 'Go touch some grass'
        btn['text'] = 'X_X'
        btn['state'] = 'disable'
    else:
        label['text'] = f'Button pressed {i} times'


i = 0  # counter

# root window
root = tk.Tk()
root.title('Clicker')
root.geometry('500x400')

# widgets section
frame = tk.Frame(root)
label = tk.Label(frame, text='Button is not pressed')
btn = tk.Button(frame, text='Click!', command=counter)

# widgets style
label.config(font=('Arial', 20))
btn.config(bg='gray', activebackground='#bbbbbb', font=('Arial', 14), border=0)

# placement of widgets
frame.pack(expand=1)
label.pack()
btn.pack(fill='x')

root.mainloop()  # display window
