from tkinter import * 
from tkinter import messagebox
import pyperclip
import json
import random
from random import shuffle, choice, randint

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END) # Clear existing password before inserting new one
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ------------------ SAVE PASSWORD ------------------------- #
def button_smashed():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)
        
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


#------------------Find Password----------#
def find_password():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")           
    else:
        if website_entry.get() in data:
                email = data[website_entry.get()]["email"]
                password = data[website_entry.get()]["password"]
                messagebox.showinfo(title=website_entry.get(),message=f"Email :{email}\n Password : {password} ")
        else:
            messagebox.showinfo(title="Error" , message=f"No details for {website_entry.get()} Exists!! ")
# --------------------------- UI SETUP --------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, columnspan=2)

# LABELS
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ENTRIES
website_entry = Entry(width=33) # Adjusted width to match layout
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=52) # Spans across both columns
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "chinmayn621@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="w")

# BUTTONS
search_button = Button(text="Search", width=14, pady=0,command=find_password)
search_button.grid(row=1, column=2, sticky="w")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=44, command=button_smashed)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
