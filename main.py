import os
from tkinter import *
from PIL import ImageTk, Image


master = Tk()
master.title("Banking App")

# Variables
temp_register_name = StringVar()
temp_register_age = StringVar()
temp_register_gender = StringVar()
temp_register_password = StringVar()

temp_login_name = StringVar()
temp_login_password = StringVar()

# Font variables
title_font = "Calibri 14 bold"
label_font = "Calibri 12"
btn_font = "Calibri 12 bold"
notif_font = "Calibry 10 italic"


# Button Functions
def register_person():
    name = temp_register_name.get()
    age = temp_register_age.get()
    gender = temp_register_gender.get()
    password = temp_register_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "":
        notif_register.config(text="All fields are required", font=notif_font, fg="red")
        return
    else:
        notif_register.config(text="You are now registered!", font=notif_font, fg="green")

    for name_check in all_accounts:
        if name == name_check:
            notif_register.config(text="Account already exists!", font=notif_font, fg="red")
            return
        else:
            new_file = open(name, "w")
            new_file.write(name + "\n")
            new_file.write(password + "\n")
            new_file.write(age + "\n")
            new_file.write(gender + "\n")
            new_file.write("O")
            new_file.close()
            notif_register.config(text="Account has been created", font=notif_font, fg="green")


def login_person():
    global login_name
    global login_password
    global file_data

    # Variables
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    all_accounts = os.listdir()

    if login_name == "" or login_password == "":
        notif_login.config(text="All fields are required!", font=notif_font, fg="red")
    else:
        for name in all_accounts:  
            if name == login_name:
                file = open(name, "r")
                file_data = file.read()
                file_data = file_data.split("\n")
                password = file_data[1]

                # Account Dashboard Screen
                if login_password == password:
                    account_dashboard()
                    file.close()
                    print("File is closed!!!")
                    break
                else:
                    notif_login.config(text="Your password is incorrect!", font=notif_font, fg="red")
                    break

            notif_login.config(text="No account found!", font=notif_font, fg="red")


def personal_detail():
    # Variables
    login_name = temp_login_name.get()
    all_accounts = os.listdir()

    # Screen
    personal_detail_screen = Toplevel(master)
    personal_detail_screen.title("Personal Data")

    # Fetching data
    for name in all_accounts:
        if name == login_name:
            with open(name, "r") as f:
                file_data = f.read()
                file_data = file_data.split("\n")

                name_n = file_data[0]
                password = file_data[1]
                age = file_data[2]
                gender = file_data[3]
                balance = file_data[4]

    # Labels
    Label(personal_detail_screen, text=f"Your personal details {name_n}", font=title_font, fg="darkblue").grid(row=0, sticky="N", pady=10, padx=5)
    Label(personal_detail_screen, text=f"Name: {login_name}", font=label_font).grid(row=1, sticky="W", padx=(30, 0))
    Label(personal_detail_screen, text=f"Password: {password}", font=label_font).grid(row=2, sticky="W", padx=(30, 0))
    Label(personal_detail_screen, text=f"Age: {age}", font=label_font).grid(row=3, sticky="W", padx=(30, 0))
    Label(personal_detail_screen, text=f"Gender: {gender}", font=label_font).grid(row=4, sticky="W", padx=(30, 0))
    Label(personal_detail_screen, text=f"Balance: {balance} €", font=label_font).grid(row=5, sticky="W", padx=(30, 0), pady=(0, 10))

    print("personel detail")


def deposit_detail():
    print("deposit detail")


def withdrawel_detail():
    print("withdrawel detail")


