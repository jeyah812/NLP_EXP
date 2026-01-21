import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'a'
N -> 'cat'
V -> 'saw'
""")

parser = ChartParser(grammar)
sentence = "a cat saw a cat".split()

for tree in parser.parse(sentence):
    tree.pretty_print()