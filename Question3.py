def Som(l1):
    S=0
    for i in range(len(l1)):
        S=S+l1[i]
    return(S)
def Mul(l2):
    P=1
    for i in range(len(l2)):
        P=P*l2[i]
    return (P)            
LP=[]
LS=[]
x=int(input("Donner la taille de la liste "))
for i in range(x):
    y=int(input("Donner les élémant de la liste "))
    if i%2==0:
        LS.append(y)
    else :
        LP.append(y)    
print(Som(LS))
print(Mul(LP))