from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import pandas as pd
import re
import smtplib
import ssl
import sys

load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

SMTP_PORT: int = 465
SMTP_SERVER: str = "smtp.gmail.com"

def send_email(
    sender_email: str,
    sender_password: str,
    receiver_email: str,
    template: str,  # Email template as HTML
    args: dict      # Arguments to be replaced in the template
) -> None:
    print(f"Sending email to {receiver_email}")

    template = template.format(**args)

    subject = ""
    subject_match = re.search(r'<!--\s*(.*?)\s*-->', template, re.DOTALL)
    if subject_match:
        subject = subject_match.group(1).strip()
    else:
        raise ValueError("Subject not found in the email template")

    email: MIMEMultipart = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject
    email.attach(MIMEText(template, "html"))

    ssl_context: ssl.SSLContext = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=ssl_context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email.as_string())

def print_usage() -> None:
    print("Usage: python3 main.py <path_to_data> <path_to_template>")

def main() -> None:
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)

    users_file_path = sys.argv[1]      # CSV file with users data: field_to_send_1,field_to_send_2,...,field_to_send_n,user_email
    email_template_path = sys.argv[2]  # Email template path as an HTML file
    email_template = open(email_template_path, "r").read()

    users_data = pd.read_csv(users_file_path, delimiter=",")
    fields = users_data.columns

    for index, user in users_data.iterrows():
        args = {fields[i]: user.iloc[i] for i in range(len(fields))}
        send_email(SENDER_EMAIL, SENDER_PASSWORD, user["user_email"], email_template, args)

if __name__ == "__main__":
    main()