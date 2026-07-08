from googletrans import Translator
text = "Hello, how are you?"
translator=Translator()
translated =translator.translate(text,src='en',dest="German")
print("German translation:",translated.text)
