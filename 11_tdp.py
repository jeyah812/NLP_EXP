grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["dog"]],
    "V": [["chased"]]
}

def parse(symbols, words):
    if not symbols and not words:
        return True
    if not symbols or not words:
        return False

    first = symbols[0]

    if first in grammar:
        for rule in grammar[first]:
            if parse(rule + symbols[1:], words):
                return True
    else:
        if first == words[0]:
            return parse(symbols[1:], words[1:])

    return False

sentence = "the dog chased the dog".split()
print(parse(["S"], sentence))