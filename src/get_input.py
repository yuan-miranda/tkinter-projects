import tkinter

WIN_TITLE = "get_input.py"

def print_entry():
    """Prints the text in the entry."""
    print(entry.get())

window = tkinter.Tk()
window.title(WIN_TITLE)

entry = tkinter.Entry(window)
entry.pack(side="left")

button = tkinter.Button(window, text="print", command=print_entry)
button.pack(side="right")

window.mainloop()