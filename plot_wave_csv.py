import matplotlib.pyplot as plt
import numpy as np
import wave




def plot_wave(file_name_in):

    file_name = file_name_in + ".wav"

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

    data_read = wf.readframes(chunk_size)
    data_src = np.frombuffer(data_read, "int16")
    data = data_src/amp

    data_amp = data_src*0.01

    # print(data_src)


    # time axis
    size = float(chunk_size)
    x = np.arange(0, size/fr, 1/fr)

    # print("channel Count :", channels)
    ### out, 2
    ### Stereo


    """

    # multi channels
    for i in range(channels):
        plt.plot(x, data[i::channels])
        # plt.plot(x, data_amp[i::channels])

        print("i :", i)

        x_len = len(x)
        print("x length :", x_len)
        ### out, 1323000
        ### 1323000 = 30 * 44100

        print("data", data)
        print("- - -")

    """



    # Single
    plt.plot(x, data[0::channels])
    plt.plot(x, data[1::channels])



    x_len = len(x)
    print("x_length :", x_len)
    ### out, 1323000
    ### 1323000 = 30 * 44100



    # 0 - 899
    # 30 sec x 30 FPS
    count = 0

    path_csv = file_name_in + ".csv"
    print(path_csv)


    CSV_data = []
    CSV_data.append("j, count, amp,\n")


    data_zero = data[0::channels]

    for j in range(x_len):
        # print("j :", j)

        if (j%1470 == 0):

            # print("count :", count)
            # print("count :", count, ", j :", j)
            # print("data : ", data_zero[j])
            temp = str(j) + "," + str(count) + "," + str(data_zero[j]) + ",\n"
            # print(temp)
            CSV_data.append(temp)

            count += 1



    with open(path_csv, mode='w') as f:
        f.writelines(CSV_data)




    print("- - -")

    print(data[0::channels])
    print(data[1::channels])

    # print("data :", data)
    # print("data shape :", data.shape) # data shape : (2646000,)
    # print("data shape(0) :", data[0::channels].shape) # data shape(0) : (1323000,)
    # print("data shape(1) :", data[1::channels].shape) # data shape(0) : (1323000,)

    print("- - -")

    print(data)
    print(data_zero)
    print(data_zero[1322999])





    print("- - -")






    title = "Plot Wave - " + '"' + FILE + '.wav"'

    plt.title(title)
    plt.xlabel("Times [Sec]")
    plt.ylabel("standardizes amplitude")

    plt.ylim([-2, 2])
    # plt.ylim([-500, 500])

    plt.show()





# FILE = "drum_machine_30"
FILE = "60_62_64"
# FILE = "nene_2"
in_path = "data/" + FILE


plot_wave(in_path)