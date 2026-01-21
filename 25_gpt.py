import openai

openai.api_key = "YOUR_API_KEY"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Explain Natural Language Processing in simple words.",
    max_tokens=60
)

print(response.choices[0].text.strip())
