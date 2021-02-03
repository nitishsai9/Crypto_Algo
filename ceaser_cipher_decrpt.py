import string

enctxt=input()


def decrypt(key,enctxt):
    plaintxt=""
    for i in enctxt:
        if i.islower():
            plaintxt+= chr(((ord(i)-key - ord('a'))%26)+ord('a'))
        else:
            plaintxt+= chr(((ord(i)-key - ord('A'))%26)+ord('A'))
    
    return plaintxt





for key in range(0,26):
    print(key, decrypt(key,enctxt))

