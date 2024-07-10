import tkinter as tk
from PIL import Image, ImageTk

WIN_WIDTH = 300
WIN_HEIGHT = 100
IMG_PATH = "../../img/piston.png"
IMG_PUSHED_PATH = "../../img/piston_pushed.png"
WIN_TITLE = "piston_sheep.py"

def display_piston():
    """Displays the piston image."""
    piston_img.place(x=0, y=0)
    piston_pushed_img.place_forget()

def key_press(event):
    """Listens to the key event and push the piston when space is pressed."""
    if event.keysym == "space":
        push_piston()

def push_piston():
    """Replace the piston image with the pushed piston image."""
    piston_img.place_forget()
    piston_pushed_img.place(x=0, y=0)
    window.after(100, display_piston)

window  = tk.Tk()
window.title(WIN_TITLE)
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
window.resizable(False, False)

window.piston_img = Image.open(IMG_PATH)
piston_img = window.piston_img.resize((window.piston_img.size[0] // 4, window.piston_img.size[1] // 4))
window.piston_img = ImageTk.PhotoImage(piston_img)
piston_img = tk.Label(window, image=window.piston_img)
piston_img.place(x=0, y=0)

window.piston_pushed_img = Image.open(IMG_PUSHED_PATH)
piston_pushed_img = window.piston_pushed_img.resize((window.piston_pushed_img.size[0] // 4, window.piston_pushed_img.size[1] // 4))
window.piston_pushed_img = ImageTk.PhotoImage(piston_pushed_img)
piston_pushed_img = tk.Label(window, image=window.piston_pushed_img)
piston_pushed_img.place(x=0, y=0)
piston_pushed_img.place_forget()

window.bind("<Key-space>", key_press)
window.mainloop()