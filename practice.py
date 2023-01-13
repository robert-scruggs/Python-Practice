import smtplib

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('scruggstyrese@gmail.com', "qpxczkxbsctewyld")

    server.sendmail("scruggstyrese@gmail.com", "scruggstyrese@gmail.com", "how are you doing")

    server.quit()

i = 0
while (i < 10):
    sendMail()
    i = i + 1
