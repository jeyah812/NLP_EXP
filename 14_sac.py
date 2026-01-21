import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP_SG VP_SG | NP_PL VP_PL
NP_SG -> 'he'
NP_PL -> 'they'
VP_SG -> 'runs'
VP_PL -> 'run'
""")

parser = ChartParser(grammar)

sentences = ["he runs", "they run", "he run"]

for s in sentences:
    tokens = s.split()
    parses = list(parser.parse(tokens))
    print(s, ":", "Correct" if parses else "Incorrect")