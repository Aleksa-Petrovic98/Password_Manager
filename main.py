
#Password Generator Project
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Define the generate_password function
def generate_password():
    # Get the length of the password from the first Entry widget
    length = 16

    # Define the character sets to use in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine the character sets
    all_chars = uppercase_letters + lowercase_letters + digits + symbols

    # Generate a password of the specified length
    password = ''.join(random.choices(all_chars, k=length))

    #Copy to clipboard
    pyperclip.copy(password)


    # Display the password in the second Entry widget
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entries():
    # Get the values of the Entry widgets
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0:
        messagebox.showinfo(message="Password is empty, please enter something")
    elif len(website) == 0:
        messagebox.showinfo(message="Website is empty, please enter something")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered Email/Username: {email} |  Password: {password}\n Is it okay to save?")


        if is_ok:
            # Write the values to a file
            with open("passwords.txt", "a") as f:
                f.write(f"\nWebsite: {website} | Email/Username: {email} |  Password: {password}")
                website_entry.delete(0,END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #


root = Tk()

root.title("Password Manager")

root.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200,width =200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

# Labels and Entries
# Website Row
website_label = Label(root, text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=2)


# Email Row
email_label = Label(root, text="Email/Username")
email_label.grid(row=2, column=0)
email_entry = Entry(width=30)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"p.aleksa98@gmail.com")

# Create third label
password_label = Label(root, text="Password: ")
password_label.grid(row=3, column=0)
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, columnspan=2)

# Create a button to generate the password
button1 = Button(root, text="Generate Password",width =15,  command=generate_password)
button1.grid(row=3, column=2, columnspan=2)



# Create a button to save the entries
save_button = Button(root, text="Add",width =15,  command=save_entries)

save_button.grid(row=4, column=1, columnspan=2)

root.mainloop()


