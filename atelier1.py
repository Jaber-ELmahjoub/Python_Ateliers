#Exercice 1:

def fact(i):                    # Definir la fonction factoriel
    if i==0:
        return 1
    else:
        return (i*(fact(i-1)))

lim=int(input("Enter number of terms: "))
sum=0
for i in range (1,lim+1):           # Boucle qui compte la somme de chaque partie et les partie precedente.
    sum=sum+fact(i)/i

print("the sum of the serie is: ",sum)    #Affichage du resultat


# Exercice 2:

# programme qui converti un nombre du decimal en binaire

def conv(x):
    if x>1:                     # condition pour prendre les elements different de 0 et 1
        conv(x//2)
    print(x % 2,end=" ")        #affichage du reste de la division pour avoir 0 ou 1

x=int(input("entrer la valeur de x:")) #affichage du resultat
conv(x)


# exercice 3:

def sum(x):
    if x==1:                    # condition d'arret pour la fonction recursive elle retourne 0 ou 1
        return 1
    elif x<=0:
        print("entrer un nombre positive") # demander de l'utilisateur de taper une valeur positive
    else:
        return (x+sum(x-1))            #Retun la somme des entiers precedents
x=int(input("entrer un nombre positive: "))
print(sum(x))

# Exercice 4:

def fibo(n):
    if n==0:               # condition d arret pour la fonction fibonacci
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)   # L'qppelle à nouveau de la fonction fibo

a=int(input("Veuiller entrer un nombre de 1 à n: "))
print("Votre suite fibonacci est:")
for i in range(a):                  # Boucle pour parcourire les elements precedents
    print(fibo(i),end=" ")          # Affichage de resultat

# Exercice 5:

def combien(x):
    if x//10==0:            # on fait la division par 10 puis on incremente 1 chaque fois
        return 1
    else:
        return 1+combien(x/10)

n=int(input("Entrer votre nombre:"))
print("votre nombre contient:",combien(n),"chiffres")

# Exercice 6:
#Programme qui compare deux elements adjacents et les inversent dans le sens croissant en utilisant deux boucles qui parcourent la liste

def bull_tri(x):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j]>x[j+1]:
                r=x[j]
                x[j]=x[j+1]
                x[j+1]=r
    print(x)
x=[98, 22, 1, 89, 4, 75, 0, 2]
bull_tri(x)

# Exercice 7:

def rev(a):
    b=[]                                # creer une liste vide.
    for i in range(len(a)):
        b.append(a[-i-1])              # on ajoute chaque fois les caracteres dans la liste B
        b[i]=a[-i-1]                    # on remplace les elements de la liste a dans b

        print(b[i],end=" ")
a=str(input("Enter votre chaine de caractere: "))
rev(a)

# Exercice 8:

def freq(x,n):
    return x.count(n)        # on retourne le count du chaine de caractere et on le stoke dans x
x=str(input("entrer votre chaine de caractere: "))
n=str(input("entrer votre caractere:"))
print(freq(x,n))

# Exercice 9:

def trouver(e, m):
    for i in range(len(m)):         # boucle i pour parcourir les index i dans len(matrice)
        for j in range(len(m[i])):  # boucle j pour parcourir les index j
            if m[i][j] == e:        # condition de trouver l element.
                return (i,j)        #return les index de e.

m=[[3,27],[-1,15],[1,2]]            #exemple de matrice donnee.
print(trouver(-1,m))



