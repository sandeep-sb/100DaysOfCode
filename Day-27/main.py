import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)


# button click respond function
def button_clicked():
    my_label["text"] = input.get()


# Label
my_label = tkinter.Label(text="I am a Label.", font=("Arial", 24))
my_label.grid(row=0, column=0)

# Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

# New Button
new_button = tkinter.Button(text="new button")
new_button.grid(row=0, column=2)

#  Entry
input = tkinter.Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()
