from random import choice, sample, randint
import string
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_letters = [choice(letters) for _ in range(randint(0, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    passwd = password_letters + password_symbols + password_numbers
    passwd = sample(passwd, len(passwd))

    password.delete(0, END)
    password.insert(0, "".join(passwd))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if website.get() != "" and password.get() != "" and user_name.get() != "":
        is_ok = messagebox.askokcancel(
            title="Confirm", message=f""
                                     f"There are the details entered:"
                                     f"\nEmail: {user_name.get()}"
                                     f"\nWebsite: {website.get()}"
                                     f"\nPassword: {password.get()}"
                                     f"\nIs that ok?")
        if is_ok is True:
            with open("data.txt", "a") as data:
                data.write(f"{website.get()} | {user_name.get()} | {password.get()}\n")
            website.delete(0, END)
            password.delete(0, END)
            messagebox.showinfo(title="Success", message="Your password was added")
    else:
        messagebox.showinfo(title="Opss", message="Do not leave empty fields")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
picture = PhotoImage(file="logo.png")
window.iconphoto(False, picture)
canvas = Canvas(width=200, height=200, highlightthickness=FALSE)
canvas.create_image(100, 100, image=picture)
canvas.grid(column=1, row=0, sticky="w")

# labes
website_label = Label(text="Website:")
user_name_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# entris
website = Entry(width=45)
user_name = Entry(width=45)
user_name.insert(0, "default@gmail.com")
password = Entry(width=26)

# buttons
generate_password_button = Button(text="Generate Password", command=generate_pass)
add_button = Button(text="Add", width=38, command=save)

# grids
website_label.grid(column=0, row=1, sticky="e")
password_label.grid(column=0, row=3, sticky="e")
user_name_label.grid(column=0, row=2, sticky="e")

website.grid(column=1, row=1, columnspan=2)
user_name.grid(column=1, row=2, columnspan=2)
password.grid(column=1, row=3, sticky="w", columnspan=2)

generate_password_button.grid(column=1, row=3, sticky="e", columnspan=2)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
