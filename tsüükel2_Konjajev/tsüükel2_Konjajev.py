#Ülesanne 11 Arvamismäng
from math import *
from random import * 

#Работа стаса 1.
positive=0
negative=0
a=1
while True:
    a=int(input("Sisestage number: "))
    if a>0: positive+=a
    elif a<0: negative+=a
    else: break
print("Positiivne", positive, "Negatiivne", negative)
print()


#Работа Стаса 2.
n=int(input("Sisestage number n: "))
for i in range(1,11):
    print(f"{n} * {i} ={n*i}")
print()


# Работа Полины
print("Sa pead ära juhuslikult mõistatatud arvu (1-50). 10 katsega")
r=randint(1,50)
n=1
while n<=10:
    o=int(input("Sisesta arv: "))
    if o==r:
        print(f"Sa arvasid et sul läks {n} katset.")
        break
    elif r>o:
        print("Väga väike")
    elif o>r:
        print("Väga suur")
    n=n+1
print()


#0 Работа Майкла
while True:
    print("Tere Tulemsat!")
    try:
        print("Latte, 2.25 eurot")
        print("Espressi, 2 euro")
        print("Capuccino, 3 euro")
        print("kakao, 2.20 euro")
        hind=float(input("Vali hind: "))       
        if hind<2 or hind>3:break
        m=input("Valige makseviis: ")
        if m.lower()=="sularaha":
            print("anna raha"); summa=float(input())
        if summa==hind:
            print("see ye")
        elif summa>hind:
            tagaraha=summa-hind
        else:
            tagaraha1=hind-summa
        print(f"Teie tagaraha: ", tagaraha)
        if m.lowwer=="kaardiga":
            n=int(input("sisestage kaardi number: "))
            print(n,"selle kaardiga on tehtud makse")

    except:
        print("")
print()
#1 Работа Артема Под.
p=0
while True:
    number= int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >= 10:
        print("Õigest")
        break
    else:
        print("Arv on liiga väike",p)
print("katsed", p)
print()

#22 Работа Арема Под.
print("Ma tah kommi")
katsed=0
while True:
    answer=input("Tahan kommi")
    katsed+=1
    if answer.lower()=="kommi":
        print(f"Teil kommid kirjutakse kulus {katsed} katse.")
        break
print()

#22.1
katsed=0
answer=""
while answer!="komm":
    answer=input("Taham kommi!")
    katsed+=1
print(f"Katsed: {katsed}")
print()

#11 ülesane
print("Arvuti mõistatab numbrit 1-10 ja sina üritad seda ära arvata.")
a=randint(1,10)
vastus=int(input("mis arv on mõistatanud arvutit?: "))
k=p=1
while vastus!=a:
    print("Ära sa ei arvanud ära, proovi uuesti!: ")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    p+=1
    if k>2: 
        print("Püüdlused on lõppenud")      
        b=input("Kas proovi veel kord: ")
        if b.upper()=="JÄH":
            k=0
            continue
        else:
            break
if vastus==a:
     print("Palju õnne, sa arvasid ära!",p )
     
print()

#Mõtle ise välja ülesanne, mis on vaja lahendada while tingimusega/while True/for kasutades. Lahenda nii while kui ka for abil.
while True:
    a=input("Kas sa tahad endale uue arvuti osta?: ")
    if a.upper()=="JÄH" or a.upper()=="EI": break
if a.upper()=="JÄH":
    while True:
        c=input("Kas tahad mänguarvutit või tavalist?: ")
        if c.upper()=="MÄNGUARVUTIT" or c.upper()=="TAVALIST": break
    if c.upper()=="MÄNGUARVUTIT":
        while True:
            try:
                a1=float(input("Kui palju maksab korpus, mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        while True:
            try:
                a2=float(input("Kui palju maksab protsessor, mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        while True:
            try:
                a3=float(input("Kui palju maksab videokaart, mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        while True:
            try:
                a4=float(input("Kui plaju maksab emaplaat, mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        while True:
            try:
                a5=float(input("Kui plaju maksabmälu mida soovite osta?: "))               
                break
            except: 
                print("TypeError")
        hind5=a1+a2+a3+a4+a5 
        print(f"Teie arvuti maksab: {hind5}")
    else:
        print("Me müüme ainult mänguarvuteid")
else:
    print("nagemist")
print()



#1 ülessane 6
for x in range(5):
    print("*****")

#1 ggggg
for i in range(1, 11):
    print("*"*i, end="")
    print()

for i in range(1,5):
    x=str("*"*i).center(18," ")
    print(x, end="") 
    print()
for i in range(1,7):
    x=str("*"*(i+2)).center(18," ")
    print(x, end="") 
    print()
