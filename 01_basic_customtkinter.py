import customtkinter as ctk

window = ctk.CTk()
window.title("Basic Custom Tkinter")
window.geometry('600x400')

label1 = ctk.CTkLabel(window, text="Hello World...", fg_color='skyblue', text_color='black', corner_radius=21)
label1.pack()
window.mainloop()