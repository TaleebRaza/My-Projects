# Importing Packages
import json

from pyperclip import copy
from tkinter import PhotoImage
from customtkinter import *
from tkinter import messagebox
from Password_generator import create_password

# ------------------ Constants ------------------ #
BUFF = "#EAAC8B"
LIGHT_CORAL = "#E56B6F"
YELLOW = "#ffd60a"
VIOLET = "#6D597A"
RICH_BLACK = "#070A0E"
TRANSPARENT = "transparent"
WIDTH = 700; HEIGHT = 500
FONT = "consolas"

# ------------------ Global Variable (if any) ------------------ #
password = ''

# ------------------ helper Functions ------------------ #
def hide_password():
    global password
    password_entry.delete(first_index=0, last_index=END)
    for letter in range(len(password)):
        password_entry.insert(index=0, string="•")
    hide_button.configure(command=show_password, text="Show")

def show_password():
    password_entry.delete(first_index=0, last_index=END)
    for letter in range(len(password)):
        password_entry.insert(index=END, string=password[letter])
    hide_button.configure(command=hide_password, text="Hide")

def focus_next(event):
    current_widget = event.widget.master

    if current_widget == website_entry:
        email_username_entry.focus_set()
    elif current_widget == email_username_entry:
        password_entry.focus_set()
    elif current_widget == password_entry:
        generate_button.focus_set()
    return "break"

# ------------------ Search Function ------------------ #
def search_data():
    try:
        with open("Passwords.json", mode="r") as file:
            password_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="File Not Found", message="We Couldn't Find Any File With Your Passwords\nThis can happen due to\n1. File Name Being Changed\n2. File Being Deleted\n3. File Being Empty.")
    else:
        website_to_search = website_entry.get().lower()
        if website_to_search in password_data:
            messagebox.showinfo(title="Data Found", message=f"Email: {password_data[website_to_search]["email"]}\nPassword: {password_data[website_to_search]["password"]}\n\n(password copied to clipboard)")
            copy(password_data[website_to_search]["password"])
        if website_to_search not in password_data:
            messagebox.showinfo(title="Data Not Found", message="There was no data linked with that website")


# ------------------ Password Generator ------------------ #
def generate_password():
    global password
    password_entry.delete(first_index=0, last_index=END)
    password = create_password()
    password = ''.join(password)
    password_entry.insert(index=0, string=password)
    copy(password) # Copy password on the clipboard
    hide_button.configure(command=hide_password, text="Hide")

# ------------------ Save Password ------------------ #
def write_to_file(website:str, name_email:str, password:str):
    data_to_write = {website.lower(): {
        "email": name_email,
        "password": password
    }}

    try:
        with open("Passwords.json", mode="r") as file:
            new_data = json.load(file)
            new_data.update(data_to_write)

        with open("Passwords.json", mode="w") as file:
            json.dump(new_data, file, indent=4)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("Passwords.json", mode="w") as file:
            json.dump(data_to_write, file, indent=4)


def save_password():
    global password
    website = website_entry.get()
    email_username = email_username_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0: # don't let user save if nothing is typed
        filed_to_fill = ""
        if len(website) == 0:
            filed_to_fill = "Website"
        elif len(email_username) == 0:
            filed_to_fill = "Email/Username "
        elif len(password) == 0:
            filed_to_fill = "Password "

        messagebox.showinfo(title="No Data Found", message=f"Please Enter {filed_to_fill} To Save")

    else:
        # ask the user to confirm data saving
        add_data = messagebox.askokcancel(title=website, message=f"Email/Username: {email_username}\nPassword: {password}\nPress OK to add.")

        if add_data: # if user confirms
            write_to_file(website=website, name_email=email_username, password=password)
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)
            password = ''
        else:
            messagebox.showinfo(title="Operation Cancelled", message="No Data Was Added In The Password File")



# ------------------ UI Setup ------------------ #

# Creating the main app
app = CTk()

# Setting up dimensions and color theme
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)
set_appearance_mode("dark")
app.title("Password Manager")
app.config(bg=RICH_BLACK, padx=20, pady=20)

# Image canvas
lock_image = PhotoImage(file="My Pass.png")

image_canvas = CTkCanvas(master=app, bg=RICH_BLACK, width=300, height=300, borderwidth=0, highlightthickness=0)
image_canvas.create_image(150, 150, image=lock_image)
image_canvas.grid(column=1, row=0)

# Creating required labels
website_label = CTkLabel(master=app, text_color=YELLOW, bg_color=RICH_BLACK, text="Website: ", font=(FONT, 20, "bold"), pady=5)
email_username_label = CTkLabel(master=app, text_color=YELLOW, bg_color=RICH_BLACK, text="Email/Username: ", font=(FONT, 20, "bold"), pady=5)
password_label = CTkLabel(master=app, text_color=YELLOW, bg_color=RICH_BLACK, text="Password", font=(FONT, 20, "bold"), pady=5)

# placing the labels
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Creating required entries
website_entry = CTkEntry(master=app, width=295, text_color=YELLOW, font=(FONT, 15, "bold"), bg_color=RICH_BLACK, fg_color=TRANSPARENT, border_color=VIOLET, placeholder_text= "Enter Any Website", placeholder_text_color=VIOLET)
email_username_entry = CTkEntry(master=app, width=450, text_color=YELLOW, font=(FONT, 15, "bold"), bg_color=RICH_BLACK, fg_color=TRANSPARENT, border_color=VIOLET, placeholder_text= "Enter Your Email/Username", placeholder_text_color=VIOLET)
password_entry = CTkEntry(master=app, width=300, text_color=YELLOW, font=(FONT, 15, "bold"), bg_color=RICH_BLACK, fg_color=TRANSPARENT, border_color=VIOLET, placeholder_text="Press Generate", placeholder_text_color=VIOLET)

# Placing the entries
website_entry.grid(column=1, row=1)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Bind Enter key to move to the next field
website_entry.bind(sequence="<Return>", command=focus_next)
email_username_entry.bind(sequence="<Return>", command=focus_next)
password_entry.bind(sequence="<Return>", command=focus_next)

# Creating required buttons
generate_button = CTkButton(master=app, bg_color=RICH_BLACK, fg_color=TRANSPARENT, border_color=LIGHT_CORAL, hover_color=YELLOW, text_color=LIGHT_CORAL, text="Generate Password", border_width=1, font=(FONT, 15, "bold"), command=generate_password)
add_button = CTkButton(master=app, width=300, bg_color=RICH_BLACK, fg_color=TRANSPARENT, border_color=VIOLET, hover_color=LIGHT_CORAL, text_color=YELLOW, text="Add", border_width=1, font=(FONT, 15, "bold"), command=save_password)
hide_button = CTkButton(master=app, width=150, bg_color=RICH_BLACK, fg_color=TRANSPARENT, border_color=LIGHT_CORAL, hover_color=LIGHT_CORAL, text_color=YELLOW, text="Hide", border_width=1, font=(FONT, 15, "bold"), command=hide_password)
search_button = CTkButton(master=app, width=150, bg_color=RICH_BLACK, fg_color=TRANSPARENT, border_color=LIGHT_CORAL, hover_color=LIGHT_CORAL, text_color=YELLOW, text="Search", border_width=1, font=(FONT, 15, "bold"), command=search_data)

# Placing the buttons
add_button.grid(column=1, row=4)
generate_button.grid(column=2, row=3)
hide_button.grid(column=2, row=4)
search_button.grid(column=2, row=1)

# Main app loop
app.mainloop()