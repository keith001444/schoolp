import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(sender_email,recipient_email, password, password2, subject, body):
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        
        # Send email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def forgot_m_pass(sender_email,sender_password, recipient_email, subject, body):
    
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
           
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            print("Email sent successfully!")
        print("A default password has been sent to your email.", "success")
    except Exception as e:
        print("Failed to send email. Try again later.", "danger")

          

