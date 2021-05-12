from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as data:
        data.write(f"{website}  |  {email}  |  {password}\n")
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20
              )
canvas = Canvas(width=200, height=190)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=photo_image)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus_set()
email_entry = Entry(width=35)
email_entry.insert(index=0, string="sandeep@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = Entry(width=21, show="*")
password_entry.grid(row=3, column=1, sticky="EW")

# Button
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(row=3, column=2, sticky="EW")
add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
