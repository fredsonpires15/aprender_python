import pyttsx3
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os

# Inicializar pyttsx

idade = 23
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)  # 1 para voz feminina e 0 para voz masculina

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt')
        print("Usuário disse: " + query + "\n")
    except Exception as e:
        print(e)
        speak("Desculpe, não entendi")
        return "None"
    return query.lower()

if __name__ == '__main__':
    speak("Assistente de Amigo ativado")
    speak("Como posso ajudar você?")

    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Pesquisando na Wikipedia...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("De acordo com a Wikipedia")
            speak(results)
        
        elif 'are you' in query: 
            speak(f"Eu sou Amigo, desenvolvido por Fredson Vila Vova, ele tem {idade} anos de idade ")
        elif 'cala boca' in query:

            speak(f"Cala boca você!!")
        
        elif 'open' in query:
            if 'youtube' in query:
                speak("Abrindo Youtube")
                webbrowser.open("https://www.youtube.com")
                
            elif 'google' in query:
                speak("Abrindo Google3")
                webbrowser.open("https://www.google.com")
            elif 'github' in query:
                speak("Abrindo Github")
                webbrowser.open("https://www.github.com")
            elif 'stackoverflow' in query:
                speak("Abrindo Stack Overflow")
                webbrowser.open("https://www.stackoverflow.com")
            elif 'spotify' in query:
                speak("Abrindo Spotify")
                webbrowser.open("https://www.spotify.com")
            elif 'whatsapp' in query:
                speak("Abrindo Whatsapp")
                os.startfile("C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            elif 'music' in query:
                speak("Abrindo Spotify para música")
                webbrowser.open("https://www.spotify.com")
            elif 'disk' in query:
                speak("Qual disco você deseja abrir? D, C ou E?")
                disk = take_command()
                if disk == 'd':
                    os.startfile("D://")
                elif disk == 'c':
                    os.startfile("C://")
                elif disk == 'e':
                    os.startfile("E://")
                else:
                    speak("Desculpe, disco inválido")
        
        elif 'Sleep' in query:
            speak("Desligando assistente...")
            exit(0) 
