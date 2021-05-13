import random
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = pass_numbers + pass_letters + pass_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {email}\n "
                                                                f"Password: {password}\n Is it ok to save?")
        if is_okay:
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
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky="EW")
add_button = Button(width=36, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
