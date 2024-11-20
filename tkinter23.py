# import module
import tkinter as tk
from tkinter import messagebox as mb


# function section
def get_time():
    global pol, gen, hol, mon, kar, shi
    inp = stop.get()

    if inp == '1' or inp == 'Polyclinic No. 4':
        display_time(pol)
    elif inp == '2' or inp == 'General Lizyukov Street':
        display_time(gen)
    elif inp == '3' or inp == 'Holzunov Street':
        display_time(hol)
    elif inp == '4' or inp == 'Monument of Glory':
        display_time(mon)
    elif inp == '5' or inp == 'Karpinski Street':
        display_time(kar)
    elif inp == '6' or inp == 'Shishkov Street':
        display_time(shi)
    else:
        mb.showerror('Input error', 'Incorrect data has been entered')


def display_time(buses):
    output.config(state='normal')
    output.delete(1.0, 'end')
    for i in buses:
        output.insert(1.0, f'Way by bus {i} will take {buses.get(i)} min.\n\n')

    min_time = min(buses.values())
    min_bus = get_key(buses, min_time)
    output.insert('end', f'Shortest way is by bus {min_bus} takes {min_time} min.')

    output.config(state='disabled')


def get_key(d, value):
    for i, j in d.items():
        if j == value:
            return i


def clear():
    output.config(state='normal')
    stop.delete(0, 'end')
    output.delete(1.0, 'end')
    output.config(state='disabled')


# root window
root = tk.Tk()
root.title('Bus Schedules')
root.geometry('1000x310')

# bus stops
pol = {38: 5, 125: 15, 90: 27, '5a': 4}
gen = {125: 25, 90: 17, '5a': 42}
hol = {38: 23, 90: 13}
mon = {38: 47, 125: 33, 90: 69}
kar = {125: 11}
shi = {38: 4, 125: 77, '5a': 19}

# widget section
main_frame = tk.Frame(root, bg='#454545')
main_frame.pack(fill='both', expand=1)

for column in range(7):  # set column size
    main_frame.columnconfigure(column, weight=round(1000/7))

# list of buses
tk.Label(main_frame, text='Bus/Stops', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 14)).grid(sticky='news', pady=(10, 5))

# bus stops
(tk.Label(main_frame, text='Polyclinic No. 4', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12))
 .grid(column=1, row=0, sticky='news', pady=(10, 5)))
(tk.Label(main_frame, text='General Lizyukov Street', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12))
 .grid(column=2, row=0, sticky='news', pady=(10, 5)))
(tk.Label(main_frame, text='Holzunov Street', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12))
 .grid(column=3, row=0, sticky='news', pady=(10, 5)))
(tk.Label(main_frame, text='Monument of Glory', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12))
 .grid(column=4, row=0, sticky='news', pady=(10, 5)))
(tk.Label(main_frame, text='Karpinski Street', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12))
 .grid(column=5, row=0, sticky='news', pady=(10, 5)))
(tk.Label(main_frame, text='Shishkov Street', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12))
 .grid(column=6, row=0, sticky='news', pady=(10, 5)))

# buses
tk.Label(main_frame, text='38', bg='#919191', font=('Arial', 13)).grid(column=0, row=1, sticky='news', pady=5)
(tk.Label(main_frame, text='125', bg='#919191', font=('Arial', 13))
 .grid(column=0, row=2, sticky='news', pady=(0, 5)))
tk.Label(main_frame, text='90', bg='#919191', font=('Arial', 13)).grid(column=0, row=3, sticky='news', pady=(0, 5))
tk.Label(main_frame, text='5a', bg='#919191', font=('Arial', 13)).grid(column=0, row=4, sticky='news')

# times
# Polyclinic No. 4
pol_38_time = tk.Label(main_frame, text='5', bg='#919191', font=('Arial', 11))
pol_38_time.grid(column=1, row=1, sticky='news', pady=5)
pol_125_time = tk.Label(main_frame, text='15', bg='#919191', font=('Arial', 12))
pol_125_time.grid(column=1, row=2, sticky='news', pady=(0, 5))
pol_90_time = tk.Label(main_frame, text='27', bg='#919191', font=('Arial', 12))
pol_90_time.grid(column=1, row=3, sticky='news', pady=(0, 5))
pol_5a_time = tk.Label(main_frame, text='4', bg='#919191', font=('Arial', 12))
pol_5a_time.grid(column=1, row=4, sticky='news')

