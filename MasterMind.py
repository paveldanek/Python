import random

Quiz=[0,0,0,0,0]

def getnums():
    A=[0,0,0,0,0]
    for i in range(0,5):
        match=True
        while match:
            A[i]=random.randint(0,9)
            match=False
            for j in range(i,0,-1):
                if A[i]==A[j-1]:
                    match=True
    return A

def inpnums():
    Error=True
    while Error:
        Str=input("> ")
        A=[0,0,0,0,0]
        i=0
        if len(Str)!=5:
            Error=True
        else:
            Error=False
        while (i<5) and (not Error):
            if str.isdigit(Str[i]):
                A[i]=int(Str[i])
            else:
                Error=True
            i=i+1
        if not Error:
            for i in range(0,5):
                for j in range(0,5):
                    if i!=j and A[i]==A[j]:
                        Error=True
        if Error:
            print("=INVALID=")
    return A

def Xs(A,B):
    x=0
    for i in range(0,5):
        if A[i]==B[i]:
            x=x+1
    return x

def Os(A,B):
    o=0
    for i in range(0,5):
        for j in range(0,5):
            if i!=j and A[i]==B[j]:
                o=o+1
    return o

#=================== main
X=0
O=0
N=0
print("Play MasterMind! Guess 5 digits in a row! Receive X for right number")
print("at the correct spot, receive O for the right number at the incorrect")
print("spot. (To quit, press <Ctrl>+C.)")
Quiz=getnums()
while X<5:
    N=N+1
    Answ=inpnums()
    X=Xs(Quiz,Answ)
    O=Os(Quiz,Answ)
    for i in range(0,5):
        print(Answ[i]," ",sep="",end="")
    if X==0 and O==0:
        print("     NO LUCK")
    else:
        print("     ",sep="",end="")
        for i in range(0,X):
            print("X",sep="",end="")
        for i in range(0,O):
            print("O",sep="",end="")
        print("")
print("Good job! You guessed it in",N,"attempts!")



        




    
