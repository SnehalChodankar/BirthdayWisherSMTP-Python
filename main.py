import datetime as dt
import random
import smtplib

import pandas

##################### Normal Starting Project ######################


MY_EMAIL = "snehalchodankar357@gmail.com"
PASSWORD = "chiyuicppmxfkyzt"

now = dt.datetime.now()
today = (now.month, now.day)
print(today)

df_data = pandas.read_csv("./birthdays.csv")

birthdays_dict = {(val.month, val.day):val  for (key, val) in df_data.iterrows()}
# print(birthdays_dict)

if today in birthdays_dict:
    person = birthdays_dict[today]
    # print(person)
    person_name = str(person["name"])


    letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    letter = random.choice(letters_list)

    with open(f"./letter_templates/{letter}") as letter_file:
        data = letter_file.read()
        data = data.replace("[NAME]", person_name)

        # print(data)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="snehalchodankar955@gmail.com",
                            msg=f"Subject:Happy Birthday {person_name}!\n\n{data}")


