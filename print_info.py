import struct
from scipy import fromstring, int16
import wave

# read file
wave_file_name = "Everything_affair"
wave_file = "data/" + wave_file_name + ".wav"
wave_r = wave.open(wave_file, "r")

# get info
ch = wave_r.getnchannels()
width = wave_r.getsampwidth()
fr = wave_r.getframerate()
fn = wave_r.getnframes()
time_sec = 1.0*fn/fr
minites = int(time_sec // 60)
seconds = time_sec % 60

print("Channel :", ch)
print("Width :", width)
print("Frame Rate :", fr)
print("Frame num : ", fn)
# print("Param :", wave_r.getparams())
print("Tatal Time :", time_sec)
print("Total Time :", minites, "min", seconds, "sec")


#data = wave_r.readframes(wave_r.getnframes())
wave_r.close()
#X = fromstring(data, dtype=int16)