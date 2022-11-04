# @author Joep Demollin
# @date 2022-11-04

import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from io import createInput, readInput, writeOutput
from bruteforce import bruteforce

def callMultipleTimes():
    sizes=[2,4,8,16,32,64,128,256,512,1024,2048,4096]
    timeCorrelation = dict()
    for i in sizes:
        timeCorrelation[i] = []
        for j in range(20):
            createInput(i)
            edges = readInput

            start = time.perf_counter()
            intersections = bruteforce(edges)
            end = time.perf_counter()

            writeOutput(intersections)
            timeCorrelation[i].append(end-start)
    
    sum = 0
    for i in timeCorrelation:
        for j in timeCorrelation[i]:
            sum += j
        sum = sum/len(timeCorrelation[i])
        timeCorrelation[i] = sum

    plt.plot(list(timeCorrelation.keys()), list(timeCorrelation.values()))
    plt.title('Advanced sweep line algoritme')
    plt.xlabel('Hoeveelheid cirkels')
    plt.ylabel('Tijd (s)')
    plt.show()


callMultipleTimes()