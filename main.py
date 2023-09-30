import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import openai
from config import apikey
import requests
import pywhatkit
import pyjokes
import pyautogui
import time
def takeCommand():
    r = sr.Recognizer()
    print("listening")
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=20)
        print("Recognizing...")
        try:
            query = r.recognize_google(audio, language="en-en")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Timeout reached, no speech detected.")
            return ""
        except Exception as e:
            return "Sorry, I didn't catch that. Please say again!"


chatStr = ""
def chat(query):
    global chatStr
    openai.api_key = apikey
    messages = [{"role": "user", "content": query}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    assistant_response = response['choices'][0]['message']['content']
    say(assistant_response)

    # Update chatStr to include the AI's response
    chatStr += f"assistant: {assistant_response}\n"
    return assistant_response


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def ai(messages):
    openai.api_key = apikey
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    print('You can start chatting with the AI now.')
    while True:
        user_input = takeCommand()
        if "stop conversation" in user_input.lower():
            break
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_message = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_message.strip("\n").strip()})
        text = f"\n************\nUser: {user_input}\nAssistant: {assistant_message}"
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(assistant_message.split('AI')[1:]).strip()}.txt", "w") as f:
            f.write(text)

'''
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"

    # Fetching data
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raises an exception for HTTP errors

        data = response.json()
        if data["cod"] != 404:
            main_data = data["main"]
            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_data = data["weather"]
            weather_description = weather_data[0]["description"]

            return f"Weather in {city}: Temperature: {temperature}°K, Atmospheric Pressure: {pressure} hPa, Humidity: {humidity}%, Description: {weather_description.capitalize()}."

        else:
            return f"Weather data for {city} not found!"

    except requests.RequestException as e:
        return f"Error fetching data: {e}"
        '''

def ai(messages):
    openai.api_key = apikey
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    print('You can start chatting with the AI now.')
    while True:
        user_input = takeCommand()
        if "stop conversation" in user_input.lower():
            break
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_message = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_message.strip("\n").strip()})
        text = f"\n************\nUser: {user_input}\nAssistant: {assistant_message}"
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(assistant_message.split('AI')[1:]).strip()}.txt", "w") as f:
            f.write(text)

def writingCode():
    say("what would you like to name the project")
    project_name = takeCommand()
    try:
        os.mkdir(project_name)
    except FileExistsError:
        say("A project with that name already exists.")
    os.startfile(r"C:\Users\13379\AppData\Local\Programs\Microsoft VS Code\Code.exe", project_name)
    time.sleep(4)
    writecode = takeCommand()
    aicode = ai(writecode)
    pyautogui.hotkey('ctrl', 'n')
    say(f"coding{writecode}")
    say("completing your code")
    pyautogui.write(aicode)
    time.sleep(3)

if __name__ == '__main__':
    print('Welcome to Jarvis AI')
    say("I am Jarvis. How can I help You today")
    while True:
        query = takeCommand()


        # Handle AI command
        if "AI".lower() in query.lower():
            ai(messages=query)
            continue  # Move to next iteration to avoid checking other conditions

        # Handle web browser commands
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"],
                 ["facebook", "https://www.facebook.com"], ["tiktok", "https://www.tiktok.com"],
                 ["netflix", "https://www.netflix.com"]]
        opened = False
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} ...")
                webbrowser.open(site[1])
                opened = True
                break
        if opened is True:
            continue

        if "open vs code".lower() in query.lower():
            say("Opening vs code")
            os.startfile(r"C:\Users\13379\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            writingCode()
            continue

        if "open netbeans".lower() in query.lower():
            os.startfile(r"C:\Program Files\NetBeans-16\netbeans\bin\netbeans64.exe")
            say("Opening Netbeans")
            continue

        elif "reset chat".lower() in query.lower():
            chatStr = ""
            break

        elif "search google".lower() in query.lower():
            pyttsx3.speak("Sir, what would you like me to search for in google?")
            cn = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cn}")
            continue
        elif"search wikipedia".lower() in query.lower():
            pyttsx3.speak("Sir, what would you like me to search for in wikipedia?")
            cn = takeCommand().lower()
            webbrowser.open(f"https://en.wikipedia.org/wiki/{cn}")
            continue
        elif "search youtube".lower() in query.lower():
            pyttsx3.speak("Sir, what would you like watch in youtube?")
            cn = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={cn}")
            continue
        elif "netflix".lower() in query.lower():
            pyttsx3.speak("what would you like to watch in netflix")
            cn = takeCommand().lower()
            webbrowser.open("https://www.netflix.com/")
            continue
        elif"play music".lower() in query.lower():
            pyttsx3.speak("Sir, what would you like to listen to?")
            cn = takeCommand().lower()
            pywhatkit.playonyt(cn)
            continue

        elif "joke".lower() in query.lower():
            joke = pyjokes.get_joke()
            pyttsx3.speak(joke)
            continue

        elif"shut down".lower() in query.lower():
            os.system("shutdown /s /t 5")
            continue

        elif "restart".lower() in query.lower():
            os.system("shutdown /s /t 5")
            continue

        elif"where am I".lower() in query.lower():
            pyttsx3.speak("locating you")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                pyttsx3.speak(f"Based on your ip address you are currently in {city} city of {country}")
            except Exception as e:
                pyttsx3.speak("Could not track your location")
                pass
            continue

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        else:
            print("Chatting...")
            chat(query)
            break
## make jarvis to open vs code and make it write code


