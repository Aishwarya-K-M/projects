import pandas as pd
from tkinter import *
#from tkcalendar import Calendar
import datetime as dt
from tkinter  import messagebox as ms
from email_validator import validate_email, EmailNotValidError
import random as rd
import smtplib


'''with open("birthday-wisher/birthdays.csv",'a') as f:
    f.write("aishu,abc@dsd,2021,12,12\n")

data = pd.read_csv("birthday-wisher/birthdays.csv")
print(data)'''


def check_det():
    data = pd.read_csv("birthday-wisher/birthdays.csv")
    data_dic = data.to_dict(orient="records")
    for data in data_dic:
        if data['month'] == now.month and data['day'] == now.day:
            my_email = "gesturecadley@gmail.com"
            password = "ldksadfdmsf"
            l_no = rd.randrange(1,3)
            with open(f"birthday-wisher/letter_templates/letter_{l_no}.txt",'r') as f:
                letter = f.readlines()
                let = ''
                for line in letter:
                    lines = line.replace("[NAME]",data["name"])
                    lines = lines.replace("Angela","Aishwarya")
                    let += (lines)
            with smtplib.SMTP("smtp.gmail.com", 587) as con:
                con.starttls()
                con.login(user=my_email,password=password)
                con.sendmail(from_addr=my_email,to_addrs=data['email'],msg=f"Subject:Happy Birthday!!\n{let}")
                ms.showinfo(message=f"Mail sent to {data['name']}",title="Success!")


def add_det():
    date_d = date.get()
    name_d = name.get()
    email_d = email.get()
    try:
        date_d = dt.datetime.strptime(date_d,"%d/%m/%y")
    except:
        ms.showerror(message="Not the right format!!",title="Invalid!!")
    else:
        if(name_d == ''):
            ms.showerror(message="Please Enter Name!!", title="Insufficient Data!")  
        elif(email_d == ''):
            ms.showerror(message="Please Enter Email Id!!", title="Insufficient Data!")
        else:
            try:
                email_d = validate_email(email_d).email
            except EmailNotValidError as e:
                ms.showerror(message="Enter valid Email Id!!",title="Invalid!!")
            else:
                try:
                    ack = ms.askokcancel(message=f"Name:{name_d}\nEmail: {email_d}\nDate:{date_d.day}/{date_d.month}/{date_d.year}")
                    if ack:
                        try:
                            with open("birthday-wisher/birthdays.csv",'a') as f:
                                f.write(f"{name_d},{email_d},{date_d.year},{date_d.month},{date_d.day}\n")
                                email.delete(0,"end")
                                name.delete(0,"end")
                                date.delete(0,"end")
                                ms.showinfo(message="added sucessfully",title="Birthday-Wisher")
                        except:
                            ms.showerror(message="File Error!",title="Error!!")
                except:
                    ms.showerror(message="Some Error in filing data\nPlease try again!",title="Error!")

win = Tk()
win.title("Birthday wisher!")
win.config(padx=50,pady=50)
img = PhotoImage(file="birthday-wisher/happy_birth_pic.png")

can = Canvas(width = 200,height=200)
can.create_image(100,100,image=img)
can.grid(column=1,row=0)

namel = Label(text="Name: ")
namel.grid(row=1)
name = Entry(width=40)
name.grid(column=1,row=1,columnspan=2)

emaill = Label(text="Email: ")
emaill.grid(row=2)
email = Entry(width=40)
email.grid(column=1,row=2,columnspan=2)

now = dt.datetime.now()
#dob = Calendar(selectmode='day',year=now.year,day=now.day,month=now.month)
datel = Label(text="Date: ")
datel.grid(row=3)
date = Entry(width=20)
date.insert(0,"dd/mm/yy")
date.grid(row=3,column=1)


add = Button(text="Add",width=12,highlightthickness=0)
add.config(command=add_det)
add.grid(column=0, row = 4)

check = Button(text="Check",width=12,highlightthickness=0)
check.config(command=check_det)
check.grid(column=1,row=4)

win.mainloop()
