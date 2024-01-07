import tkinter as tk
from PIL import Image, ImageTk

width = 300
height = 100

window  = tk.Tk()
window.title("piston sheep")
window.geometry(f"{width}x{height}")
window.resizable(False, False)

window.piston_img = Image.open("../../img/piston.png")
piston_img = window.piston_img.resize((window.piston_img.size[0] // 4, window.piston_img.size[1] // 4))
window.piston_img = ImageTk.PhotoImage(piston_img)
piston_img = tk.Label(window, image=window.piston_img)
piston_img.place(x=0, y=0)

window.piston_pushed_img = Image.open("../../img/piston_pushed.png")
piston_pushed_img = window.piston_pushed_img.resize((window.piston_pushed_img.size[0] // 4, window.piston_pushed_img.size[1] // 4))
window.piston_pushed_img = ImageTk.PhotoImage(piston_pushed_img)
piston_pushed_img = tk.Label(window, image=window.piston_pushed_img)
piston_pushed_img.place(x=0, y=0)
piston_pushed_img.place_forget()

def show_piston():
    piston_img.place(x=0, y=0)
    piston_pushed_img.place_forget()

def key_press(event):
    if event.keysym == "space":
        piston_img.place_forget()
        piston_pushed_img.place(x=0, y=0)

        window.after(500, show_piston)

window.bind("<Key-space>", key_press)
window.mainloop()