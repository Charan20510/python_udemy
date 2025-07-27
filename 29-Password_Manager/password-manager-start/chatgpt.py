from tkinter import *
from tkinter import messagebox

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#f4f4f4")

# Fonts and colors
FONT_NAME = "Calibri"
LABEL_FONT = (FONT_NAME, 12)
ENTRY_FONT = (FONT_NAME, 11)
BUTTON_FONT = (FONT_NAME, 10, "bold")
RED_COLOR = "#d94f4f"
BTN_COLOR = "#e76f51"

# Canvas for logo
canvas = Canvas(height=200, width=200, bg="#f4f4f4", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")  # Make sure this file exists
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=LABEL_FONT, bg="#f4f4f4")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:", font=LABEL_FONT, bg="#f4f4f4")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:", font=LABEL_FONT, bg="#f4f4f4")
password_label.grid(row=3, column=0, sticky="e")

# Entry Fields
website_entry = Entry(width=35, font=ENTRY_FONT)
website_entry.grid(row=1, column=1, columnspan=2, pady=4)
website_entry.focus()

email_entry = Entry(width=35, font=ENTRY_FONT)
email_entry.grid(row=2, column=1, columnspan=2, pady=4)
email_entry.insert(0, "example@email.com")  # default value

password_entry = Entry(width=21, font=ENTRY_FONT)
password_entry.grid(row=3, column=1, pady=4)

# Buttons
generate_password_button = Button(
    text="Generate Password",
    font=BUTTON_FONT,
    bg=BTN_COLOR,
    fg="white",
    highlightthickness=0
)
generate_password_button.grid(row=3, column=2)

add_button = Button(
    text="Add",
    width=36,
    font=BUTTON_FONT,
    bg=RED_COLOR,
    fg="white",
    highlightthickness=0
)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
