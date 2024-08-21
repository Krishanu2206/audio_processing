##AUDIO FILE FORMATS
#.mp3, .flac, .wav

import wave

##AUDIO SIGNAL PARAMETERS
# number of channels, sample width, framerate/sample_rate : 44,100Hz, number of frames, values of a frame ##all explanations in resources.txt

obj = wave.open("audio.wav", "rb")

#EXTRACT THE AUDIO DATA

print(f"Number of channels : {obj.getnchannels()}")
print(f"Sample width : {obj.getsampwidth()}")
print(f"Frame rate : {obj.getframerate()}")
print(f"Number of frames : {obj.getnframes()}")
print(f"PARAMETERS OF THE AUDIO : {obj.getparams()}")

t_audio = obj.getnframes()/obj.getframerate()
print(t_audio)##t_audio=time of the audio

frames=obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
print(len(frames)/(obj.getsampwidth() * obj.getnchannels()))
print(obj.getnframes())

obj.close()

##RESAMPLE AND CONVERT
##ON DOING THIS, A NEW RECORDING WILL BE CREATED BY THE NAME "recording_new.wav"

obj_new=wave.open("recording_new.wav", "wb")

obj_new.setnchannels(obj.getnchannels())
obj_new.setsampwidth(obj.getsampwidth())
obj_new.setframerate(obj.getframerate())
obj_new.writeframes(frames)

obj_new.close()      

