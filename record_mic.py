import pyaudio 
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("Start Recording...")
seconds = 8
frames=[]
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):##The loop runs for a specific number of iterations, each time capturing a chunk of audio data (of size FRAMES_PER_BUFFER) and storing it in the frames list. After the loop completes, the frames list will contain all the captured audio data chunks, which can then be processed, saved, or played back.
    data=stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj=wave.open("output.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()