import speechrecognizer as sr
x = sr.Recognizer()
with sr.Microphone() as source:
	print("edhavdhu pesu:")
	audio = x.listen(source)
	try:
		a.recognize_google(audio)
		print("You said: {}".format(text))

	except:
		print("Ozhunga pesu da venna")