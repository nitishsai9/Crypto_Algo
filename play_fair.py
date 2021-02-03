plainTxt=input("enter plain text").upper().replace(" ","")

key=input("enter Key").upper().replace(" ","")

keyMatrix=[[0 for i in range(5)] for j in range(5)]
key+="ABCDEFGHIKLMNOPQRSTUVWXYZ"
key=key.replace("J","I")

temp=[]
for i in key:
    if i not in temp:
        temp.append(i)

c=0
for i in range(5):
    for j in range(5):
        keyMatrix[i][j]=temp[c]
        c+=1

for i in range(0,len(plainTxt)-1):
    if plainTxt[i]==plainTxt[i+1]:
        plainTxt=plainTxt[:i+1]+"X"+plainTxt[i+1:]

if len(plainTxt)&1==1:
    plainTxt=plainTxt[:]+"X"
msg=[ plainTxt[i:i+2] for i in range(0,len(plainTxt),2)      ]


def find(keyMatrix,key):
    loc=[]
    for i in range(5):
        for j in range(5):
            if keyMatrix[i][j]==key:
                loc.append(i)
                loc.append(j)
    return loc
encTx=[]

for i in msg:
    p1,q1=find(keyMatrix,i[0])
    p2,q2=find(keyMatrix,i[1])
    if p1==p2:
        if q1==4:
            q1=-1
        if q2==4:
            q2=-1
        encTx.append(keyMatrix[p1][q1+1])
        encTx.append(keyMatrix[p1][q2+1])
    elif q1==q2:
        if p1==4:
            p1=-1
        if p2==4:
            p2=-1
        encTx.append(keyMatrix[p1+1][q1])
        encTx.append(keyMatrix[p2+1][q2])
    else:
        encTx.append(keyMatrix[p1][q2])
        encTx.append(keyMatrix[p2][q1])

print(encTx)

