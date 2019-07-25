if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isdigit = False 
    islower = False 
    isupper = False

    for i in s:
        if i.isalnum():
            isalnum = True
            break
    print(isalnum)
    for i in s:
        if i.isalpha():
            isalpha = True
            break
    print(isalpha)
    for i in s:
        if i.isdigit():
            isdigit = True
            break
    print(isdigit)
    for i in s:
        if i.islower():
            islower = True
            break
    print(islower)
    for i in s:
        if i.isupper():
            isupper = True
            break
    print(isupper)