# Screen Functions
def register():
    # Globals
    global notif_register

    # Screen
    register_screen = Toplevel(master)
    register_screen.title("Register")

    # Labels
    Label(register_screen, text="Pleas enter your details below", font=title_font, fg="darkblue").grid(row=0, sticky="N", pady=10, padx=5)
    Label(register_screen, text="Name", font=label_font).grid(row=1, sticky="W", padx=2)
    Label(register_screen, text="Age", font=label_font).grid(row=2, sticky="W", padx=2)
    Label(register_screen, text="Gender", font=label_font).grid(row=3, sticky="W", padx=2)
    Label(register_screen, text="Password", font=label_font).grid(row=4, sticky="W", padx=2)
    notif_register = Label(register_screen, font=notif_font, fg="red")
    notif_register.grid(row=6, sticky="N", pady=10)

    # Entrys
    Entry(register_screen, textvariable=temp_register_name, width=15).grid(row=1, column=0, sticky="E", padx=(0, 10), pady=2)
    Entry(register_screen, textvariable=temp_register_age, width=15).grid(row=2, column=0, sticky="E", padx=(0, 10), pady=2)
    Entry(register_screen, textvariable=temp_register_gender, width=15).grid(row=3, column=0, sticky="E", padx=(0, 10), pady=2)
    Entry(register_screen, textvariable=temp_register_password, width=15, show="*").grid(row=4, column=0, sticky="E", padx=(0, 10), pady=2)

    # Buttons
    Button(register_screen, text="Register", font=btn_font, fg="green", width=25, command=register_person).grid(row=5, sticky="N", pady=(10, 2), padx=10)


def login():
    # Globals
    global notif_login
    global login_screen

    # Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")

    # Labels
    Label(login_screen, text=f"Login in to your account", font=title_font, fg="darkblue").grid(row=0, columnspan=2, sticky="N", pady=10, padx=5)
    Label(login_screen, text="Name", font=label_font).grid(row=1,column=0, sticky="W", padx=(2,0))
    Label(login_screen, text="Password", font=label_font).grid(row=2,column=0, sticky="W", padx=(2, 0))
    notif_login = Label(login_screen, font=notif_font, fg="red")
    notif_login.grid(row=4, columnspan=2, pady=10)

    # Entrys
    Entry(login_screen, textvariable=temp_login_name, width=15).grid(row=1, column=1)
    Entry(login_screen, textvariable=temp_login_password, width=15, show="*").grid(row=2,column=1, sticky="W")

    # Buttons
    Button(login_screen, text="Login", font=btn_font, width=20, command=login_person).grid(row=3,columnspan=2, pady=10, padx=10)


def account_dashboard():
    name = file_data[0]

    # Screen
    account_screen = Toplevel(master)
    account_screen.title("Dashboard")
    
    # Labels
    Label(account_screen, text="Account Dashboard", font=title_font, fg="darkblue").grid(row=0, columnspan=2, sticky="N", padx=10)
    Label(account_screen, text=f"Welcome {name}", font=("Calibri 12 bold"), fg="darkgreen").grid(row=1, columnspan=2, sticky="N", padx=10)

    # Buttons
    Button(account_screen, text="Personal Details", font=btn_font, width=25, command=personal_detail).grid(row=2, columnspan=2, padx=10)
    Button(account_screen, text="Deposit",font=btn_font, width=25, command=deposit_detail).grid(row=3, columnspan=2, padx=10)
    Button(account_screen, text="Withdraw", font=btn_font, width=25, command=withdrawel_detail).grid(row=4, columnspan=2, padx=10, pady=(0, 10))
    login_screen.destroy()


# Image import
img = Image.open("bank.jpg")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

# Labels
Label(master, text="Custom Banking Beta", font=title_font, fg="darkblue").grid(row=0, sticky="N", pady=10, padx=10)
Label(master, text="The most secure bank you ever used", font=label_font).grid(row=1, sticky="N", padx=10)
Label(master, image=img).grid(row=2, sticky="N")

# Buttons
Button(master, text="Register", font=btn_font, width=20, command=register).grid(row=3, sticky="N")
Button(master, text="Login", font=btn_font, width=20, command=login).grid(row=4, sticky="N", pady=10)


master.mainloop()
