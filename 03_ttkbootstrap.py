import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# Website for ttkbootstrap themes
# https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/

# just define the theme name
window = ttk.Window(themename='solar')
window.title("ttkbootstrap Theme")
window.geometry('600x400')

label = ttk.Label(window, text='Label 1', background='skyblue')
label.pack(expand=True, fill='both')

button = ttk.Button(window, text='Button 1', bootstyle = 'danger-outline')
button.pack(expand=True)

button2 = ttk.Button(window, text='Button 1')
button2.pack(expand=True)

window.mainloop()