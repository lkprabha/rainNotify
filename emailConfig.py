import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class configEmailSend:
    def sendemail(msg):
        emsg = msg
        port = 465  # For SSL
        context = ssl.create_default_context()
        body = "This is an email with attachment sent from Python"
        sender_email = "senderemail@gmail.com"
        receiver_email = "receiver@gmai.com"
        password = "yourpassword123"
            #input("Type your password and press enter:")
        subject = "An email with attachment from Python"

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
       #message["Bcc"] = receiver_email  # Recommended for mass emails
        etext = "Hi,"+" ***" + msg \
                #+ " "+"                                               "+body+"Thank You"

        # Add body to email
        message.attach(MIMEText(etext, "plain"))
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender_email, password)
                #message.attach(part)
                text = message.as_string()
                print(emsg)
                server.sendmail(sender_email, receiver_email, text)


