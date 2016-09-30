import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from matcha import app

def send_mail(to_address, subject, body):
    login = app.config['SMTP_LOGIN']
    password = app.config['SMTP_PASSWORD']
    from_address = "staff@matcha.com"

    # Bind to server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login, password)

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

def send_password_reset(to, password):
    message = "Hello, your password has been reset to {}".format(password)
    send_mail(to, "Matcha password reset", message)