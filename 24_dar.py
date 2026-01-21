dialog = [
    "Hello",
    "Can you help me?",
    "I need information",
    "Thank you"
]

print("Dialog Act Classification:")
for utterance in dialog:
    if "?" in utterance:
        act = "Question"
    elif "thank" in utterance.lower():
        act = "Acknowledgement"
    elif "hello" in utterance.lower():
        act = "Greeting"
    else:
        act = "Statement"
    print(utterance, "->", act)
