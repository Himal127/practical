print("enter any 4 digit no.")
num = int(input())
a = num % 10
num = num // 10
b = num % 10
num = num //10
c = num % 10
d = num // 10
reverse = a*1000 + b*100 + c*10 + d
print(reverse)