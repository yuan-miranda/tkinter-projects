import tkinter

# function to print the content of the entry box
def print_entry():
    print(entry.get())

window = tkinter.Tk()
window.title("get_input.py")

entry = tkinter.Entry(window)
entry.pack(side="left")

button = tkinter.Button(window, text="print", command=print_entry)
button.pack(side="right")

window.mainloop()