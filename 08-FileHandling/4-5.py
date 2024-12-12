import re

def email_sender(email_content):
   
    sender_pattern = r'^From:.*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    sender_match = re.search(sender_pattern, email_content, re.MULTILINE)
    return sender_match.group(1) if sender_match else "Sender not found"

def email_recipient(email_content):
  
    recipient_pattern = r'^To:.*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    recipient_match = re.search(recipient_pattern, email_content, re.MULTILINE)
    return recipient_match.group(1) if recipient_match else "Recipient not found"

def email_subject(email_content):
   
    subject_pattern = r'^Subject:\s*(.*)'
    subject_match = re.search(subject_pattern, email_content, re.MULTILINE)
    return subject_match.group(1).strip() if subject_match else "Subject not found"

def email_body(email_content):

    body_pattern = r'\n\n(.*)'
    body_match = re.search(body_pattern, email_content, re.DOTALL)
    return body_match.group(1).strip() if body_match else "Body not found"


