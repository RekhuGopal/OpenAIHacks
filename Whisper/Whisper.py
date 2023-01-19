import whisper

model = whisper.load_model("base")
result = model.transcribe("D:\VSCode\GitRepos\OpenAIHacks\Whisper\Test.mp3")
options = whisper.DecodingOptions(fp16=False)
print(result["text"])