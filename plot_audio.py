import wave
import matplotlib.pyplot as plt
import numpy as np

obj=wave.open("audio.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave=obj.readframes(-1)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

##IF STEREO SPLIT INTO 2 CHANNELS
if obj.getnchannels() == 2:
    signal_array = np.reshape(signal_array, (-1,2)) ## signal_array = np.reshape(signal_array, (-1, 2)), 2 indicates 2 columns
    channel_1 = signal_array[:,0]
    channel_2 = signal_array[:,1]
else:
    channel_1 = signal_array

obj.close()

t_audio = n_samples/sample_freq

print(t_audio)

times=np.linspace(0, t_audio, n_samples)

if(obj.getnchannels()==2):

    # Create a figure with a specified size
    plt.figure(figsize=(15, 5))

    # First subplot for Channel 1
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
    plt.plot(times, channel_1, label="Channel 1")
    plt.xlabel("Time")
    plt.ylabel("Signal wave")
    plt.title("Channel 1")
    plt.xlim(0, t_audio)

    # Second subplot for Channel 2
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
    plt.plot(times, channel_2, label="Channel 2", color='orange')
    plt.xlabel("Time")
    plt.ylabel("Signal wave")
    plt.title("Channel 2")
    plt.xlim(0, t_audio)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

# Create a figure with a specified size
plt.figure(figsize=(15, 5))

# First subplot for Channel 1
plt.plot(times, channel_1, label="Channel 1")
plt.xlabel("Time")
plt.ylabel("Signal wave")
plt.title("Channel 1")
plt.xlim(0, t_audio)

plt.show()