import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Q: Who is Sachin Tendulkar?\nA:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(response)