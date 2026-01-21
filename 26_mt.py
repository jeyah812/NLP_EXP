from transformers import pipeline

translator = pipeline("translation_en_to_fr")

text = "Natural language processing is interesting"
translation = translator(text)

print("English:", text)
print("French:", translation[0]['translation_text'])
