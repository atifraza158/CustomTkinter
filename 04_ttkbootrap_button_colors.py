import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename='solar')
window.title("All Color Buttons")
# window.geometry('700x400')

button1 = ttk.Button(window, text="Button 1", bootstyle = 'primary')
button1.pack(side='left', padx=10, pady=20)

button1 = ttk.Button(window, text="Button 2", bootstyle = 'success')
button1.pack(side='left', padx=10, pady=20)

button1 = ttk.Button(window, text="Button 3", bootstyle = ('warning', 'outline'))
button1.pack(side='left', padx=10, pady=20)

button1 = ttk.Button(window, text="Button 4", bootstyle = 'info')
button1.pack(side='left', padx=10, pady=20)

button1 = ttk.Button(window, text="Button 5", bootstyle = ('secondary', 'outline'))
button1.pack(side='left', padx=10, pady=20)

button1 = ttk.Button(window, text="Button 6", bootstyle = 'dark-outline')
button1.pack(side='left', padx=10, pady=20)

button1 = ttk.Button(window, text="Button 7", bootstyle = 'light')
button1.pack(side='left', padx=10, pady=20)

button1 = ttk.Button(window, text="Button 8", bootstyle = 'danger')
button1.pack(side='left', padx=10, pady=20)

# Text Widget with ttkbootstrap
text = ttk.Text(window)
text.pack(side='bottom')


window.mainloop()