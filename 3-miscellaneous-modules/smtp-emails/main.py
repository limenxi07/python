# automated birthday wishies via email
import smtplib, datetime as dt, pandas as pd, random

email = ""
password = ""
dataf = pd.read_csv("3-miscellaneous-modules/smtp-emails/birthdays.csv")
data = dataf.to_dict(orient="records")

for i in data:
  if i["month"] == dt.datetime.now().month and i["day"] == dt.datetime.now().day:
    with open(f"3-miscellaneous-modules/smtp-emails/letter-{random.randint(1, 3)}.txt") as file:
      t = file.read()
      letter = t.replace("[NAME]", i["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls() # establish secure connection to server
      connection.login(user=email, password=password)
      connection.sendmail(
        from_addr=email, 
        to_addrs=i["email"], 
        msg=f"Subject:Happy Birthday!\n\n{letter}"
      )