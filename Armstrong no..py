num = int(input("Enter a number: "))
temp = num
power = len(str(num))
sum_num = 0

while temp > 0:
    digit = temp % 10
    sum_num += digit ** power
    temp //= 10

if sum_num == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
    
