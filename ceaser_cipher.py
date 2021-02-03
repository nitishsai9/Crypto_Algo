
plaintxt=input()
key=int(input())
enc=""

for i in plaintxt:
    if i.islower():
        enc+=chr(((ord(i)-ord('a')+key)%26)+97)
    else:
        enc+=chr(((ord(i)-ord('A')+key)%26)+65)

print("Enc " + enc) 

