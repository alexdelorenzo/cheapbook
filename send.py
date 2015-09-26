from email.message import EmailMessage
from smtplib import SMTP

from base import SENDER_EMAIL, EMAIL_USERNAME, SMTP_SERVER, EMAIL_PASSWORD, SMTP_PORT, MacBook, RECEIVER_EMAIL


def create_msg(recv: str, subject: str, body: str, sender: str=SENDER_EMAIL) -> EmailMessage:
    msg = EmailMessage()
    msg['To'] = recv
    msg['From'] = sender
    msg['Subject'] = subject
    msg.set_content(body)

    return msg


def macbook_msg(macbook: MacBook,
                recv: str=RECEIVER_EMAIL,
                sender: str=SENDER_EMAIL) -> EmailMessage:
    title = "[%s] %s" % (macbook.price, macbook.title)
    body = "%s\n%s" % (macbook.link, macbook.specs)

    return create_msg(recv, title, body, sender)


def send_msg_ssl(msg: EmailMessage, username: str=EMAIL_USERNAME,
              passwd: str=EMAIL_PASSWORD, server: str=SMTP_SERVER,
              port: int=SMTP_PORT):
    with SMTP(server, port) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(username, passwd)
        smtp_server.send_message(msg)


def send_macbook_msg(macbook: MacBook) -> None:
    print("-> Sending", macbook)
    send_msg_ssl(macbook_msg(macbook))
    print("-> Sent", macbook)
