for i in range (0,5):
    for a in range (0, 5):
        print(a)


print ("-----------------------------")

#prime number
#using nested if
for  i in range(2,30):
    j =2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j =j+1
    else:
        j = j +1
        if counter == 0:

            print(str(i)+ "is prime number")

        else:
            counter = 0

