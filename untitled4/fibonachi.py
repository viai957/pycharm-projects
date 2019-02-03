# fibonachi sequence
nth_term =  int(input("Enter the nth term"))
n1= 0
n2 = 1
count = 0
if nth_term < 0:
    print("enter a positive integer")
elif nth_term == 1:
    print("fibonachi sequence upto",nth_term,":")
    print(n1)
else:
    print("Fibonachi sequence upto",nth_term,":")
    while count < nth_term :
        print(n1 , end =',')
        nth = n1 + n2
        #update value
        n1 = n2
        n2 = nth
        count = count + 1
