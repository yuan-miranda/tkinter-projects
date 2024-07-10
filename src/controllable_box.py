import tkinter

SPEED       = 1
WIN_WIDTH   = 500
WIN_HEIGHT  = 300
IMG_WIDTH   = 10
IMG_HEIGHT  = 10
CURRENT_X   = 0
CURRENT_Y   = 0
WINDOW_BG   = "black"
IMG_PATH    = "../img/box.png"
WIN_TITLE   = "controllable.py"
FONT_STYLE  = "Consolas"
FONT_SIZE   = 8

def move_image(event):
    """Listens to the key event and move the image based on the key pressed."""
    global SPEED, CURRENT_X, CURRENT_Y

    # calculate the remaining pixel. Its been 9 months but i still dont know why subtracting 4 works.
    remaining_x = window.winfo_width() - CURRENT_X - IMG_WIDTH - 4
    remaining_y = window.winfo_height() - CURRENT_Y - IMG_HEIGHT - 4

    # increase or decrease the speed.
    if event.keysym == "w":
        SPEED += 1
    elif event.keysym == "s":
        SPEED -= 1

    # move the image based on the key pressed. Prevent the image from going out of the
    # window border by taking the minimum value between the speed and the remaining pixel.
    if event.keysym == "Up" and CURRENT_Y > 0:
        CURRENT_Y -= min(SPEED, CURRENT_Y)
    elif event.keysym == "Down" and remaining_y > 0:
        CURRENT_Y += min(SPEED, remaining_y)
    elif event.keysym == "Left" and CURRENT_X > 0:
        CURRENT_X -= min(SPEED, CURRENT_X)
    elif event.keysym == "Right" and remaining_x > 0:
        CURRENT_X += min(SPEED, remaining_x)
        
    image_label.place(x=CURRENT_X, y=CURRENT_Y)
    window.after(10, display_coordinates)

def display_coordinates():
    """Displays the current x, y, and speed on the window top left corner."""
    x_coordinate_text.config(text="[LEFT RIGHT] x: " + str(CURRENT_X))
    y_coordinate_text.config(text="[UP DOWN] y: " + str(CURRENT_Y))
    speed_text.config(text="[W S] speed: " + str(SPEED))

window = tkinter.Tk()
window.title(WIN_TITLE)
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
window.config(background=WINDOW_BG)

image = tkinter.PhotoImage(file=IMG_PATH, width=IMG_WIDTH, height=IMG_HEIGHT)
image_label = tkinter.Label(window, image=image)
image_label.place(x=0, y=0)

x_coordinate_text = tkinter.Label(window, text="[LEFT RIGHT] x: " + str(CURRENT_X), font=(FONT_STYLE, FONT_SIZE))
y_coordinate_text = tkinter.Label(window, text="[UP DOWN] y: " + str(CURRENT_Y), font=(FONT_STYLE, FONT_SIZE))
speed_text = tkinter.Label(window, text="[W S] speed: " + str(SPEED), font=(FONT_STYLE, FONT_SIZE))

x_coordinate_text.place(x=0, y=0)
y_coordinate_text.place(x=0, y=19)
speed_text.place(x=0, y=38)

window.bind("<KeyPress>", move_image)
window.mainloop()