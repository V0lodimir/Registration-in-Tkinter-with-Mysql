import mysql.connector
import tkinter as tk

connection = mysql.connector.connect(host="127.0.0.1",
                                    database="project",
                                    user="root",
                                    password="")

cursor=connection.cursor()
w = tk.Tk()

w.geometry("500x600")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

lbl_name = tk.Label(master=frm_form, text="Login:")
ent_name = tk.Entry(master=frm_form, width=50)

lbl_name.grid(row=0, column=0)
ent_name.grid(row=0, column=1)
 
lbl_password = tk.Label(master=frm_form, text="Password:")
ent_password = tk.Entry(master=frm_form, width=50)

lbl_password.grid(row=1, column=0)
ent_password.grid(row=1, column=1)

def login():
    get_login = ent_name.get()
    get_password = ent_password.get()
    a = cursor.execute("select login, password from users where login = %s and password = %s", (get_login, get_password))

    if not cursor.fetchone():
        print("User missing or password is wrong.")
    else:
        print("Welcome")


frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Login", command=login)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

w.mainloop()
cursor.close()