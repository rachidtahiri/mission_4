def is_adn(s):
    """ fonction qui verifie si la chaine donné est une suite d'ADN
    """
    k=0
    tes=False
    for i in s:
        if i=="a" or i=="t" or i=="c" or i=="g" or i=="A" or i=="T" or i=="C" or i=="G" :
            k=k+1
    if k==len(s) and k!=0:
       tes=True
    return (tes)

def liste(S):
    """ fonction qui transforme une chaine à une liste de chaines de caractères
        pre: prendre une chaine de caractère 'S'
        post: avoir une liste de chaine de caractères'c'"""
    c=[]
    for i in range(len(S)):
        c=c+[S[i:i+2]]
        if i >=(len(S)-2):
            break
    return(c)
def position(l,a):
    """ fonction qui compare la variable 'a' avec les caractères de la liste de chaine de caractères 'l'
        pre: prendre une liste de chaine de caractères 'l' et 'a'
        post: avoir les positions où 'a'== 'l[i]' """
    Q=liste(l)
    P=[]
    for i in range(len(Q)):
        if a==Q[i] or a.upper()==Q[i] or a.lower()==Q[i]:
                P=P+[i]   
    return(P)

def distance_h(A,B):
    """ fonction qui calcule la distance de hamming
        pre: prend deux chaine de carractere 'A'et'B'
        pot:retourne le nombre de possition ou les carracters sont different"""
    if len(A)!=len(B):
        return("none")
    else:
        dis=0
        for i in range (len(A)):
            if A[i]!=B[i]:
                dis+=1
        return (dis)
    
def distance_matrice(L):
    """ fonction qui calcule la distance de hamming dans une liste de chaine de chaine de carractères
        pre: prendre une liste de chaine de carractères
        post: terourner une matrice de position"""
    P=[]
    for i in range (len(L)):
        C=[]
        for j in range(len(L)):
            C.append(distance_h(L[i],L[j]))
        P=P+[C]
    return (P)