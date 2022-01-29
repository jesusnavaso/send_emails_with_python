import os
import smtplib
from email.message import EmailMessage
import imghdr
from pathlib import Path

EMAIL_USER = os.environ.get('gmail_user_python')
EMAIL_PASSWORD = os.environ.get('gmail_password_python')

LOCAL_ATTACHMENT_FOLDER = "resources/attachments"
HTML_BODY_OF_EMAIL = "resources/html_body_of_email.html"


def construct_message(with_attachments=True):
    """It constructs the message object.
    * By default it adds the attachments located in LOCAL_ATTACHMENT_FOLDER unless with_attachments=False
    * It reads the html body of the email from HTML_BODY_OF_EMAIL"""
    subject = "Test email with attachments"
    body = "Sample mail with attachments"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER  # It can be a list or a comma separated string of email addresses
    msg.set_content(body)

    with open(HTML_BODY_OF_EMAIL, 'r') as html_file:
        html_text = html_file.read()
        msg.add_alternative(html_text, subtype='html')

    if with_attachments is True:
        attachments_folder = Path(LOCAL_ATTACHMENT_FOLDER)

        for attachment_file in attachments_folder.iterdir():
            add_binary_attachment(msg, attachment_file)

    return msg


def add_image_attachment(msg, image_path: Path):
    # Deprecated, since it seems that add_binary_attachment methods sends images correctly and it is simpler
    with open(image_path, 'rb') as f:
        image_data = f.read()
        image_format = imghdr.what(f.name)
        image_name = os.path.basename(f.name)

    msg.add_attachment(image_data, maintype='image', subtype=image_format, filename=image_name)


def add_binary_attachment(msg, path_to_pdf: Path):
    """ It works for PDF and ZIP attachments. But it also seems to work for images."""
    with open(path_to_pdf, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(f.name)

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


def send_email(msg: EmailMessage):
    """ You can create a local debugging server with smtpd. Look into the README file for more details."""
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        smtp.send_message(msg)


if __name__ == '__main__':
    message = construct_message(with_attachments=False)
    send_email(message)
