import pyaudio
from vosk import Model,KaldiRecognizer


class Voice:

     global output

     def model(self):
        model = Model(r"C:\Users\Mr\PycharmProjects\speech_recognizer\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
        return model


     def command(self):
        recognizer = KaldiRecognizer(self.model(), 16000) #
        mic = pyaudio.PyAudio()
        stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000,
                          input=True , frames_per_buffer=8192)
        stream.start_stream()

        while True:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                command = recognizer.Result()
                text = str(command[14:-3])
                if text.__contains__("glassy"):
                    newText = text.replace("glassy","glassi")
                    self.output = newText
                    return newText
                else:
                    return text


     def getText(self):

         return self.output