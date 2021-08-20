import smtplib
from PriceTracker.configs import APP_PASSWORD, SENDER_EMAIL


def send_mail(receiver_email, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SENDER_EMAIL, APP_PASSWORD)

    subject = 'PriceTracker - Hurray! Price fell down!'
    body = 'Price for this product is currently lower then the price you set. Check the link ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        SENDER_EMAIL,
        receiver_email,
        msg
    )

    server.quit()

    print('Email has been sent')
