class Email:
    def __init__(self, sender, receiver, content) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    message = input()
    if message == "Stop":
        break

    message = message.split()
    sender = message[0]
    receiver = message[1]
    content = message[2]
    
    email = Email(sender, receiver, content)
    emails.append(email)

indices = [int(i) for i in input().split(", ")]

for i in indices:
    emails[i].send()

for email in emails:
    print(email.get_info())
