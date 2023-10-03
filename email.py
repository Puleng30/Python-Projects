 
### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    def __init__(self, email_address, subject_line, email_contents):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False
        
    def mark_as_read(self):
        self.has_been_read = True
    
    def mark_as_spam(self):
        self.is_spam = True

# --- Lists --- #
inbox = []
outbox = []

# --- Functions --- #
def populate_inbox():
    inbox.append(Email("tim@hyperiondev.com", "Welcome to HyperionDev!", "Hi Tim! Welcome to the coding world, where you will learn all about coding!"))
    inbox.append(Email("james@hyperiondev.com", "Great work on the bootcamp!", "Continue with the good work, keep it up!"))
    inbox.append(Email("jane@gmail.com", "Your excellent marks!", "You are in the top 10 and are well on your way to graduating soon!"))
    
def list_emails():
    for x, email in enumerate(inbox):
        print(f"{x}: {email.subject_line}")

def read_email(x):
    email = inbox[x]
    print(f"From: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Body: {email.email_contents}")
    email.mark_as_read()
    print("Email has been marked as read.")

def mark_spam(x):
    email = inbox[x]
    email.mark_as_spam()
    print("Email has been marked as spam.")

def delete_email(x):
    inbox.pop(x )
    print("Email has been deleted.")

def send_email(email_address, subject_line, email_contents):
    outbox.append(Email(email_address, subject_line, email_contents))
    print("Email sent.")

# --- Email Program --- #
populate_inbox()
while True: 
    print("Welcome to your email simulator. Choose an option:") 
    print("1. Read an email") 
    print("2. Mark an email as spam") 
    print("3. Delete an email") 
    print("4. View unread emails") 
    print("5. View spam emails") 
    print("6. Send an email") 
    print("7. Quit application") 
    
    choice = input()


# Read an email
    if choice == "1":
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
        
# Mark an email as spam
    elif choice == "2":
        list_emails()
        index = int(input("Enter the index of the email you want to mark as spam: "))
        mark_spam(index)

# Delete an email
    elif choice == "3":
        list_emails()
        index = int(input("Enter the index of the email you want to delete: "))
        delete_email(index)
    
# View unread emails
    elif choice == "4":
        for email in inbox: 
            if not email.has_been_read:
                print(email.subject_line)
                    
# View spam emails
    elif choice == "5":
       for email in inbox:
           if email.is_spam:
               print(email.subject_line)
    
# Send an email
    elif choice == "6":
        email_address = input("Enter the recipient's email address: ")
        subject_line = input("Enter the subject line: ")
        email_contents = input("Enter the contents of the email: ") 
        send_email(email_address, subject_line, email_contents)
        
# Quit appplication
    elif choice == "7":
        break 
        



