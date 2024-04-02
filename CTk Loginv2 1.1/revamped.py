from customtkinter import *
from PIL import Image
import json
import random


img = Image.open("profile.png")

def create():
    em = email.get()
    user = username.get()
    passw = password.get()

    accounts = 'literal_users.json'
    key_creation = user

    with open(accounts, 'r') as f:
        j = json.load(f)
        j[key_creation] = {"Username": user, "Password": passw, "Email": em, "ID": key_creation, "Display_Name": None}
        with open(accounts, 'w') as b:
            json.dump(j, b, indent=4)
            print("[+] created use login")

def login():
 accounts = 'literal_users.json'
 gra = username_L.get()
 try:
    if gra:
      if password_L:
         
       with open(accounts, 'r') as f:
            j = json.load(f)
            if gra == j[gra]["Username"]:          
                passW = password_L.get()
                if passW == j[gra]["Password"]:
                    print("email: ", j[gra]["Email"]) #verifys email
                    print("[+] logged in")
                    user()
                    us_label = CTkLabel(app, text=username_L.get(), image=CTkImage(img, size=(60, 60)), font=CTkFont('Arial', 20), )
                    us_label.pack(anchor='se', pady=10)

                else:
                 print("wrong password, try again")
      else:
         print("you need to enter a password")
    else:
         print("enter a username")

 except:
     print("wrong username, try again")









   
def user():

 accounts = 'literal_users.json'
 gra = username_L.get()
 with open(accounts, 'r') as f:
    j = json.load(f)
    user_label.destroy()
    nw_label = CTkLabel(tabview.tab('User Data'), text=f'Username: {j[gra]["Username"]}\nPassword: {j[gra]["Password"]}\nEmail: {j[gra]["Email"]}\nID: {j[gra]["ID"]}\nDisplay Name: {j[gra]["Display_Name"]}', font=CTkFont('Times New Roman Thin', 20), text_color="#FFFFFF")
    nw_label.pack(anchor='center', pady=10)

   
       

def light_dark():
   if toggle_l_d.get() == True:
      set_appearance_mode("light")
   else:
       set_appearance_mode("dark")


def change_e():
   accounts = 'literal_users.json'
   gra = username_L.get()
   passw = password_L.get()
   if gra and passw:
    with open(accounts, 'r') as f:
        j = json.load(f)
        if c_email.get():
         j[gra].update({"Email": c_email.get()})
         with open(accounts, 'w') as b:
          json.dump(j, b, indent=4)
          print("[+] Changed Email Successfully")
        else:
         print("you need to enter a email to be able to change your current one")
   else:
      print("you need to login first")
               

def change_p():
   accounts = 'literal_users.json'
   gra = username_L.get()
   passw = password_L.get()
   if gra and passw:
      
    with open(accounts, 'r') as f:
        j = json.load(f)
        if c_password:
         j[gra].update({"Password": c_password.get()})
         with open(accounts, 'w') as b:
          json.dump(j, b, indent=4)
          print("[+] Changed Password Successfully")
        else:
           print("cannot set nothing as your password")
   else:
      print("you need to login first")


def display():
   accounts = 'literal_users.json'
   gra = username_L.get()
   passw = password_L.get()
   if gra and passw:
      
    with open(accounts, 'r') as f:
        j = json.load(f)
        if display:
         j[gra].update({"Display_Name": dr.get()})
         with open(accounts, 'w') as b:
          json.dump(j, b, indent=4)
          print("[+] Changed Display Successfully")
        else:
           print("cannot set nothing as your display name")
   else:
      print("you need to login first")



   
     








app = CTk()
app.geometry("900x900")
app.title("Sign Up/Login by @.lowpsi")
set_appearance_mode("dark")

#tab handler
tabview = CTkTabview(app, width=750, height=650)
tabview.pack(padx=20, pady=20, expand=True)

#tabs/borders
t1 = tabview.add("Create")
t1.configure(border_color='#57615F', border_width=2)

t2 = tabview.add("Login")
t2.configure(border_color='#57615F', border_width=2)

t3 = tabview.add("User Data")
t3.configure(border_color='#57615F', border_width=2)

t4 = tabview.add("Settings")
t4.configure(border_color='#57615F', border_width=2)


#create
header = CTkLabel(tabview.tab("Create"), text='Sign Up', font=CTkFont("Times New Roman Bold", 40), text_color="#FFFFFF")
header.pack(anchor='center', pady=10)

email = CTkEntry(tabview.tab("Create"), width=300, height=15, placeholder_text='Enter Your Email')
email.pack(anchor='center', pady=10)

username = CTkEntry(tabview.tab("Create"), width=300, height=15, placeholder_text='Enter Your Wanted Username')
username.pack(anchor='center', pady=10)

password = CTkEntry(tabview.tab("Create"), width=300, height=15, placeholder_text='Enter Your Password')
password.pack(anchor='center', pady=10)

create_acc = CTkButton(tabview.tab("Create"), width=100, height=30, text='Create Account', command=create)
create_acc.pack(anchor='center', pady=10)

#login
header_L = CTkLabel(tabview.tab("Login"), text='Sign In', font=CTkFont("Times New Roman Bold", 40), text_color="#FFFFFF")
header_L.pack(anchor='center', pady=10)

username_L = CTkEntry(tabview.tab("Login"), width=300, height=15, placeholder_text='Enter Your Username')
username_L.pack(anchor='center', pady=10)

password_L = CTkEntry(tabview.tab("Login"), width=300, height=15, placeholder_text='Enter Your Password')
password_L.pack(anchor='center', pady=10)

login_B = CTkButton(tabview.tab("Login"), width=100, height=30, text='Login', command=login)
login_B.pack(anchor='center', pady=10)

user_label = CTkLabel(tabview.tab("User Data"), text='no data found')
user_label.pack(anchor='center', pady=10)

#settings
c_email = CTkEntry(tabview.tab("Settings"), width=300, height=15, placeholder_text='Enter Your New Email')
c_email.pack(anchor='center', pady=10)

c_e_b = CTkButton(tabview.tab("Settings"), width=100, height=30, text='Change Email', command=change_e)
c_e_b.pack(anchor='center', pady=10)

c_password = CTkEntry(tabview.tab("Settings"), width=300, height=15, placeholder_text='Enter Your New Password')
c_password.pack(anchor='center', pady=10)

c_e_b = CTkButton(tabview.tab("Settings"), width=100, height=30, text='Change Password', command=change_p)
c_e_b.pack(anchor='center', pady=10)

dr = CTkEntry(tabview.tab("Settings"), width=300, height=15, placeholder_text='Enter Your Wanted Display Name')
dr.pack(anchor='center', pady=10)

d_b = CTkButton(tabview.tab("Settings"), width=100, height=30, text='Change Display Name', command=display)
d_b.pack(anchor='center', pady=10)

toggle_l_d = CTkSwitch(tabview.tab("Settings"), text='Light Mode', command=light_dark)
toggle_l_d.pack(anchor='center', pady=10)




app.mainloop()