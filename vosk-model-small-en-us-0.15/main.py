from Recognizer_Engine import Voice




# Voice Recognizer
while True:
    try :
        voice = Voice()
        txt = "ME-> "+voice.command()
        if voice.command() != "":
          print(txt)

        elif "exit" == voice.command():
             break

    except KeyboardInterrupt:
           pass







