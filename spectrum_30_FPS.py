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
    fr_30 = int(fr/30)
    d = 1.0 / fr
    freqList = np.fft.fftfreq(size, d)

    print("freqList :", freqList)

    FILE_r = "data/" + FILE + ".wav"


    wave = load_wave(FILE_r)

    for i in range(1323000):
    # for i in range(10000): # debug


        if (i%1470 == 0):

            frame_i = int(i/1470)
            num = "%05d" % frame_i

            FILE_t = "Spectrum - " + FILE + ".wav - " + num
            FILE_out = "Graph/" + FILE + "-" + num + ".png"

            windowedData = hammingWindow * wave[i:i+size]

            data_fft = np.fft.fft(windowedData)
            data_src = abs(data_fft*10)
            print(data_src)

            data_max = data_fft/max(abs(data_fft)) # 正規化？

            # plt.plot(freqList, abs(data_max))
            plt.plot(freqList, abs(data_src))
            # plt.bar(freqList, abs(data_src))


            # plt.axis([0, fr/16, 0, 2])
            # plt.axis([0, 4096, 0, 2])
            plt.axis([0, 4096, 0, 1000])

            plt.title(FILE_t)
            plt.xlabel("Frequency [Hz]"), plt.ylabel("Amblitude Spectrum")
            plt.show()
            plt.savefig(FILE_out)
            plt.clf()

            print(str(i))

    # return data


load_fft("Cluster_A_30", 1024)


print("Finish!!")