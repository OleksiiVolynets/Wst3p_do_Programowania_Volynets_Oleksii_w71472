#zadanie 1
'''print("zadanie1")
print(type(1+2))
print(type(1+4.5))
print(type(3 / 2))
print(type(4 / 2))
print(type(3 // 2))
print(type(-3 // 2))
print(type(11 % 2))
print(type(2 ** 10 ))
print(type(8 ** (1/3)))'''
#zadanie 2
'''print("zadanie2")
print("\n\n\n")
print(type(int(3.0)))
print(type(float(3)))
print(type(float("3") ))
print(type(str(12.4) ))
print(type(bool(0)))'''
#zadanie 3
'''print("zadanie3")
imie="Oleksii"
kierunek="programowanie"
uczelnia="WSIZ"
print(f"Nazywam sie {imie} studiuje {kierunek} na {uczelnia}")'''
#zadanie 4
'''print("zadanie4")
imie=input("Jak sie nazywasz ")
print(f"Czesc {imie}")'''
#zadanie 5
'''
print("zadanie5")
a=float(input("1 bok prostokata jest "))
b=float(input("2 bok prostokata jest "))
pole=a*b
obwod=2*(a+b)
print("pole =",pole,"obwod =",obwod,sep=" ")'''
#zadanie 6
'''print("zadanie6")
a=float(input("ile kilometrów przejechałeś? "))
b=float(input("Jakie jest średnie spalanie twojego sam(w litrach na 100 km) "))
c=6.5
bn=a/100*b
cn=c*bn
print("Тa podróż wydał ",bn,"co ci kosztuwaw",cn)'''
#zadanie 7
'''import random
b=float(input("Jakie jest średnie spalanie twojego sam(w litrach na 100 km) "))
a=random.randint(100,1000)
bn=a/100*b
c=6.5
cn=c*bn

print("Тa podróż wydał ",bn,"litrow","co ci kosztuwaw",cn,"zwotych")'''
#zadanie 8
'''a=float(input("Ile masz lat? "))
if a>=18:
    print("Jestes pewnoletni")
else:
    print("nie jestes pewnoletni")'''
#zadanie 9
'''a=float(input("Ile masz lat? "))
b=input("Czy jestes studemtem? ")
if a<4:
    cena=0
elif a>=4 and a<=17:
    cena=10
elif a>=18:
    if b=="tak":
        cena=20*0.75
    else:
        cena=20
print("Wartosc bileta",cena)'''
#zadanie 10

'''a=float(input("Podaj liczbe x "))
b=float(input("Podaj liczbe y"))
c=float(input("Podaj liczbe z"))
if b>a:
    b,a=a,b
if c>a:
    c,a=a,c
if c>b:
    c,b=b,c
print(c,b,a)'''
#11
'''a=float(input("Podaj liczbe a dla  równania kwadratowego "))
b=float(input("Podaj liczbe b dla  równania kwadratowego "))
c=float(input("Podaj liczbe c dla  równania kwadratowego "))
d=b**2-4*a*c
if d>0:
    x1=(-b+d**(1/2))/(2*a)
    x2=(-b-d**(1/2))/(2*a)
    print("rozwiązywania","x1=",x1,"x2=",x2)
if d==0:
    x=-b/(2*a)
    print("rozwiązywania","x1=",x)
else:
    print("rozwiązywania nie ma")'''
#12
#a
'''x=float(input("Podaj liczbe x "))
if x>0:
    a=2*x
elif x==0:
    a=0
else:
    a=-3*x
print("Znaczenie a(x)=",a)'''
#b
'''x=float(input("Podaj liczbe x "))
if x>=1:
    b=x**2
else:
    b=x
print("Znaczenie b(x)=",a)'''
#c
'''x=float(input("Podaj liczbe x "))
if x>0:
    c=x+2
elif x==0:
    c=8
else:
    c=x-4
print(c)'''
#13
'''a=float(input("Podai 1 liczbe"))
b=float(input("Podai 2 liczbe "))
c=input("Podaj działanie matematyczne ")
# + / // % **
match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "//":
        print(a//b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case "%":
        print(a%b)'''
#14
file=input("Podai nazwe failu ")
print(file.endswith(".xls"))
#15 
'''a=float(input("Podaj liczbe a dla  równania kwadratowego 0= ax + b "))
b=float(input("Podaj liczbe b dla  równania liniowego  0= ax + b "))
x=-b/a
print("rozwiązywania",x)'''
#16
'''a=float(input("Podaj liczbe a dla strony trójkąta "))
b=float(input("Podaj liczbe b dla strony trójkąta "))
c=float(input("Podaj liczbe c dla strony trójkąta "))
p=(a+b+c)/2
P=(p*(p-a)*(p-b)*(p-c))**(1/2)
print("Obwód  trójkąta",P)'''
#17
'''a=input("Podaj litere krora jest duża czy mała ")
# b=list()
# b.append(a)
# c="".join(b)
if a.isupper()==False:
    print("Litera jest mała")
else:
    print("Litera jest duża")'''
#19
'''a=input("Podaj litere krora jest duża czy mała ")

if a.isupper()==False:
    print(a.upper())
else:
    print(a.lower())'''
