import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "developerbambam@gmail.com"
receiver_email = "developerbambam@gmail.com"
subject = "multipart"
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
message["Bcc"] = receiver_email

text = """\
Hi, 
it's just test mail, keep on scrolling
"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.starynaplecach.com">Stary na plecach</a>
       is such a great site.
    </p>
  </body>
</html>"""
password = input("Type your password and press enter: ")
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()