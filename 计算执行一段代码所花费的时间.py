import time
start_time=time.time()
for i in range(10**5):
    a,b=1,2
    c=a+b
end_time=time.time()
time_taken_in_micro=(end_time-start_time)*(10**6)
print(time_taken_in_micro)