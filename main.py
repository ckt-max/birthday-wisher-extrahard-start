##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import requests
from bs4 import BeautifulSoup #web_scraping
import smtplib
import ssl
import random
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


today = dt.datetime.now()

df = pd.read_csv('birthdays.csv')

# loop to check if today is someone's bday:
for i,j in df.iterrows():
    if j.month == today.month and j.day == today.day:

        # getting the body of the email by selecting one of the letter templates at random

        letter = random.choice(
            ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt'])

        print(letter)

        with open(letter) as file:
            contents = file.read()
            mail_body = contents.replace('[NAME]', 'Chetan')

        file.close()

        # Sending Email

        print('Composing Email....')

        email_sender = 'testmail.ckt01@gmail.com'
        email_password = 'qmvr bmrb fkbd ebkb'
        email_receiver = j.email

        content = mail_body


        # Email details
        msg = MIMEMultipart()  # function to create email
        msg['Subject'] = 'Happy Birthday'
        msg['From'] = email_sender
        msg['to'] = email_receiver
        msg.attach(MIMEText(content))  # to attach email body

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            print("Mail sent......")









