from gtts import gTTS
text="hi,how are you"
tts = gTTS(text=text)
tts.save("hello.mp3")
print("output saved as hello.mp3")
