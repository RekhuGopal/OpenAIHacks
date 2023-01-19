import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "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"

response = openai.Image.create_edit(
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']