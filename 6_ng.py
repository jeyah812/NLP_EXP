import random
from collections import defaultdict

text = "i want to eat food i want to eat lunch"
words = text.split()

bigrams = defaultdict(list)

for i in range(len(words) - 1):
    bigrams[words[i]].append(words[i + 1])

def generate_text(start, length=6):
    word = start
    result = [word]
    for _ in range(length - 1):
        word = random.choice(bigrams[word])
        result.append(word)
    return " ".join(result)

print(generate_text("i"))
