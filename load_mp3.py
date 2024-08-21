from pydub import AudioSegment

audio = AudioSegment.from_wav("audio.wav")

# INCREASING THE VOLUME BY 6dB
audio = audio + 30

audio = audio * 2 

audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done!")