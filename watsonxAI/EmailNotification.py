# from exchangelib import Credentials, Account, DELEGATE

# import imaplib

# username='baijkuma@in.ibm.com'
# password= 'Gaya!12345678#&!'

# # credents = Credentials(username='baijkuma@in.ibm.com', password= 'Gaya!12345678#&!')

# # # config = Configuration(server='D50PT006/50/PT/IBM', credentials= credents)

# # account = Account(
# #         primary_smtp_address='baijkuma@in.ibm.com',
# #         credentials=credents, 
# #         autodiscover=True,
# #         access_type=DELEGATE)
# mail = imaplib.IMAP4_SSL('outlook.office365.com')

# mail.login(username, password)
# mailbox = 'inbox'
# mail.select(mailbox)
# # Search for all emails
# status, email_ids = mail.search(None, 'ALL')
# email_id_list = email_ids[0].split()

# # Get the count of emails
# email_count = len(email_id_list)
# print(f"Total number of emails in {mailbox}: {email_count}")

# # Access the inbox folder
# inbox = account.inbox
# email_count = inbox.count()
# print(email_count)

# # # Print the subject and sender of the first 10 emails in the inbox
# # for item in inbox.all().order_by('-datetime_received')[:10]:
# #     print(f'Subject: {item.subject}')
# #     print(f'Sender: {item.sender}')
# #     print('---')