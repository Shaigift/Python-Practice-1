
send_messages = ['Hello! I am Sam', 'Hello! I am Angela', 'Hello! I am Nokia']
sent_messages = []

while send_messages:
    current_messages = send_messages.pop()
    print(f"These are the messages {current_messages}")
    sent_messages.append(current_messages)

print("\nThese are the sent messages:")
for sent_message in sent_messages:
    print(sent_message)
