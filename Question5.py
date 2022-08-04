def Formule(D):
    C=50
    H=30
    P=2*C*D
    Div=P/H
    Q=Div**0.5
    Pr=Q-int(Q)
    if Pr>0.5 :
        Q=int(Q)+1
    else :
        W=Q-Pr
        Q=int(W)
    return (Q)
x=int(input(("Donner la valeur de D : ")))
print(Formule(x))
            
