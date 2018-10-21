import datetime
import time


def task():
    for i in range(1000):
        for j in range(1000):
            temp = i*j

    # now = datetime.datetime.now()
    # now.strftime("%Y/%m/%d %H:%M:%S")
    # print(now)



a = 0.5
# a = 1/30

while True:
    start = time.time()

    task()
    time.sleep(a)

    elapsed_time = time.time() - start
    print ("elapsed_time : {0}".format(elapsed_time) + "[sec]")


"""
elapsed_time : 0.7485780715942383[sec]
elapsed_time : 0.7638468742370605[sec]
elapsed_time : 0.7349748611450195[sec]
elapsed_time : 0.7522351741790771[sec]
elapsed_time : 0.7669477462768555[sec]
elapsed_time : 0.7706260681152344[sec]
elapsed_time : 0.7379779815673828[sec]
"""