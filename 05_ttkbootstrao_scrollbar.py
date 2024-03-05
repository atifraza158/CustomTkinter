import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter


window = ttk.Window(themename='solar')
window.title("Scrollbar")


scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill='both')

for i in range(100):
    ttk.Label(scroll_frame, text=f"Label: {i}").pack()
    ttk.Button(scroll_frame, text=f"Button: {i}").pack()


# ToastNotification
toast  = ToastNotification(title="Title", 
                           message="This is Message", 
                           duration=3000, bootstyle='warning', 
                           position=(50, 100, 'ne'))


button = ttk.Button(window, 
                    text="Show Toast", 
                    command=lambda: toast.show_toast())
button.pack(pady=20)
# Tooltip
ToolTip(button, text="This is a toast button", bootstyle='warning-inverse')


# Calender
calander = ttk.DateEntry(window)
calander.pack(pady = 30)

# Button to show selected date
button2 = ttk.Button(window, 
                     text="Show Date", 
                     command=lambda: print(calander.entry.get()))
button2.pack(pady=20)

# ProgressBar
progress_value = tk.IntVar(value=50)
progress = ttk.Floodgauge(window, 
                          text="Progress", 
                          variable = progress_value, 
                          mask="Progress: {}%")
progress.pack(fill='x')

slider = ttk.Scale(window, from_= 0, to=100, variable=progress_value)
slider.pack(pady=5)

# Meter Widget
meter = ttk.Meter(window, 
                  metersize=200, 
                  amountused=50, 
                  subtext="miles per hour", 
                  metertype='semi')
meter.pack()

window.mainloop()