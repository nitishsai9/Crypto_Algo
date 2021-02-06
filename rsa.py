import math 
p=int(input())
q=int(input())

msg=int(input())
n=p*q

toient=(p-1)*(q-1)
e=2

while e < toient:
    if math.gcd(e,toient)==1:
        break
    e+=1
d=1
while True:
    if e*d % toient==1:
        break
    else:
        d+=1

ec=(msg**e)%n

dc=(ec**d)%n

print(ec,dc)