# General Lizyukov Street
gen_38_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 11))
gen_38_time.grid(column=2, row=1, sticky='news', pady=5)
gen_125_time = tk.Label(main_frame, text='25', bg='#919191', font=('Arial', 12))
gen_125_time.grid(column=2, row=2, sticky='news', pady=(0, 5))
gen_90_time = tk.Label(main_frame, text='17', bg='#919191', font=('Arial', 12))
gen_90_time.grid(column=2, row=3, sticky='news', pady=(0, 5))
gen_5a_time = tk.Label(main_frame, text='42', bg='#919191', font=('Arial', 12))
gen_5a_time.grid(column=2, row=4, sticky='news')

# Holzunov Street
hol_38_time = tk.Label(main_frame, text='23', bg='#919191', font=('Arial', 11))
hol_38_time.grid(column=3, row=1, sticky='news', pady=5)
hol_125_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 12))
hol_125_time.grid(column=3, row=2, sticky='news', pady=(0, 5))
hol_90_time = tk.Label(main_frame, text='13', bg='#919191', font=('Arial', 12))
hol_90_time.grid(column=3, row=3, sticky='news', pady=(0, 5))
hol_5a_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 12))
hol_5a_time.grid(column=3, row=4, sticky='news')

# Monument of Glory
mon_38_time = tk.Label(main_frame, text='47', bg='#919191', font=('Arial', 11))
mon_38_time.grid(column=4, row=1, sticky='news', pady=5)
mon_125_time = tk.Label(main_frame, text='33', bg='#919191', font=('Arial', 12))
mon_125_time.grid(column=4, row=2, sticky='news', pady=(0, 5))
mon_90_time = tk.Label(main_frame, text='69', bg='#919191', font=('Arial', 12))
mon_90_time.grid(column=4, row=3, sticky='news', pady=(0, 5))
mon_5a_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 12))
mon_5a_time.grid(column=4, row=4, sticky='news')

# Karpinski Street
kar_38_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 11))
kar_38_time.grid(column=5, row=1, sticky='news', pady=5)
kar_125_time = tk.Label(main_frame, text='11', bg='#919191', font=('Arial', 12))
kar_125_time.grid(column=5, row=2, sticky='news', pady=(0, 5))
kar_90_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 12))
kar_90_time.grid(column=5, row=3, sticky='news', pady=(0, 5))
kar_5a_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 12))
kar_5a_time.grid(column=5, row=4, sticky='news')

# Shishkov Street
shi_38_time = tk.Label(main_frame, text='4', bg='#919191', font=('Arial', 11))
shi_38_time.grid(column=6, row=1, sticky='news', pady=5)
shi_125_time = tk.Label(main_frame, text='77', bg='#919191', font=('Arial', 12))
shi_125_time.grid(column=6, row=2, sticky='news', pady=(0, 5))
shi_90_time = tk.Label(main_frame, text='--', bg='#919191', font=('Arial', 12))
shi_90_time.grid(column=6, row=3, sticky='news', pady=(0, 5))
shi_5a_time = tk.Label(main_frame, text='19', bg='#919191', font=('Arial', 12))
shi_5a_time.grid(column=6, row=4, sticky='news')

# functional
# input
input_frame = tk.Frame(main_frame, bg='#2e2e2e')
input_frame.grid(columnspan=3, column=0, rowspan=5, row=5, sticky='news', padx=5, pady=(10, 0))

# content
tk.Label(input_frame, text='Select Stop', bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12)).pack(fill='both', expand=1)
stop = tk.Entry(input_frame, bg='#919191', bd=0, font=('Arial', 12))
stop.pack(fill='both', expand=1)
tk.Button(input_frame, text='Determine', bg='#2e2e2e', fg='#ebebeb', bd=0, font=('Arial', 12),
          activebackground='#919191', activeforeground='#2e2e2e', command=get_time).pack(fill='both', expand=1)
tk.Button(input_frame, text='Clear', bg='#2e2e2e', fg='#ebebeb', bd=0, font=('Arial', 12),
          activebackground='#919191', activeforeground='#2e2e2e', command=clear).pack(fill='both', expand=1)
(tk.Button(input_frame, text='Exit', bg='#2e2e2e', fg='#ebebeb', bd=0, font=('Arial', 12),
           activebackground='#919191', activeforeground='#2e2e2e', command=lambda: root.destroy())
 .pack(fill='both', expand=1))

# output
output_frame = tk.Frame(main_frame, bg='#2e2e2e')
output_frame.grid(columnspan=4, column=3, rowspan=5, row=5, sticky='news', padx=5, pady=(10, 0))
output = tk.Text(output_frame, bg='#2e2e2e', fg='#ebebeb', font=('Arial', 12), width=1, height=4, bd=0)
output.config(state='disabled')
output.pack(fill='both', expand=1)

root.mainloop()  # display window
