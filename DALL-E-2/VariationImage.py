import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "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"

response = openai.Image.create_variation(
  image=open("corgi_and_cat_paw.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']