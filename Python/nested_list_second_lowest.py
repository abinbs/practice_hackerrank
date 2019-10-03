marksheet=[] # creates a list marksheet
scorelist=[] # creates a list scorelist

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input("Entre the name:")
        score = float(input("Enter the score:"))
        marksheet+=[[name,score]]
        scorelist+=[score]


    scorelist = list(dict.fromkeys(scorelist))
    b=sorted(scorelist)[1] # Function which sorts the list in the increasing order of scores  

    for a,c in sorted(marksheet):
        if c==b:
            print(a)
