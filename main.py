import json
import pyperclip
import string
from random import choice, sample, randint
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
    end_password = "".join(passwd)

    password.delete(0, END)
    password.insert(0, end_password)
    pyperclip.copy(end_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website.get(): {
            "email": user_name.get(),
            "password": password.get(),
        }
    }

    if website.get() != "" and password.get() != "" and user_name.get() != "":
        is_ok = messagebox.askokcancel(
            title="Confirm", message=f""
                                     f"There are the details entered:"
                                     f"\nEmail: {user_name.get()}"
                                     f"\nWebsite: {website.get()}"
                                     f"\nPassword: {password.get()}"
                                     f"\nIs that ok?")
        if is_ok is True:
            try:
                with open("data.json", "r") as data:
                    data_value = json.load(data)
                    data_value.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("data.json", "w") as data:
                    json.dump(data_value, data, indent=4)
            finally:
                website.delete(0, END)
                password.delete(0, END)
                messagebox.showinfo(title="Success", message="Your password was added")
    else:
        messagebox.showinfo(title="Opss", message="Do not leave empty fields")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_value:
            data = json.load(data_value)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        try:
            messagebox.showinfo(title=website.get(),
                                message=f"{data[website.get()]["email"]}\n{data[website.get()]["password"]}")
        except KeyError:
            messagebox.showinfo(title="Error", message="No details for the website exist")


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
website = Entry(width=26)
user_name = Entry(width=46)
user_name.insert(0, "default@gmail.com")
password = Entry(width=26)

# buttons
generate_password_button = Button(text="Generate Password", width=18, command=generate_pass)
add_button = Button(text="Add", width=45, command=save)
search_button = Button(text="Search", width=18, command=find_password)

# grids
website_label.grid(column=0, row=1, sticky="e")
password_label.grid(column=0, row=3, sticky="e")
user_name_label.grid(column=0, row=2, sticky="e")

website.grid(column=1, row=1, columnspan=2, sticky="w")
user_name.grid(column=1, row=2, columnspan=2)
password.grid(column=1, row=3, sticky="w", columnspan=2)

search_button.grid(column=1, row=1, sticky="e", columnspan=2)
generate_password_button.grid(column=1, row=3, sticky="e", columnspan=2)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
