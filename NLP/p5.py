import googletrans

# print(googletrans.LANGUAGES)

translator = googletrans.Translator()
text = translator.translate("Hello, world!" , dest="fr")

print(text)