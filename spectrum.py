import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import random
import wave

def load_wave(file_name):

    # open file
    wf = wave.open(file_name, "r")
    channels = wf.getnchannels()
    fr = wf.getnframes()

    # load wave data
    chunk_size = fr
    amp = (2**8) ** wf.getsampwidth()/2

    data = wf.readframes(chunk_size)
    data = np.frombuffer(data, "int16")
    data = data/amp
    data = data[::channels]

    return data


def load_fft(FILE ,size):

    hammingWindow = np.hamming(size)
    fr = 44100 ###
    d = 1.0 / fr
    freqList = np.fft.fftfreq(size, d)


    FILE_r = "data/" + FILE + ".wav"
    FILE_t = "Spectrum - " + FILE + ".wav"

    wave = load_wave(FILE_r)
    windowedData = hammingWindow * wave[0:size]
    data = np.fft.fft(windowedData)
    data = data/max(abs(data))
    plt.plot(freqList, abs(data))

    plt.axis([0, fr/16, 0, 2])
    plt.title(FILE_t)
    plt.xlabel("Frequency [Hz]"), plt.ylabel("Amblitude Spectrum")
    plt.show()
    plt.savefig("Graph/Graph.png")

    return data


load_fft("Everything_affair", 1024)