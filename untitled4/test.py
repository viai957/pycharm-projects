#Prime numbers
number = int(input("Enter a number :"))
i= 2
while number < i :
    prime = number % number
    if prime == 0:
        flag =1
        print("Its a prime number")
        if prime != 0:
            flag = 0
            print("Its not a prime number")
    i = i+1


    