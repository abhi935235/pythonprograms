# cook your dish here
number=int(input("Enter number:\n"))
sum=0
temp=number
while temp>0 :
    digit = temp % 10
    sum += digit ** 3
    temp = temp//10 
print(sum)
if number == sum:
    print("Armstrong number")
else:
    print("Not an armstrong")

    
