import smtplib
from email.mime.text import MIMEText

def send_mail(customer , dealer, rating, comments):
    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = "4c70ed53177a51"
    password = "fc5ab0a554212c"
    message = f"<h3>New Feedback submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    
    sender_email = "email1@example.com"
    reciever_email = "email2@exmaple.com"
    msg = MIMEText(message, "html")
    msg["Subject"] = "Lexus Feedback"
    msg["From"] = sender_email
    msg["to"] = reciever_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())
