#num = int(input())
#for i in range(1,num + 1):
#    for j in range(1,i+1) :
#        print(j, end = "")
#    print()
r = int(input())
c = int(input())

x = []
val = []


for i in r:
    for j in c:
        val.insert(j,input())
    x[i] = val

print(x)