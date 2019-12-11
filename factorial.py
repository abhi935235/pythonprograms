# cook your dish here
number=int(input())
fact=1
if number==1:
    print("0")
else:
    while number >= 1 :
        fact*=number
        number=number-1
    print(fact)
