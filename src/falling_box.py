import tkinter

# initial variable setup
SPEED       = 1
WIN_WIDTH   = 500
WIN_HEIGHT  = 300
IMG_WIDTH   = 10
IMG_HEIGHT  = 10
CURRENT_X   = 10
CURRENT_Y   = 0
WINDOW_BG   = "black"
IMG_PATH    = "../img/box.png"
WIN_TITLE   = "falling_box.py"

# function to move the image
def move_image():
    global CURRENT_Y

    if CURRENT_Y + IMG_HEIGHT != WIN_HEIGHT:    # make the image fall till it hits the border
        CURRENT_Y += SPEED

    image_label.place(y=CURRENT_Y)
    window.after(10, move_image)

window = tkinter.Tk()
window.title(WIN_TITLE)
window.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT)) # window.geometry("200x200") optionally
window.config(background=WINDOW_BG)

image = tkinter.PhotoImage(file=IMG_PATH, width=IMG_WIDTH, height=IMG_HEIGHT)
image_label = tkinter.Label(window, image=image)
image_label.place(x=CURRENT_X, y=CURRENT_Y)

move_image()
window.mainloop()
