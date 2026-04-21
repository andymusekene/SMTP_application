import smtplib
from email.mime.text import MIMEText

# SMTP Server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "andymusekene@gmail.com"  # Replace with your own Gmail address
EMAIL_PASSWORD = "izvo iktr dkhm ukhd"  # Use App Password if MFA is enabled

# Create email message
msg = MIMEText(f"This is a test email sent via Gmail SMTP. My student number is 241034981.")
msg["Subject"] = f"SMTP Practical 241034981"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "brandta@cput.ac.za"

# Send email
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()  # Upgrade connection to secure
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
server.sendmail(EMAIL_ADDRESS, "brandta@cput.ac.za", msg.as_string())
server.quit()

print("Email sent successfully!")
