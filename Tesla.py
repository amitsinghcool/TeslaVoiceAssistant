import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #if you want wikipedia results pip install wikipedia
import webbrowser 
import os
import smtplib
import random
import requests, json 

engine= pyttsx3.init('sapi5') #sapi5 is a windows API for Voices
voices=engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
contacts={"amit":"singhamitrocks1999@gmail.com"} # you can put your contacts here to send mails I am prakash, test your code by mailing me and ill reply just say send mail 
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!.")
    else:
        speak("Good Evening Sir!.")
    speak("I am Tesla. Please tell me How may i help you!")    
            

def takeCommand():
    #it takes input from user and returns string output
    r=sr.Recognizer()  # to recognise audio
    with sr.Microphone() as source: #
        print("Listening.....")
        r.pause_threshold=1 # seconds of non speaking seconds
        
        
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print("user said: ", query) 

    except Exception as e:
        
        print("please say that again sir!")
        return "None"       
    return query
#for sending mail, type your account mail id and password from which you want to login and send the mail
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example@gmail.com','examplepassword')
    server.sendmail('example@gmail.com',to, content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task based on my command
        if 'wikipedia' in query:
            speak("Searching Wikipedia.... please Wait ")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia.")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack' in query:
            webbrowser.open("stackoverflow.com")

        elif 'weather' in query:
            api_key = "a31701327639a3e2751b57480ed4b785"
            # base_url variable to store url 
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Which city")
            # Give city name 
            city_name = takeCommand().lower()
            
            # complete_url variable to store 
            # complete url address 
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
            
            # get method of requests module 
            # return response object 
            response = requests.get(complete_url) 
            
            # json method of response object  
            # convert json format data into 
            # python format data 
            x = response.json() 
            
            # Now x contains list of nested dictionaries 
            # Check the value of "cod" key is equal to 
            # "404", means city is found otherwise, 
            # city is not found 
            if x["cod"] != "404": 
            
                # store the value of "main" 
                # key in variable y 
                y = x["main"] 
            
                # store the value corresponding 
                # to the "temp" key of y 
                current_temperature = y["temp"]-273.15 
            
                # store the value corresponding 
                # to the "pressure" key of y 
                current_pressure = y["pressure"] 
            
                # store the value corresponding 
                # to the "humidity" key of y 
                current_humidiy = y["humidity"] 
            
                # store the value of "weather" 
                # key in variable z 
                z = x["weather"] 
            
                # store the value corresponding  
                # to the "description" key at  
                # the 0th index of z 
                weather_description = z[0]["description"] 
            
                # print following values 
                speak(f" Sir the current temperature of" + city_name  + "is"
                               + str(current_temperature) + "degree celcius" 
                    "\n  with atmospheric pressure of " +
                                str(current_pressure) +
                    "\n and humidity of " +
                                str(current_humidiy) +
                    "\n with overall " +
                                str(weather_description) +"nature") 
            
            else: 
                print(" City Not Found ") 

        elif 'play music' in query:
            music_dir="E:\\Songs"
            songs = [x for x in os.listdir(music_dir) if x.endswith(".mp3")]
            musicrandom=random.randint(1,101)
            os.startfile(os.path.join(music_dir, songs[musicrandom]))
        elif 'play some music' in query:
            music_dir="E:\\Songs"
            songs = [x for x in os.listdir(music_dir) if x.endswith(".mp3")]
            musicrandom=random.randint(1,101)
            os.startfile(os.path.join(music_dir, songs[musicrandom]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
        
            speak(f"Sir, the time is {strTime}")    
            

        elif "open code" in query:
            codePath="C:\\Users\\HAPPY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(codePath)    
        elif 'send mail' in query:
            try:
                speak("Who Should I Send The Mail To?")
                name=takeCommand().lower()
                if name in contacts:
                    to=contacts[name]
                    speak("What Should I say?")
                    content=takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent sir!.")
            except Exception as e:
                speak("Sorry the mail couldn't be sent at this moment!.")
        elif 'send email' in query:
            try:
                speak("What Should I say?")
                content=takeCommand()
                to="kvshete15@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!.")
            except Exception as e:
                speak("Sorry the mail couldn't be sent at this moment!.")        
     
        elif 'what' in query:
           webbrowser.open(f"{query}")    

        elif 'why' in query:
           webbrowser.open(f"google.com/{query}")

        elif 'where' in query:
           webbrowser.open(f"google.com/{query}")  
        elif 'quit' in query:
            exit()
        elif 'exit' in query:
            exit()    
