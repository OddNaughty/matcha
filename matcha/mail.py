# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

def send_mail(to, subject, message):
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = MIMEText(message)

    msg['Subject'] = subject
    msg['From'] = "matcha@matcha.matcha"
    msg['To'] = to

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

def send_password_reset(to, password):
    message = "Hello, your password has been reset to {}".format(password)
    send_mail(to, "Matcha password reset", message)