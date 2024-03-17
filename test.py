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