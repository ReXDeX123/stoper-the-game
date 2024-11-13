import random
import time
import sys
def prime_numbers(n):
    number=[x for x in range(n+1)]
    try:
        number.pop(0)
        number.pop(0)
    except:
        pass
    for x in number:
        for i in range(2,n+1):
            try:
                a=i*x
                number.remove(a)
            except:
                continue
    for x in number:
        number.append(x*-1)
    return number
b=0
timer=0
c=0
d=0
e=0
n=0
l=0
lvl = 0
losn= 0
p=0
wyb = 0
miejski = open("miejski2.txt","r",encoding="utf-8").readlines()
miejski = str(miejski).replace("'", "").replace("\\", "").replace("[", "").replace("]", "").split(",")

while p == 0:
    a = random.randint(1,100)
    print(f"mineło {e} dni {d} godzin {c} minut {b} sekund")
    b = b + a
    if b >= 120:
        b = b - 120
        c = c + 2
    elif b >= 60:
        b = b - 60
        c = c + 1
    if c >= 120:
        c = c - 120
        d = d + 2
    elif c >= 60:
        c = c - 60
        d = d + 1
    if d >= 24:
        d = d - 24
        e = e + 1
    czas = b + (c + (d + e*24)*60)*60
    lvl = lvl + czas
    l = l+a
    g = n*1000
    if l > 1000 :
        l=0
        n = n + 1
        print(f"Wbłeś {n} LvL")
    elif czas == 2137 or czas == 4566769:
        print("Odblokowałeś papaja jaka grywalna postać")
    elif czas == 666 or czas ==443556:
        print("odblokowałeś szatana zdejmujacego gacie")
    elif n > 100:
        print("zostales timerowym sigemka")
    elif czas == 14 or czas == 196:
        print("Odblokowałeś Dissa")
    elif czas == 69 or czas == 4761:
        print("Odblokowałeś osiagniecie sex")
    elif czas == 10 or czas == 100 or czas == 100:
        print("odblokowałeś osiagniecie ona jest 10 na 10 ale cie nie lubi")
    elif czas == 2138:
        print("prawie odblokowales papaja")
    elif czas == 420:
        print("odblokwałeś weed")
    elif czas == 1337:
        print("zostales elita")
    elif czas == 9 or czas == 81 or czas == 729:
        print("you are a king of Albania")
    elif czas == 0:
        print("sigma")
    elif czas == 18002255324 or czas == 1800:
        print("odblokowales wjazd na chate przez FBI")
    elif czas == 477213657 or czas == 477212750:
        print("odblokowales wjazd na chate przez CBŚP")
    elif czas == 999 or czas == 998 or czas == 997 or czas ==112:
        print("odblokowałeś Makowca")
    elif czas == 207:
        print("odblokowałeś pegeota")
    time.sleep(1)
    liczbapr = 15 - n
    if liczbapr <= 2:
        liczbapr = 2
    los1=random.randint(1,5)
    if los1 == 1:
        losn = 0
        while losn == 0:
            losn = random.randint((n+1)*-50,(n+1)*50)
        while timer < liczbapr:
            wyb=input("jak sadzisz co wylosowala partia ")
            try:
                wyb=int(wyb)
            except:
                continue
            if wyb == losn:
                print("wygrałeś")
                timer = 0
                break
            if wyb % 2 == 0 and losn % 2 == 0:
                print("liczba jest parzysta")
            elif wyb % 2 == 1 and losn % 2 == 1:
                print("liczba jest nieparzysta")
            else:
                pass
            if wyb in prime_numbers(n=losn) and losn in prime_numbers(n=losn):
                if wyb > 0 and losn > 0:
                    print("liczba is pierwsza")
                elif wyb < 0 and losn < 0:
                    print("liczba jest ujemna liczba pierwsza")
            elif wyb not in prime_numbers(n=losn) and losn not in prime_numbers(n=losn):
                print("liczba is not pierwsza")
            else:
                pass
            if wyb > losn:
                print("liczba is too big")
            elif wyb < losn:
                print("liczba is too low")
            if losn > 0 and wyb > 0:
                print("liczba is dodatnia")
            elif losn < 0 and wyb < 0:
                print("liczba is ujemna")
            
            timer = timer +1
            if timer == liczbapr:
                p=1
                break
    los2 = random.randint(1,1)
    if los2 == 1:
        sigma=0
        loss = random.choice(miejski)
        loss=loss.lower().strip()
        listaloss =[]
        blad = 0

        for x in loss:
            listaloss.append(x)
        tablica="_"*len(listaloss)
        tablica=[x for x in tablica]
        symbols = [' ','`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/']
        for x in listaloss:
            if x in symbols:
                index2 = listaloss.index(x)
                tablica[index2] = x
        liczpodej = 24-n
        if liczpodej <= 4:
            liczpodej = 4
        while sigma == 0:
            if blad == liczpodej:
                print("przegrałeś")
                print(f"haslem było {loss}")
                sys.exit(0)
            print(tablica)
            strinput=str(input("wybierz literke badz haslo "))
            if strinput == loss:
                print("wygrałeś")
                break
            else:
                pass
            if strinput not in listaloss:
                blad = blad + 1
            if len(strinput) == 1:
                while strinput in listaloss:
                    try:
                        index=listaloss.index(strinput)
                        tablica[index] = strinput
                        listaloss[index] = "zgadniete"
                    except:
                        continue
            if listaloss.count("zgadniete") == len(listaloss):
                print("wygrałeś")
                listalos=[]
                sigma = 1
                
                
                
