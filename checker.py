import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import urllib.request
import urllib.error



site = str(input("What site would You like to check? "))
interval = int(input("Choose time intervals (in secs). "))
sender_email = input("Enter sender email adres. ")
password = input("Type your password and press enter: ")
receiver_email = input("Enter receiver email adress. ")

smtp_server = "smtp.gmail.com"
port = 587
subject = "Chosen site is down!"
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
text = """ Hey You!\
Your site is down, do something!"""
html = f"""\
<html>
  <body>
    <p><br> Hey You!</br>\
      <a href = {site}> Your site </a> is down! Do something!
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()

def uptime_bot(url, interval, sender_email, receiver_email, part1, part2, message, context, port, smtp_server, password):


    while True:
        try:
            conn = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
        #    print(f'HTTPError: {e.code} for {url}')
            try:
                server = smtplib.SMTP(smtp_server, port)
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            except Exception as e:
                print(e)
            finally:
                server.quit()
        except urllib.error.URLError as e:
            try:
                server = smtplib.SMTP(smtp_server, port)
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            except Exception as e:
                print(e)
            finally:
                server.quit()
        #    print(f'URLError: {e.code} for {url}')
        time.sleep(interval)

if __name__ == '__main__':
    url = site
    uptime_bot(url, interval, sender_email, receiver_email, part1, part2, message, context, port, smtp_server, password)