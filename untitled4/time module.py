import time
time.time()
def numbers(max):
    time1 = time.time()
    for i in range(0,max):
        print(i)
        time2 = time.time()
        print(str(time2-time1))

numbers(300)


print(time.asctime())

tup = (2000, 10 ,15 ,8 ,45 ,12 ,6, 0, 1)
print(time.asctime(tup))

print(time.localtime())
t= time.localtime()
year = t[0]
day = t[2]
month = t[1]
print(year)
print(day)
print(month)

for i in range(0,5):
    print(i)
    time.sleep(1)




