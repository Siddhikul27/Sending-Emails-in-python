import pandas as pd 
import smtplib


SenderAddress = "siddhikulkarni.96@gmail.com"
password = "asambhav123"


e = pd.read_csv('C:/Users/User/Desktop/Email_id.csv')
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is test email from python"
subject = "Hello World"
body = "subject:{}\n\n{}".format(subject,msg)

for email in emails:
	server.sendmail(SenderAddress,email,msg)
server.quit()

