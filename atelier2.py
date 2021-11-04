#Exerice 1:

def afficher (l1,l2):
    l3=[]
    for i in l1:
        if l1.index(i)%2 ==0:       #condition de l index paire
            l3.append(i)
    for i in l2:
        if l2.index(i)%2 !=0:        #condition de l index impaire
            l3.append(i)
    print(l3)

l1=[4,8,12,16,20,24,28]
l2=[3,6,9,12,15,18,21]

afficher(l1,l2)

#Exercice 2:

def dev_inv(liste):
    v=len(liste)//3        # on devise la longuer de la liste par 3
    s=v*2
    l1=liste[:v]            #la liste l1 contient les 3 premiers elements
    l2=liste[v:s]           #la liste l2 contient les 3 suivants elements
    l3=liste[s:]            ##la liste l13 contient les 3 derniers elements
    print(l1[::-1],l2[::-1],l3[::-1])   #on affiche les 3 listes reversed

l1=[1,2,3,4,5,6,7,8,9]
dev_inv(l1)


#Exercice 3:

l=[11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
for i in l:
        if l.count(i)>1: # condition pour savoir les elements qui se repete plus de fois
            d.update({i:l.count(i)})
            del(i)           # on supprime l element pour ne pas le repeter
        else:
            d.update({i:l.count(i)})    # on ajoute un element au dictionnaire
print(d,end=" ")

#Exercice 4:

#Dans ce programme on a utilise la fonction intersection du set pour trouver set1 inter sets et puis faire la difference entre eux pour avoir la nouvelle set3
set1={23,42,65,57,78,83,29}
set2={57,83,29,67,73,43,48}
t=set1.intersection(set2)
set3=(set1-t)
print("L'intersection du deux sets est:",t)
print("La nouvelle set est: ",set3)


#Exercice 5:

a=[47,64,69,37,76,83,95,97]
d={'Khadija':47,'Imane':69,'jaber':76,'Abir':97}
b=[]
for value in d.values():    #boucle for pour parcourir les value du dictionnaire
    for i in a:
        if i==value:        #condition pour tester
            b.append(value) #ajouter les valeurs dans b
print(b,end=" ")


