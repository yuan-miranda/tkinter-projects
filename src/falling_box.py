import tkinter

SPEED = 1
WIDTH = 25
HEIGHT = 25
IMAGE_PATH = "../img/box.png"

# function to move the image
def move_image():
    global current_y

    if current_y + image.height() != window.winfo_height():
        image_label.place(y=current_y)
        current_y += SPEED

        window.after(10, move_image)

window = tkinter.Tk()
window.title("falling_box.py")
window.geometry("500x1000")
window.config(background="black")

image = tkinter.PhotoImage(file=IMAGE_PATH, width=WIDTH, height=HEIGHT)
image_label = tkinter.Label(window, image=image)

current_y = 0

move_image()
window.mainloop()
