import time


def heapsort(array):
    start = time.perf_counter()



    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "Heapsort for "+ str(len(array)) + " elements took "+ str(round(finalTime,3))+" miliseconds"
