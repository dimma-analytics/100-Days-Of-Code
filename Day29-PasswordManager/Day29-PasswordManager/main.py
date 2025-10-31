from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range (nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_textbox.insert(0, password)
    pyperclip.copy(password)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():

    website = website_textbox.get()
    email = user_textbox.get()
    password = password_textbox.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}\nPassword: {password}\nIs it ok to save?")
        
        if is_ok:
            file_name = "p_manager.txt"
            with open(file_name, "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_textbox.delete(0, END)
                password_textbox.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#Website Entry textbox
website_textbox = Entry(width=53)
website_textbox.focus()
website_textbox.grid(column=1, row=1, columnspan=2)

#Email/Username Label
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

#Email/Username Entry textbox
user_textbox = Entry(width=53)
user_textbox.insert(0, "contact@gmail.com")
user_textbox.grid(column=1, row=2, columnspan=2)

#Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Password Entry textbox
password_textbox = Entry(width=33)
password_textbox.grid(column=1, row=3)

#Generate Password Buttons
password_button = Button(text="Generate Password", command=generate_password, width=15)
password_button.grid(column=2, row=3)

#Add Button
add_button = Button(text="Add", command=save_to_file, width=44)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()