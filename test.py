'''
s = 0

for i in range(-10,0,3):
    s += ((i)**((((-i)*2)+1)/3))
print(s)

s = 0
for i in range(7,0,-2):
    s += (-((i*3-1)/2))**i 
print(s)

s = 0
for i in range(4):
    s += (-(3*i+1))**(2*i+1)
print(s)

s=0
for i in range(1,5,1):
   s += (-((1+i*3)-3))**(2*i-1)
print(s)

n = eval(input('n:'))

for i in range(2,n):
    if n%i == 0:
        print('no')
        break
    
if i == n-1:
    print('yes')

s = 0
for i in range(1,7):
    s += (2*i-1)*(-1)**(i+1)*(3)**(i-1)

print(s)

n = int(input("請輸入一個整數 n: "))

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
'''
rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    
    # Print asterisks
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line after each row
    print()
'''
'''
n = eval(input())
for i in range(n, 0, -1):
        # Inner loop for leading spaces in each row
        for j in range(n - i):
            print(" ", end="")
        # Inner loop for printing asterisks in each row
        for k in range(2*i - 1):
            print("*", end="")
        # Move to the next line after each row
        print("\r")

rows = eval(input('rows:'))  # Number of rows in the pyramid

for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    
    # Print asterisks
    for k in range(i + 1):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()

rows = 5  # Number of rows in the pyramid

for i in range(rows):
    # Print leading spaces
    for j in range(i):
        print(" ", end="")
    
    # Print asterisks
    for k in range(rows - i):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()

n = int(input())

if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    N1 = 1
    N2 = 1
    for i in range(2, n + 1):
        N3 = N1 + N2
        N1 = N2
        N2 = N3
    print(N3)
'''
import random

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

while 1:
    x = random.randint(1,100)
    y = random.randint(1,100)
    arithmetic = input('加法或減法')
    if arithmetic == '加法':
        ans = eval(input(x,'+',y,'=?'))
        ANS = add(x,y)
        if ans == ANS:
            print('答對了')
        else:
            print('答錯了')
    elif arithmetic == '減法':
        ans = eval(input(x,'-',y,'=?'))
        ANS = sub(x,y)
        if ans == ANS:
            print('答對了')
        else:
            print('答錯了')



