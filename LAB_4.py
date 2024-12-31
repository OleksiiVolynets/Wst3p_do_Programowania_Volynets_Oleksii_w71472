#5
'''def sred(p):
    sred=0
    for i in p:
        sred+=i
    sred=sred/len(p)
    print(sred)


nums1=[5,5,7,8,3,4,2,3,-2]
sred(nums1)'''
#7
'''def troj(a,b,c):
    sred=0
    P=0
    if a>0 and b>0 and c>0:
        if max(a,b,c)!=a and min(a,b,c)!=a:
            sred=a
        elif max(a,b,c)!=b and min(a,b,c)!=b:
            sred=b
        elif max(a,b,c)!=c and min(a,b,c)!=c:
            sred=c
        if max(a,b,c)<=min(a,b,c)+sred:
            p=(a+b+c)/2
            P=(p*(p-a)*(p-b)*(p-c))**(1/2)
    print("Obwód  trójkąta",P)
a=float(input("Podaj liczbe a dla strony trójkąta "))
b=float(input("Podaj liczbe b dla strony trójkąta "))
c=float(input("Podaj liczbe c dla strony trójkąta "))
troj(a,b,c)'''
#6
'''def person(imie, wiek=20):
    """
    Ta funkcja wypisuje podane imię i wiek na ekranie.
    Parametry:
    - imie: imię użytkownika (str)
    - wiek: wiek użytkownika (int, domyślnie 20)
    """
    print(f"Imię: {imie}, Wiek: {wiek}")

imie=input("Podaj imie")
#wiek=int(input("Ile masz lat"))
person(imie)
print(person.__doc__)'''
#8
'''def fun(a,n):
    if n==1: 
        return a
    else: 
        return a*fun(a,n-1)
a=float(input("Podaj liczbe"))
n=int(input("Podaj potęgę tej liczby"))
print(fun(a,n))'''
#9
'''def fuc_krol(a):
    if a==1:
        return 0
    if a==2:
        return 1
    else:
        return fuc_krol(a-1)+fuc_krol(a-2)
a=int(input("Padaj n-ty element ciągu Fibonacci "))
print(fuc_krol(a))'''
#10   
'''def wez(p):
    n=0
    if p==1:
        n=1
        return n
    else:
        return 2*wez(p-1) +1
a=int(input("Podaj ilość dysków w weże Hanoi"))
print(wez(a))'''
#1
'''def kolo(r):
    S=0
    S=3.14*r**2
    print("Pole koła",S)
r=float(input("Padaj r koła "))
kolo(r)'''
#2
'''def trapeza(a,b,h):
    S=((a+b)/2)*h
    print("Pole trapezy",S)
a=float(input("Padaj a trapezy "))
b=float(input("Padaj b trapezy "))
h=float(input("Padaj h trapezy "))
trapeza(a,b,h)'''
#3
'''def ok(x):
    a=True if x>0 else False
    print("Czy liczba jest dodatnia?",a)
x=float(input("Podaj liczbę"))
ok(x)'''
#4
'''
def co_robi(m,h):
    c=m/(h/100)**2
    if c<18.5:
        print("Masz underweight")
    if c>18.5 and c<24.9:
        print("masz normal weight")
    if c>25 and c<29.9:
        print("Masz overweight")
    if c>30 and c<34.9:
        print("Masz obesity")
    if c>35 and c<39.9:
        print("Masz extreme obesity")
    if c>40:
        print("Co ty z sobą zrobiłeś")
m=float(input("Jaka jest twoja waga "))
h=float(input("Jaki jest twój wzrost "))
co_robi(m,h)'''
#11
'''def string(l):
    n=list(l)
    n=n[::-1]
    n="".join(n)
    print(n)
l=input("Podak tekst")
string(l)'''
#12
'''def plec(name):
    rozwiazanie={}
    for i in name:
        if i in ["Анна", "Марія", "Катерина", "Моніка", "Софія"]:
            b="жінка"
            rozwiazanie[i]=b
        elif i in ["Іван", "Петро", "Максим", "Тарас", "Олег"]:
            b="чоловік"
            rozwiazanie[i]=b
        else:
            b=0
    print(rozwiazanie)
plec(["Анна", "Петро", "Софія", "Максим", "Марія"])'''
#13
'''def zbiory(s1,s2):
    s1=set(s1)
    s2=set(s2)
    return list(s1.intersection(s2))
a=[2,5,8,6,3]
b=[9,7,5,1,8]
print(zbiory(a,b))'''
#14
'''def dz(a,b,c):
    if a%c==0 and b%c==0:
        return c
    else:
        return dz(a,b,c-1)
a=int(input("Podaj 1 liczbę"))
b=int(input("Podaj 2 liczbę"))
c=max(a,b)//2
print(dz(a,b,c))'''
#15
'''def palindr(a):
    a=a
    v=a.lower().replace(" ", "")

    if v==v[::-1]:
        print("palindrom")
    else:
        print("nie")
a=input("Podaj tekst")
palindr(a)'''
#16
'''def anagr(a,b):
    if len(a)==len(b):
        a=set(a)
        b=set(b)
        if a.issubset(b):
            print("Tak  są anagrami")
    else:
        print("nie są anagrami")
a=input("Podaj 1 słowo ")
b=input("Podj 2 słowo ")
anagr(a,b)'''
#17
def mxim(*agrs):
    maks=agrs[0]
    for i in agrs:
        if i>maks:
            maks=i
    print(maks)
mxim(2,8,6,9,2,10)    