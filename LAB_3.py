#Zad 1
#a
'''a=["Olek","Maksym","Michał","James"]
a.sort()
for i in a:
    print(i,end=" ")
#b
a.append("Patycja")
a.append("Marek")
a.pop(-1)
print(a.pop(-1))
for i in a:
    print(i,end=" ")
#c
a.insert(2,"Jakub")
for i in a:
    print(i,end=" ")
#d
a.reverse()
for i in a:
    print(f"{i}{" " *1}{i}{" " *1}",end="")'''
#2
#a
'''print("")
a=input("Podaj tekst")
b=list(a.lower())
print(sorted(b))
alfabet=list("abcdefghijklmnopqrtuvwxyz")
for i in alfabet:
    if i not in a:
        print(i,end=" ")
#b
print("")
b.sort()
c=b[1::2]
print(c)'''
#c

'''
print("")
a=input("Podaj tekst")
a=a.split(" ")
print(a)
m=list(a[0])
print(m)
for i in a:
    m=list(i)
    m[0]=m[0].upper()
    m[-1]=m[-1].upper()
    result="".join(m)
    print(result,end=" ")'''
#d
'''
a=input("Podaj tekst")
a=a.split(" ")
print(a)
mal=""
lon=0
print(len(a[0]))
k=[]
b=max(a, key=len)
for i in a:
    if i!=b:
        if len(i)==len(b):
            k.append(i)
            k.append(b)
print("najdłuższe słowo"," ".join(k),"jego długość",len(b))'''
#e
'''
a=input("Podaj tekst")
b=list(a)
for i in range(len(b)):
    if b.count(b[i])>=2:
        b[i]="@"
print(b)'''
#3
'''a=input("Podaj tekst")
v=list(a.lower().replace(" ", ""))

if v==v[::-1]:
    print("palindrom")
else:
    print("nie")'''
#4

'''import random
n=int(input("Padaj liczbe elementów"))
x=int(input("Podaaj maksymalną długość ciągu znaków"))
h=[]

alfabet=list("abcdefghijklmnopqrtuvwxyz")
for i in range(n):
    w=""
    lenght=random.randint(1, x)
    for i in range(lenght):
        l=random.choice(alfabet)
        w+=l
    h.append(w)
h=tuple(h)
print(h)
#a
suma=0
for i in h:
    suma+=len(i)
print(suma)
#b
y=[]
for i in h:
    b=list(i)
    y.extend(b)
print(y)
print(y.count("k"))
#d
con=0
s=int(input("Podaj ile musi byc s"))
for i in h:
    if len(i)>s:
        con+=1
print(con)'''
#e
'''u=["ktktkt","ktr","ktkt","tyh"]
iloszcz=0
for i in u:
    iloszcz+=i.count("kt")
print(iloszcz)'''
#5
'''slownik={"piwo":4,"wino":5,"lays":9,"ser":7}
z=""
e=0
for i in slownik:
    z+=i+" "
    e+=slownik[i]
    print("Za",i,"zapłaciliśmy",slownik[i])
print("Za",z.strip(),"zapłaciliśmy",e)'''
#6

'''miesiecy={"grudzien":40,"styczen":50,"mart":90,"kwiecen":70,"czerwiec":30,"lipiec":60}
lun=0
sred=0
mil=0
for i in miesiecy:
    sred+=miesiecy[i]
    if miesiecy[i]>lun:
        lun=miesiecy[i]
sred=sred/len(miesiecy)
print(lun)
print(sred)
for i in miesiecy:
    if miesiecy[i]<lun:
        lun=miesiecy[i]
print(lun)
#b

if next(reversed(miesiecy.values()))>sred:
    print("Trzeba zacisnąć pasa")
else:
    print("„Wszystko okay")'''
#7
import random
zbior=set()
zbior2=set()
a=random.randint(3,7)
b=random.randint(3,7)
for i in range(a):
    h=random.randint(0,10)
    zbior.add(h)
print(zbior)
for i in range(b):
    h=random.randint(0,10)
    zbior2.add(h)
print(zbior2)
#a
print(5 in zbior)
#b
if zbior.issubset(zbior2):
    print("zbior jest podzbiorem zbioru2")
else:
    print("zbior nie jest podzbiorem zbioru2")
#c
if zbior2.issubset(zbior):
    print("zbior2 jest podzbiorem zbioru")
else:
    print("zbior2 nie jest podzbiorem zbioru")
#d
print(zbior.union(zbior2))
#e
print(zbior-zbior2)
#f
print(zbior2-zbior)
#g
print(zbior.intersection(zbior2))
#h
print(max(zbior.union(zbior2)))
#i
zbior3=list(zbior)
n=zbior3.pop(0)
print(n)
zbior2.add(n)
zbior=set(zbior3)
print(zbior)
print(zbior2)
#j
zbior2=zbior2.union(zbior)
print(zbior2)
#k
zbior.clear()
zbior2.clear()
print(zbior)
print(zbior2)
