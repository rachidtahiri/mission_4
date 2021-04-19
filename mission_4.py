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