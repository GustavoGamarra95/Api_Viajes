import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_addrs, body):
    from_addr ="ktgqrcczze2zmtcl@ethereal.email"
    login = "ktgqrcczze2zmtcl@ethereal.email"
    password = "Jrsju6v5s6NkhjPR2y"

    msg = MIMEMultipart()
    msg["from"] = "viajes_confrimar@email.com"
    msg["to"] = ', '.join(to_addrs)

    msg["Subject"] = "confirmacion de viaje"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()
