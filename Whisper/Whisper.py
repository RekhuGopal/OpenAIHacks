import whisper

model = whisper.load_model("base")
options = whisper.DecodingOptions(fp16=False)
result = model.transcribe("D:\VSCode\GitRepos\OpenAIHacks\Whisper\Test.mp3")
print(result["text"])