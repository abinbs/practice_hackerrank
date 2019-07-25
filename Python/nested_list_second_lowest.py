marksheet=[]
scorelist=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scorelist+=[score]


    scorelist = list(dict.fromkeys(scorelist))
    b=sorted(scorelist)[1] 

    for a,c in sorted(marksheet):
        if c==b:
            print(a)
