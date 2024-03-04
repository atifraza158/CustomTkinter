import customtkinter as ctk

window = ctk.CTk()
window.title("Basic Custom Tkinter")
window.geometry('600x400')

label1 = ctk.CTkLabel(window, text="Hello World...", fg_color=('skyblue', 'lightgreen'), text_color='black', corner_radius=21)
label1.pack()

button = ctk.CTkButton(window, text="My Button", fg_color='#ff0', text_color='black', hover_color='#AA0', command=lambda: ctk.set_appearance_mode('light'))
button.pack()

frame = ctk.CTkFrame(window)
frame.pack()

# Slider
slider = ctk.CTkSlider(frame)
slider.pack(pady = 10)

# Switch
switch = ctk.CTkSwitch(frame, text="Bulb", button_color=('orange', 'lightgreen'), progress_color=('blue', 'pink'), border_color = ('blue', 'green'), fg_color = ('purple', 'purple'), button_hover_color=('orange', 'orange'), switch_width=70, switch_height=30, corner_radius=0)
switch.pack(padx = 20, pady = 20)


window.mainloop()