def counte(s):
    c=0
    for j in s:
        if(j=="A" or j=="E" or j=="I" or j=="O" or j=="U"):
            c+=1
        
    return c


def minion_game(xs):
    
    k=0
    s=0
    v=counte(xs[0:len(xs)])
    c=len(xs)-v
    i=1
    for i in range(1,len(xs)+1):
        if(xs[len(xs)-i] =="A" or xs[len(xs)-i]=="E" or xs[len(xs)-i]=="I" or xs[len(xs)-i]=="O" or xs[len(xs)-i]=="U"):
            k+=v
            s+=c
            v-=1
        else:
            k+=v
            s+=c
            c-=1
        
            
        
        
        
    if(s>k):
        print("Stuart",s)
    elif(s<k):
        print("Kevin",k)
    else:
        print("Draw")
