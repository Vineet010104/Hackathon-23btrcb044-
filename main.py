import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



# Setting up text-to-speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello sir, I'm your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        speak("Sorry, I did not catch that.")
        text = ""
    except sr.RequestError:
        print("Sorry, my speech service is not working.")
        speak("Sorry, my speech service is not working.")
        text = ""

if "what" in text and "about" in text and "you" in text:
    speak("I am also having a good day, sir.")
speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    try:
        text2 = r.recognize_google(audio)
        print("You said:", text2)
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        speak("Sorry, I did not catch that.")
        text2 = ""
    except sr.RequestError:
        print("Sorry, my speech service is not working.")
        speak("Sorry, my speech service is not working.")
        text2 = ""

if "information" in text2:
    speak("You need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            info = r.recognize_google(audio)
            print("You said:", info)
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            speak("Sorry, I did not catch that.")
            info = ""
        except sr.RequestError:
            print("Sorry, my speech service is not working.")
            speak("Sorry, my speech service is not working.")
            info = ""

    class Info:
        def __init__(self):
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)

        def get_info(self, query):
            self.query = query
            self.driver.get("https://www.wikipedia.org")
            time.sleep(2)  # Wait for the page to load

            # Find the search input box and enter the query
            search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
            search.click()
            search.send_keys(query)

            # Find and click the search button
            enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
            enter.click()

            speak(f"Here is the information I found about {query}.")
            input("Press Enter to exit...")
            self.driver.quit()

    speak("searching in wikipedia{}".format(info))
    # Call the assistant to get information
    assist = Info()
    assist.get_info(info)
    
elif "play" and "video" in text2:
    speak("you want to play which video??")

    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            vid = r.recognize_google(audio)
            print("You said:", vid)
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            speak("Sorry, I did not catch that.")
            vid = ""
        except sr.RequestError:
            print("Sorry, my speech service is not working.")
            speak("Sorry, my speech service is not working.")
            vid = ""

class music():
    def __init__(self):
        # Use ChromeDriver Manager to handle the driver setup
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--autoplay-policy=no-user-gesture-required")  # Force autoplay
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")  # Maximize the window
        self.driver = webdriver.Chrome(service=service, options=options)

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        time.sleep(3)  # Wait for the search results to load

        try:
            # Click on the first video in the search results
            video = self.driver.find_element(By.XPATH, '(//*[@id="video-title"])[1]')
            video.click()
            time.sleep(3)  # Wait for the video page to load
            
            # Try to skip any ads
            try:
                skip_button = self.driver.find_element(By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]')
                skip_button.click()
                print("Ad skipped successfully.")
            except:
                print("No skippable ad found.")

            # Use JavaScript to force the video to play
            video_element = self.driver.find_element(By.TAG_NAME, "video")
            self.driver.execute_script("arguments[0].play();", video_element)
            print("Video is playing...")

        except Exception as e:
            print("Error:", str(e))

        input("Press Enter to exit...")
        self.driver.quit()

assist = music()
assist.play(vid)

