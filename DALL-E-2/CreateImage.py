import os
import openai
import webbrowser

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="Indian Cricketer Sachin Tendulkar celebrating century",
  n=1,
  size="1024x1024"
)
print(response)
image_url = response['data'][0]['url']
print (image_url)
webbrowser.open_new_tab(image_url)