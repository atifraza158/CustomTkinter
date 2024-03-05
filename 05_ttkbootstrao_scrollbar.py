import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame

window = ttk.Window()
window.title("Scrollbar")


scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill='both')

for i in range(100):
    ttk.Label(scroll_frame, text=f"Label: {i}").pack()
    ttk.Button(scroll_frame, text=f"Button: {i}").pack()


window.mainloop()