import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'dog'
V -> 'chased'
""")

parser = EarleyChartParser(grammar)
sentence = "the dog chased the dog".split()

for tree in parser.parse(sentence):
    print(tree)