from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    is_yes = messagebox.askyesno(title=website, message=f"Confirm\n Email:{email}\n Password:{password}\n Are you sure?")
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Oops!", message="Fill empty box")
    elif is_yes:
        with open('data.txt', 'a') as file:
            file.write(f'{website} | {email} | {password}\n')

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# ---------------------------- labels ------------------------------- #

# label for website text
website_text = Label(text="Website: ")
website_text.grid(column=0, row=1)

# label for email/username text
email_text = Label(text="Email/Username: ")
email_text.grid(column=0, row=2)

# label for password text
password_text = Label(text="Password: ")
password_text.grid(column=0, row=3)
# ---------------------------- Entries ------------------------------- #
# entry for website
website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# entry for email
email_entry = Entry(width=50)
email_entry.insert(0, "nadir@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, pady=10)

# entry for password
password_entry = Entry(width=32)

password_entry.grid(column=1, row=3, pady=10)

# ---------------------------- Buttons ------------------------------- #
# button for generating password
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# button for add
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()


