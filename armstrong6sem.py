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
    
#version 1.0
# cook your dish here
sum=0
print("Armstrong between 0 to 1000 are:")
for i in range(1000):
    temp = i
    number=temp
    while temp > 0 :
        digit = temp % 10
        sum += digit ** 3
        temp = temp//10
    if number == sum:
        print(number,end=" ")
    sum=0

    
