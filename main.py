import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import pywhatkit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 130)     # setting up new voice rate


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    strTime=datetime.datetime.now().strftime("%I:%M %p")            
    hour=datetime.datetime.now().hour
    key='a3a2ebed6be94803bd544208210108'
    base_url="http://api.weatherapi.com/v1/current.json?"            
    city_name= 'são paulo'
    complete_url=base_url+"key="+key+"&q="+city_name +'&days=1&aqi=no'
    response = requests.get(complete_url)
    x=response.json()
    
    y=x["current"]
    current_temperature = y["temp_c"]
    condition = y["condition"]
    description = condition["text"]
    
    print
    if hour>=6 and hour<12:
        speak("Good morning Master."+f" It's {strTime}. The weather in São Paulo is {description} with {current_temperature} degrees")
        print("Good morning Master."+f" It's {strTime}. The weather in São Paulo is {description} with {current_temperature} degrees")
    elif hour>=12 and hour<18:
        speak("Good afternoon Master."+f" It's {strTime}. The weather in São Paulo is {description} with {current_temperature} degrees")
        print("Good afternoon Master."+f" It's {strTime}. The weather in São Paulo is {description} with {current_temperature} degrees")
    else:
        speak("Good evening Master."+f" It's {strTime}. The weather in São Paulo is {description} with {current_temperature} degrees")
        print("Good evening Master."+f" It's {strTime}. The weather in São Paulo is {description} with {current_temperature} degrees")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-US')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("please say that again")
            return "None"
        return statement

print("Initializing Luna... ")
speak("Initializing Luna... ")
wishMe()

if __name__=='__main__':


    while True:
        speak("how can I serve you?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Your personal assistant Luna is shutting down,Good bye Master')
            print('Your personal assistant Luna is shutting down,Good bye Master')
            break
#wikipedia

        if 'library' in statement:
            speak('Searching your library master...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to your library")
            print(results)
            speak(results)
#youtube
        elif 'play' in statement:
            song = statement.replace('play', '')
            speak('playing,' +  song + 'master')
            pywhatkit.playonyt(song)            
            time.sleep(5)
#google
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)
#open gmail
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)      
#time               
        elif 'what time is' in statement:
            strTime=datetime.datetime.now().strftime("%I:%M %p")
            speak(f"the time is {strTime}")
#search
        elif 'search'  in statement:
            search = statement.replace("search", "")
            webbrowser.open_new_tab('https://www.google.com/search?q='+ search)
            time.sleep(5)
#ask
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="XPV79U-V6Y4R9HWQ8 "
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
#existential crisis        
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Luna version 1 point O your personal assistant Master. I am programmed to minor tasks like,'
                  'opening youtube, google chrome, gmail and stackoverflow,predict time,search wikipedia, predict weather' 
                  ' and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by my master Nate")
            print("I was built by my master Nate")

        elif "weather" in statement:
            key='a3a2ebed6be94803bd544208210108'
            base_url="http://api.weatherapi.com/v1/current.json?"
            speak("what's the city name?")            
            city_name=takeCommand()
            complete_url=base_url+"key="+key+"&q="+city_name +'&days=1&aqi=no'
            response = requests.get(complete_url)
            x=response.json()
            
            y=x["current"]
            current_temperature = y["temp_c"]
            condition = y["condition"]
            description = condition["text"]
        
            
            speak(" Temperature in celsius is " +
                    str(current_temperature) +
                    
                    "\n description  " +
                    str(description))
            print(" Temperature in celsius is = " +
                    str(current_temperature) +
                
                    "\n description = " +
                    str(description))
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
			
time.sleep(3)


# {
#     "location": {
#         "name": "San Paulo",
#         "region": "Sao Paulo",
#         "country": "Brazil",
#         "lat": -23.53,
#         "lon": -46.62,
#         "tz_id": "America/Sao_Paulo",
#         "localtime_epoch": 1627794695,
#         "localtime": "2021-08-01 2:11"
#     },
#     "current": {
#         "temp_c": 11.9,
#         "is_day": 0,
#         "condition": {
#             "text": "Partly cloudy"
#         },
#         "precip_mm": 0.0,
#         "humidity": 87,
#         "feelslike_c": 10.7,
#         "uv": 1.0
#     }
# }
 