def primes(maxe):
    """fonction qui cherche tous les nombres premiers entre # 2 et maxe#
       pre:Pour chaque nombre successif, on vérifie si on peut le diviser
       par un des nombres premiers déjà trouvés. Si non, on peut ajouter le nombre à la liste.
       post: retourner tous les nombres premiers entre 2 et maxe """
    if maxe<=0:
        l=[]
    else:
        l=[2]
        for i in range (2,maxe+1):
            k=0   #l'utilisation du compteur 'k' pour verifier si le nombre 'i' est divisible par les nombres premiers au niveau de la liste 'l'
            for j in range(len(l)):
                if i % l[j] == 0:
                    k=k+1
            if k==0:
                l.append(i)

    return(l)
"""test"""
print("l=",primes(107))