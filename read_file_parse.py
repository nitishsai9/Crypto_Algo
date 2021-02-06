fp=open("hel.txt","r")
x=input()
c={}
answer = {"name":[],"town":[],"country":[],"education":[],"age":[]}
for line in fp:
    if len(line.strip().split(':'))==2:
        v,k=line.strip().split(':')
        newv=v.replace("-","")
        if k.strip()=="":
            k=v
            newv="name"
        answer[newv.strip()].append(k.strip())

if x in answer:
    for i in answer[x]:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    for i in c:
        print(i,c[i])
else:
    print("-1")



fp.close()