def Maximal(m1):
    for i in range(3):
        x=int(input("Donner un entier : "))
        m1.append(x)
    maximal=int(m1[0])
    for i in range(3):
        if maximal<int(m1[i]):
            maximal=m1[i]
    return (maximal) 

M=[]
print("la valeur maximal est : ",Maximal(M))



    