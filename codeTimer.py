#code by SukhoiSuperior
#importing libraries
import time

#Timer logging
startingTime,startingTime2 = time.perf_counter_ns(), time.perf_counter_ns()

##########START CODE########

#your code here

###########END CODE#########

#Timer end + calculation
endingTime,endingTime2 = time.perf_counter_ns(), time.perf_counter_ns()
print()
print(f"|Start time: {(startingTime+startingTime2)/2}| Ending time: {(endingTime+endingTime2)/2}| Time Taken: {((endingTime-startingTime)+(endingTime2-startingTime2))/2}|Mode: Performance Counter [Nanoseconds]|")
#Repeated twice due to inaccuracies in logging of time