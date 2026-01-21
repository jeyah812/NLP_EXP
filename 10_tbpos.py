def transform_tagger(sentence):
    tags = [(word, "NN") for word in sentence.split()]

    # Transformation rule:
    # Change NN to VBG if word ends with 'ing'
    final_tags = []
    for word, tag in tags:
        if word.endswith("ing"):
            tag = "VBG"
        final_tags.append((word, tag))
    return final_tags

print(transform_tagger("birds are flying"))
