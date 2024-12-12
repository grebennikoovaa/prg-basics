from emails import email_sender, email_recipient, email_subject, email_body

def main():
    try:
        # Read the content of the email file
        with open('email.txt', 'r') as file:
            email_content = file.read()

        # Extract details using functions from the module
        sender = email_sender(email_content)
        recipient = email_recipient(email_content)
        subject = email_subject(email_content)
        body = email_body(email_content)

        # Print the extracted details
        print(f"Sender: {sender}")
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print("Body:")
        print(body)

    except FileNotFoundError:
        print("Error: The file 'email.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()