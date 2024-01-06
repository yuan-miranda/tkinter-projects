import tkinter as tk

window  = tk.Tk()
window.title("linus eyes lol")
window.geometry("660x250")
window.resizable(False, False)

image = tk.PhotoImage(file="../../img/linus.png")
label = tk.Label(window, image=image).pack()

tk.mainloop()