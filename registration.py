import mysql.connector
import tkinter as tk

connection = mysql.connector.connect(host="127.0.0.1",
                                    database="project",
                                    user="root",
                                    password="")

cursor=connection.cursor()
w = tk.Tk()

w.geometry("500x600")

label = tk.Label(
    text="Enter information about yourself.",
    bg="white", 
    fg="black"
)
label.pack()


frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

frm_form.pack()

lbl_login = tk.Label(master=frm_form, text="Login:")
ent_login = tk.Entry(master=frm_form, width=50)

lbl_login.grid(row=0, column=0)
ent_login.grid(row=0, column=1)
 
lbl_password = tk.Label(master=frm_form, text="Password:")
ent_password = tk.Entry(master=frm_form, width=50)

lbl_password.grid(row=1, column=0)
ent_password.grid(row=1, column=1)
 
lbl_password2 = tk.Label(master=frm_form, text="Password:")
ent_password2 = tk.Entry(master=frm_form, width=50)

lbl_password2.grid(row=2, column=0)
ent_password2.grid(row=2, column=1)

def send_inf():
    get_login = ent_login.get()
    get_password = ent_password.get()
    get_password2 = ent_password2.get()

    if get_password != get_password2:
        print("Wrong password")
        exit() 
    else:
        True
    cursor.execute("select login, password from users where login = %s and password = %s",
    (get_login, get_password))

    if cursor.fetchone() is None:
        cursor.execute("insert into users(login, password) values(%s, %s)",
        (get_login, get_password))
        print("Registration is complete")
        connection.commit()

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Register", command=send_inf)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

w.mainloop()
cursor.close()