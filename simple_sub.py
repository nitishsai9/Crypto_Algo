import string

upp= string.ascii_uppercase
low=string.ascii_lowercase
uppkey=input()
lowkey=input()
plainTxt=input()
encTxt=""
for i in plainTxt:
    if i in upp and i.isupper():
        encTxt+=uppkey[upp.find(i)]
    elif i.islower() and i in low:
        encTxt+=lowkey[low.find(i)]
    else:
        encTxt+=" "


print(encTxt)
