import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# enter the email you are sending from and password.
email = 'enter your email here'
password = 'enter your password here'
send_to_email = 'enter the email you want to send to'
# type what subject you want
subject = 'This is the subject'
# type what you want in the message
message = 'This is the message'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
print('You have sent an email')
