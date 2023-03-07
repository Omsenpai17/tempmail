from mailtm import email

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

# Get Domains
test = email()
print("\nDomain: " + test.domain)

# Make new email address
test.register()
print("\nEmail Adress: " + str(test.address))

# Start listening
test.start(listener, interval=1)
print("\nWaiting for new emails...")