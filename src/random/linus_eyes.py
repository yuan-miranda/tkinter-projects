import tkinter as tk

WIN_WIDTH   = 660
WIN_HEIGHT  = 250
IMG_PATH   = "../../img/linus_eyes.png"
WIN_TITLE   = "linus_eyes.py"

window  = tk.Tk()
window.title(WIN_TITLE)
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
window.resizable(False, False)

image = tk.PhotoImage(file=IMG_PATH)
label = tk.Label(window, image=image).pack()

tk.mainloop()