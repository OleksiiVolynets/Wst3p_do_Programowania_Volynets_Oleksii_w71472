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
'''file=input("Podai nazwe failu ")
print(file.endswith(".xls"))'''
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
#1
#a
'''for i in range(1,101):
    print(i)'''
#b
'''d=100
for i in range(1,102):
    print(d)
    d-=1'''
#c
'''for i in range(7,78,7):
    print(i)'''
#d
'''for i in range(20,-1,-2):
    print(i)'''
#2
'''a=int(input("Podaj długość strony kwadrata "))
for i in range(a):
    print(a*"* ")'''
#3
'''a=int(input("Podaj długość strony trójkąta "))
j=1
while j!=a+1:
    print(j*"* ")
    j+=1'''
#4
'''a=int(input("gvvlvh"))
for j in range(a):
    print((a-1-j)*" ",end="")
    for i in range(j+1):
        print("*",end=" ")
    print("")'''
#5
'''tekst = "Rzeszów jest piękny"
print(tekst[0],tekst[-1])'''
#6
'''a="Python jest super"
print(a[0])
print(a[-1])
print(a[0: :2])
print(a[1: :3])
print(a[10: ])
print(a[ : :-1])'''
#7
#a
'''a=input("Jak masz na imię ")
print("Witaj "+a)'''
#b
'''b=float(input("Ile masz lat "))
print("Twój wiek to ",b)'''
#c
'''a=input("Jas się nazywasz ")
a.split(" ")
print(a[0]+a[a.find(" ")+1])'''
#d
'''a=input("tekst ")
for i in range(5):
    print(a)'''
#e
'''a=input("tekst ")
b=input("tekst2 ")
c=a+" "+b
print(c)'''
#f
'''a=input("tekst ")
b=input("tekst2 ")
a1=len(a)//2
b1=len(b)//2
c=a[ :a1]+b[b1: ]
print(c)'''
#8
'''x=-4
while x<=4:
    y=2*x**2-5*x-8
    print(y)
    x+=0.5'''
#9
'''while True:
    a=int(input("podaj liczbę całkowitę "))
    if a>=0:
        print(a)
    else:
        break'''
#10
'''a=int(input("podaj 1 liczbe"))
b=int(input("Podaj 2 liczbę"))
c=max(a,b)
d=min(a,b)
while d<=c:
    print(d)
    d+=1'''
#11
'''a=int(input("podaj 1 liczbe"))
b=int(input("Podaj 2 liczbę"))
c=max(a,b)
d=min(a,b)
while d<=c:
    if d%2==1:
        d+=1
        continue
    print(d)
    d+=1'''
#12
'''n=int(input("Ile są studentów "))
d=0
k=0
while d<n:
    d+=1
    c=float((input(f"Ile ptrzymał {d} studenr")))
    k+=c
print(k/n)'''
#13
'''n=int(input("Ile są studentów "))
d=0
k=0
while True:
    if d==n:
        break
    c=float((input(f"Ile ptrzymał {d} studenr")))
    if c<0 or c>100:
        continue
    d+=1
    k+=c
print(k/n)'''
#14
while True:
    a=float(input("Podaj liczbe"))
    if a<0 or a%1!=0:
        continue
    print("Liczba jest dodatnia")