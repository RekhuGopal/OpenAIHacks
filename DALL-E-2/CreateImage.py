import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "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"
response = openai.Image.create(
  prompt="A women",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print (image_url)