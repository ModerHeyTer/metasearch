import speech_recognition as sr

r = sr.Recognizer()


def listen():
    text = ''
    with sr.Microphone() as source:
        # print('Я вас слушаю: ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = (r.recognize_google(audio, language="ru-RU")).lower()
        except:
            pass
        # print(f'Вы сказали: {text}')
        return text


if __name__ == '__main__':
    while True:
        input(listen())