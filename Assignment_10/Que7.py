a=int(input("Enter input "))
a=2*a
if a%2==1:
    a-=1
for i in range(a,0,-2):
    print(i,end=' ')