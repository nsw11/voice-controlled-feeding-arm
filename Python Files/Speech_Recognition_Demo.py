import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Enter speech')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        #text = r.recognize_ibm(audio, "Rs5w1frJKl23x-_ulJBGd-9JVvxqZpXj3n1HAIieL7Vd", "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/393d2d0b-b151-4fb9-9169-8adf0284a1b3")
        print ('You said : {}'.format(text))
    except:
        print("Could not recognize your voice")
        