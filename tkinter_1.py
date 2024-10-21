# import module
import tkinter as tk

# root window
root = tk.Tk()  # create a root window
root.title('Приветствие')  # window name
root.geometry("1920x1080")  # set the window size ("widthxheight")

# widgets section
# create two labels
label_1 = tk.Label(root, text='Информационные технологии и программирование')
label_2 = tk.Label(root, text='ВТСТ')
# labels style
label_1.config(font=('Arial', 16, 'bold'))
label_2.config(font=('Arial', 24, 'bold'))
# placement of labels
label_1.pack()
label_2.pack(pady=(24, 0))  # padding top = 24px

root.mainloop()  # execute tkinter
