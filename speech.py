# one of these libraries for text to speech
# TODO : add deepmind wavenet tts for better quality
# TODO : also add paywall for wavenet
from gtts import gTTS
import os

# this is for linux
# sudo apt-get install mpg321
# this is for mac
# brew install mpg321



class TextToSpeech:
    def __init__(self):
        pass

    @staticmethod
    def speak(info):
        '''
        This will generate a complete sentence from all the information given

        info: A dictionary containing all the information to be spoken
            - current_time
            - temperature
            - humidity
            - description
            - deadline_progress

        '''

        project_name = 'begin quote,,, Become Rich and Ripped, end quote,'

        text = f'''
                Good Morning Alex! It's {info['current_time']} am, and here's your morning update.
                The current temperature is {info['temperature']}°F with a humidity of {info['humidity']}%.
                As for the weather, it's {info['description']}.

                Also, a quick project update - you've completed {info['deadline_progress']}% 
                of your {project_name} project. I think ur falling behind a little ...
                '''

        try:
            tts = gTTS(text=text, lang="en", slow=False)
            tts.save("text.mp3")
        except Exception as e:
            print(f"Error generating audio: {e}")
            return  # Do not proceed if there's an error

        try:
            os.system("mpg321 text.mp3")
        except Exception as e:
            print(f"Error playing audio: {e}")
        finally:
            os.remove("text.mp3")  # Ensure cleanup even on error

    


if __name__ == "__main__":
    info = {
        'current_time': '9:53',
        'temperature': 75,
        'humidity': 50,
        'description': 'sunny',
        'deadline_progress': 0.5
    }

    tts = TextToSpeech()
    # tts.speak(info)
    print("done")

    # testing threading 
    import threading
    import time

    threading.Thread(target=TextToSpeech.speak, args=(info,)).start()
    time.sleep(1)
    print('THIS SHOULD START RUNNING')