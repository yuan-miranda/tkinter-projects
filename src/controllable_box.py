import tkinter

# initial variable setup
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

# function to move the image
def move_image(event):
    global SPEED, CURRENT_X, CURRENT_Y
    
    # calculate the remaining pixel before it hits the window border.
    # also for some reason, subtracting 4 prevent the portion of the image from
    # going pass right and down border. I have no idea how but its there LMFAO

    remaining_x_movement = window.winfo_width() - CURRENT_X - IMG_WIDTH - 4
    remaining_y_movement = window.winfo_height() - CURRENT_Y - IMG_HEIGHT - 4

    # note: min(SPEED, CURRENT_Y) and min(SPEED, remaining_y_movement)
    # is used to adjust the pixel/speed remaining before hitting the border.

    # for example: 'speed = 10' and 'rem_x_move = 5', it would go with 'rem_x_move'
    # instead because 'speed' would make it go pass the window border.

    # in the conditions below, 'CURRENT_XY > 0' ensure that the image/box would not
    # go pass '0, 0', because 'CURRENT_XY < 0' is negative or beyond window border.

    # same with 'remaining_xy_movement > 0'. Anything pass the left and down border is
    # negative because 'remaining_xy_movement' calculates the remaining pixel before
    # hitting. And 'remaining_xy_movement == 0' means its on the edge of the border.

    if event.keysym == "w":                                     # increase the speed
        SPEED += 1
    elif event.keysym == "s":                                   # decrease the speed
        SPEED -= 1

    if event.keysym == "Up" and CURRENT_Y > 0:                  # move up
        CURRENT_Y -= min(SPEED, CURRENT_Y)
    elif event.keysym == "Down" and remaining_y_movement > 0:   # move down
        CURRENT_Y += min(SPEED, remaining_y_movement)
    elif event.keysym == "Left" and CURRENT_X > 0:              # move left
        CURRENT_X -= min(SPEED, CURRENT_X)
    elif event.keysym == "Right" and remaining_x_movement > 0:  # move right
        CURRENT_X += min(SPEED, remaining_x_movement)
        
    image_label.place(x=CURRENT_X, y=CURRENT_Y)
    window.after(10, print_coordinate)

# function that render the current XY and speed on the screen
def print_coordinate():
    x_coordinate_text.config(text="[LEFT RIGHT] x: " + str(CURRENT_X))
    y_coordinate_text.config(text="[UP DOWN] y: " + str(CURRENT_Y))
    speed_text.config(text="[W S] speed: " + str(SPEED))

window = tkinter.Tk()
window.title(WIN_TITLE)
window.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
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