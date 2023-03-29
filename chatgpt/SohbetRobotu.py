import speech_recognition as sr
import openai
import gtts
import random 
import os
from playsound import playsound

openai.api_key = "YOUR API KEY"

r = sr.Recognizer()
mic = sr.Microphone(device_index = 1)

with sr.Microphone(device_index = 0) as source:
    print("Sizi Dinliyorum?")
    audio = r.listen(source)

try:
    print("Çıktı:"+r.recognize_google(audio, language = "tr"))
except sr.UnknownValueError:
    print("Ses Algılanamadı")
except sr.RequestError as e:
    print("Sonuç alınamadı:{0}".format(e))

conversation = ""
user_name = "Mustafa"

while True:
    with mic as source:
        print("Dinliyor...")
        r.adjust_for_ambient_noise(source,duration = 0.2)
        audio = r.listen(source)
    print("Dinleme Bekleniyor.")

    try:
        user_input = r.recognize_google(audio, language = "tr")
        print("Kullanıcının İfadesi :",user_input)
    except Exception as e:
        print(e)
        continue
    prompt = user_name + ":" + user_input + "\nBot:"
    conversation += prompt

    response = openai.Completion.create(model = "text-davinci-003",
                                        prompt = conversation,
                                        max_tokens = 4000,
                                        top_p = 1.0,
                                        frequency_penalty = 0.0,
                                        presence_penalty = 0.0)
    response_str = response["choices"][0]["text"].strip()

    print(response_str)

    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)

    randfile = str(r2)+"randomtext"+str(r1) +".mp3"

    tts = gtts.gTTS(str(response_str),lang='tr', slow=True)
    tts.save(randfile)
    playsound(randfile)    
    os.remove(randfile)


   
