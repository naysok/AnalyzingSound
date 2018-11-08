import numpy as np
import matplotlib
# matplotlib.use("Agg")
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
    data_fft = np.fft.fft(windowedData)
    data = data_fft/max(abs(data_fft))
    plt.plot(freqList, abs(data))


    print("- - -")

    print("freqList :", freqList)
    # freqList : [   0.           43.06640625   86.1328125  ... -129.19921875  -86.1328125  -43.06640625]
    print("freqList.shape :", freqList.shape)
    # freqList.shape : (1024,)
    print("freqList-max :", max(freqList))
    print("freqList-min :", min(freqList))


    print("- - -")

    ### data, complex number object
    print("data :", data)
    print("data-max :", max(data))
    print("data-min :", min(data))
    # data-max : (0.8412934520702613-0.5175121771504375j)
    # data-min : (-0.7669665321635293-0.6416871032996144j)


    print("- - -")

    ### abs
    data_abs = abs(data)

    print("data_abs :", data_abs)
    print("data_abs-max :", max(data_abs))
    print("data_abs-min :", min(data_abs))
    # data_abs-max : 1.0
    # data_abs-min : 0.00168513736161361


    print("- - -")



    # plt.axis([0, fr/16, 0, 2])
    plt.axis([0, 4096, 0, 2])
    # plt.axis([-4096, 4096, 0, 2])
    plt.title(FILE_t)
    plt.xlabel("Frequency [Hz]"), plt.ylabel("Amblitude Spectrum")
    plt.show()
    # plt.savefig("Graph/Graph.png")

    return data


load_fft("Everything_affair", 1024)