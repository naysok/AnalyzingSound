import matplotlib.pyplot as plt
import numpy as np
import wave


def plot_wave(file_name):

    # opnen wav file
    wf = wave.open(file_name, "r")
    channels = wf.getnchannels()
    fr = wf.getframerate()
    fn = wf.getnframes()
    time_sec = 1.0*fn/fr
    time = time_sec

    # load wave
    chunk_size = int(fr*time)

    amp = (2**8)**wf.getsampwidth()/2

    data = wf.readframes(chunk_size)
    data = np.frombuffer(data, "int16")
    data = data/amp


    # time axis
    size = float(chunk_size)
    x = np.arange(0, size/fr, 1/fr)

    # multi channels
    for i in range(channels):
        plt.plot(x, data[i::channels])

    title = "Plot Wave - " + '"' + FILE + '"'

    plt.title(title)
    plt.xlabel("Times [Sec]")
    plt.ylabel("standardizes amplitude")

    plt.ylim([-2, 2])

    plt.show()

FILE = "Everything_affair.wav"
# FILE = "nene_2.wav"
in_path = "data/" + FILE


plot_wave(in_path)