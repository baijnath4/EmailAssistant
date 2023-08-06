import os
import sys
import win32com.client as win32

def read_unread_outlook_emails():
    sys.stdout.reconfigure(encoding='utf-8')
    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 represents the index for the Inbox folder

    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # Sort by received time in descending order

    # Filter unread messages
    unread_messages = [message for message in messages if message.UnRead]
    count_unreadEmail = len(unread_messages)
    # You can limit the number of unread emails to read by modifying the 'num_emails' variable
    num_emails = 10
    print(f'count of unread email:-- {count_unreadEmail}')
    # for i, message in enumerate(unread_messages):
    #     if i >= num_emails:
    #         break

    #     print(f"Subject: {message.Subject}")
    #     print(f"From: {message.SenderName}")
    #     print(f"Received: {message.ReceivedTime}")
    #     print(f"Body: {message.Body}")
    #     print("-" * 50)

    return count_unreadEmail