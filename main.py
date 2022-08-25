from config import secret
import openai

# Chamada na API
openai.organization = "org-Y7fWTGk542yVbKFi9GAKL5EV"
openai.api_key = secret['openai_key']

openai.Model.list()

# Completa o texto com oque mais se assimila
complete_texto = openai.Completion.create(
    model="text-davinci-002",
    prompt="The following is a list of companies and the categories they fall into:\n\n Apple, Facebook, Fedex\n\nApple\nCategory:",
    temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

# Escreve em codigo SQL oque se pede de modo textual
response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Create a SQL request to find all users who live in California and have over 1000 credits:",
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

#Corretor de texto
corretor_texto = openai.Completion.create(
  model="text-davinci-002",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
