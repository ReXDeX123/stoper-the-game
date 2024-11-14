import random
import time
import sys
from colorama import Fore, Back
import os 
def prime_numbers(n):
    if n > 0:
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
        num = []
        for x in number:
            try:
                num.append(x)
            except:
                pass
        return num
    elif n < 0:
        n= n*-1
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
        num = []
        for x in number:
            try:
                num.append(x*-1)
            except:
                pass
        return num
def perfect_numbers(n):
    if n <= 0:
        return "nie jest"
    dzielniki = [1]
    suma = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            dzielniki.append(i)
            suma += i
            if i != n // i:
                dzielniki.append(n // i)
                suma += n // i
            if suma > n:  
                return "nie jest"
def fibo(n):
    liczby_fibo = []
    if n == 1:
        liczby_fibo = [1]
    elif n > 1:
        liczby_fibo = [1, 1]
        for i in range(2, n):
            liczby_fibo.append(liczby_fibo[i-2] + liczby_fibo[i-1])
    elif n < 0:
        liczby_fibo = []
    return liczby_fibo

    return "jest" if suma == n else "nie jest" 
def eqd(eq):
    print("masz")
    print(f"{eq.count('tarcza')}🛡")
    print(f"{eq.count('żarówka')}💡")
    print(f"{eq.count('zbroja')}🧥")
    print(f"{eq.count('miecz')}🗡")
    print(f"{eq.count('shimer')}⚗")
    print(f"{eq.count('klepsydra')}⌛")
    print(f"{eq.count('roszada')}⇄")
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
klepsydra = 0
miejski = open("miejski2.txt","r",encoding="utf-8").readlines()
miejski = str(miejski).replace("'", "").replace("\\", "").replace("[", "").replace("]", "").split(",")
eq = []
monety = 0
while p == 0:
    if klepsydra == 0:
        a = random.randint(1,50)
    elif klepsydra == 1:
        a=random.randint(10,100)
   
    if eq.count("shimer") == 0:
       os.system("color 07")
    elif eq.count("shimer") > 0:
        os.system('color 2d')
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
    time.sleep(a)
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
    lossklep = 0
    if monety > 0:
        lossklep = random.randint(1,30)
    if lossklep == 1:
        eqd(eq)
        print(r"                                                        🛒Witaj w sklepie🛒")
        print("w sklepie możesz kupic specjalne przedmiety ulatwiajace gre takie jak (aby kupić przedmiot wpisz jego nazwe mozesz kupic tylko 1 przedmiot na sklep)")
        print(rf"posiadasz {monety}💰") 
        print(r"tarcza  🛡 (pozwala ona pominąć karzde zadanie) (na trybie walki blokuje jedynie nastepne obrazenia) cena tarczy wynosi 350💰")
        print(r"żarówka 💡 (daje podbowiedz w wybranym zadaniu)(nie działa w trybie walki) cena żarówki wynosi 75💰") 
        print(r"zbroja 🧥 (daje dodatkowe życia podczas zadania) cena zbroi wynosi 50💰")
        print(r"miecz 🗡 (pozwala zadac podwojny dmg dla moba)(działa tylko w minigrze walki) cena miecza wynosi 50💰") # teraz nie dziala nie ma mobow
        print(r"shimer ⚗️ (zmienia kolor timera na zielony) cena shimeru wynosi 200💰") 
        print(r"klepsydra ⌛ (pozwala zwiekszyć odstep miedzy minigrami ) cena klepsydry wynosi 2500💰")
        print(r"roszada ⇄ (pozwala zmienic haslo/moba lecz nie dodaje zycia) cena roszady wynosi 75💰") 
        print(r"wieszak  𓍯 (kończy gre ⚰️ (przegrywasz)) cena wieszaka wybosi 1000000💰")
        sklep=input("co kupujesz (jesli nic kliknij enter) ")
        if sklep in ["miecz","tarcza","żarówka","zbroja","shimer","klepsydra","roszada","wieszak"]:
            if sklep == "miecz" and monety >= 50:
                print(r"zakupiłeś 🗡")
                eq.append("miecz")
                print(fr"posiadasz {eq.count('miecz')} 🗡 ")
                monety = monety - 50
            elif sklep == "miecz" and monety < 50:
                print("nie masz pieniedzy biedaku")
            if sklep == "tarcza" and monety >= 350:
                print(r"zakupiłeś 🛡")
                eq.append("tarcza")
                monety = monety - 350
                print(fr"posiadasz {eq.count('tarcza')} 🛡 ")
            elif sklep == "tarcza" and monety < 350:
                print("nie masz pieniedzy biedaku")
            if sklep == "żarówka" and monety >= 50:
                print(r"zakupiłeś 💡")
                eq.append("żarówka")
                monety = monety - 50
                print(fr"posiadasz {eq.count('żarówka')} 💡 ")
            elif sklep == "żarówka" and monety < 50:
                print("nie masz pieniedzy biedaku")
            if sklep == "zbroja" and monety >= 50:
                print(r"zakupiłeś 🧥")
                eq.append("zbroja")
                monety = monety - 50
                print(fr"posiadasz {eq.count('zbroja')} 🧥 ")
            elif sklep == "zbroja" and monety < 50:
                print("nie masz pieniedzy biedaku")
            if sklep == "shimer" and monety >= 200 and eq.count("shimer") == 0:
                print(r"zakupiłeś ⚗")
                eq.append("shimer")
                monety = monety - 200
                print(fr"posiadasz {eq.count('shimer')} ⚗ ")
            elif sklep == "shimer" and monety < 200:
                print("nie mozesz tego kupic")
            if sklep == "klepsydra" and monety >= 2500 and eq.count("klepsydra") == 0:
                print(r"zakupiłeś ⌛")
                eq.append("klepsydra")
                monety = monety - 2500
                print(fr"posiadasz {eq.count('klepsydra')} ⌛ ")
                klepsydra = 1
            elif sklep == "klepsydra" and monety < 2500:
                print("nie mozesz tego kupic")
            if sklep == "roszada" and monety >= 75:
                print(r"zakupiłeś ⇄")
                eq.append("roszada")
                monety = monety - 75
                print(fr"posiadasz {eq.count('roszada')} ⇄ ")
            elif sklep == "roszada" and monety < 75:
                 print("nie masz pieniedzy biedaku")
            if sklep == "wieszak" and monety >= 1000000:
                print("powiesiłeś się na wieszaku")
                monety = monety - 1000000
                p=1
            elif sklep == "wieszak" and monety < 1000000:
                print("nie stac cie biedaku")
        else:
            pass
    
    liczbapr = 15 - n
    if liczbapr <= 2:
        liczbapr = 2
    los1=random.randint(1,4)
    if los1 == 1:
        losn = 0
        while losn == 0:
            losn = random.randint((n+1)*-50,(n+1)*50)
        while timer < liczbapr:
            zycia = liczbapr - timer
            print(fr"masz {zycia}❤️")
            wyb=input("jak sadzisz co wylosowala partia ")
            if wyb == "use roszada" and eq.count("roszada") > 0: # itemy
                eq.remove("roszada")
                print(fr"użyeś roszady zostało ci {eq.count('roszada')}⇄")
                print(f"zmieniona liczba to {losn}")
                losn = random.randint((n+1)*-50,(n+1)*50)
                continue
            elif wyb=="use roszada" and eq.count("roszada") == 0:
                print(r"nie masz ⇄")
                continue
            if wyb == "use zbroja" and eq.count("zbroja") > 0:
                eq.remove("zbroja")
                print(fr"użyeś roszady zostało ci {eq.count('zbroja')}🧥")
                timer = timer - 3
                continue
            elif wyb=="use zbroja" and eq.count("zbroja") == 0:
                print(r"nie masz 🧥")
                continue
            if wyb=="use tarcza" and eq.count("tarcza") > 0:
                eq.remove("tarcza")
                print(fr"użyeś roszady zostało ci {eq.count('tarcza')}🛡")
                break
            elif wyb=="use tarcza" and eq.count("tarcza") == 0:
                print(r"nie masz 🛡")
                continue
            if wyb=="use żarówka" and eq.count("żarówka") > 0:
                eq.remove("żarówka")
                print(fr"użyeś żarówka zostało ci {eq.count('żarówka')}💡")
                zarlos=randint(1,12)
                if zarlos == 1:
                    wiekszeniz50 = losn > 50
                    print(f"{'jest' if wiekszeniz50 else 'nie jest'} wieksze od 50")
                elif zarlos ==2:
                    mniejniz50 = losn > 50
                    print(f"{'jest' if mniejniz50 else 'nie jest'} mniejsze od 50")
                elif zarlos ==3:
                    wiekszenizm50 = losn > -50
                    print(f"{'jest' if wiekszenizm50 else 'nie jest'} wieksze od -50")
                elif zarlos ==4:
                    mniejniz50 = losn > -50
                    print(f"{'jest' if mniejniz50 else 'nie jest'} mniejsze od -50")
                elif zarlos ==5:
                    print(f"{'jest' if losn % 5 == 0 else 'nie jest'} podzielne przez 5")
                elif zarlos ==6:
                    print(f"{'jest' if losn % 4 == 0 else 'nie jest'} podzielne przez 4")
                elif zarlos ==7:
                    print(f"{'jest' if losn % 6 == 0 else 'nie jest'} podzielne przez 6")
                elif zarlos ==8:
                    print(f"{'jest' if losn % 7 == 0 else 'nie jest'} podzielne przez 7")
                elif zarlos ==9:
                    print(f"{'jest' if losn % 8 == 0 else 'nie jest'} podzielne przez 8")
                elif zarlos ==10:
                    print(f"{'jest' if losn % 9 == 0 else 'nie jest'} podzielne przez 9")
                elif zarlos == 11:
                    print("ta liczba jest wynikiem jakiegoś działania matematycznego")
                elif zarlos == 12:
                    print(f"{'należy' if losn in fibo(losn+1) else 'nie należy'} do ciagu fibonacziego")
                continue
            elif wyb=="use żarówka" and eq.count("żarówka") == 0:
                print(r"nie masz 💡")
                continue
            if wyb == "eq" or wyb == "open eq":
                eqd(eq)
                continue
            try:
                wyb=int(wyb)
            except:
                continue
            if wyb == losn:
                print("wygrałeś")
                monety = monety + random.randint(1,35)
                print(rf"posiadasz {monety}💰") 
                timer = 0
                break
            if wyb % 2 == 0 and losn % 2 == 0:
                print("liczba jest parzysta")
            elif wyb % 2 == 1 and losn % 2 == 1:
                print("liczba jest nieparzysta")
            pnl = prime_numbers((n+1)*50)
            pn2 = prime_numbers(n=((n+1)*-50))
            if losn in pn1 or losn in pn2:
                if wyb > 0 and losn > 0:
                    print("liczba is pierwsza")
                elif wyb < 0 and losn < 0:
                    print("liczba jest ujemna liczba pierwsza")
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
            if perfect_numbers(wyb) == "jest" and perfect_numbers(losn) == "jest":
                print("liczba jest liczba doskonała")
            elif perfect_numbers(wyb) == "nie jest" and perfect_numbers(losn) == "nie jest": 
                print("liczba nie jest liczba doskonałą")
            else:
                pass
            timer = timer +1
            if timer == liczbapr:
                print("przegrałeś")
                p=1
                break
    los2 = random.randint(1,12)
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
                listaloss[index2] = "zgadniete"
        liczpodej = 16-n
        if liczpodej <= 4:
            liczpodej = 4
        while sigma == 0:
            if blad > liczpodej:
                print("przegrałeś")
                print(f"haslem było {loss}")
                sys.exit(0)
            print(tablica)
            strinput=str(input("wybierz literke badz haslo "))
            if strinput=="use roszada" and eq.count("roszada") > 0: #itemy
                eq.remove("roszada")
                print(fr"użyeś roszady zostało ci {eq.count('roszada')}⇄")
                print(f"haslem bylo {loss}")
                loss = random.choice(miejski)
                loss=loss.lower().strip()
                listaloss =[]
                for x in loss:
                    listaloss.append(x)
                tablica="_"*len(listaloss)
                tablica=[x for x in tablica]
                for x in listaloss:
                    if x in symbols:
                        index2 = listaloss.index(x)
                        tablica[index2] = x
                        listaloss[index2] = "zgadniete"
                continue
            elif strinput=="use roszada" and eq.count("roszada") == 0:
                print(r"nie masz ⇄")
                continue
            if strinput=="zbroja" and eq.count("zbroja") > 0:
                eq.remove("zbroja")
                print(fr"użyeś roszady zostało ci {eq.count('zbroja')}🧥")
                blad = blad - 4
                continue
            elif strinput=="zbroja" and eq.count("zbroja") == 0:
                print(r"nie masz 🧥")
                continue
            if strinput=="use tarcza" and eq.count("tarcza") > 0:
                eq.remove("tarcza")
                print(fr"użyeś roszady zostało ci {eq.count('tarcza')}🛡")
                break
            elif strinput=="use tarcza" and eq.count("tarcza") == 0:
                print(r"nie masz 🛡")
                continue
            if strinput=="use żarówka" and eq.count("żarówka") > 0:
                kys=randint(0,10)
                if kys > 10:
                    strinput = "zgadniete"
                    eq.remove("żarówka")
                    print(fr"użyeś roszady zostało ci {eq.count('żarówka')}💡")
                    while strinput == "zgadniete":
                        strinput = random.choice(listaloss)
                elif kys == 10:
                    print("jest to słowo z slownika miejski.pl")
            elif strinput=="use żarówka" and eq.count("żarówka") > 0:
                print(r"nie masz 💡")
                continue
            if strinput == "eq" or strinput == "open eq":
                eqd(eq)
                continue
            if strinput == loss:
                print("wygrałeś")
                monety = monety + random.randint(1,75)
                print(rf"posiadasz {monety}💰") 
                break
            else:
                pass
            if strinput not in listaloss:
                blad = blad + 1
                zycia = liczpodej - blad +1
                print(f"masz {zycia}❤️")
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
                monrand = random.randint(1,75)
                monety = monety + monrand
                print(rf"posiadasz {monety}💰") 
                listalos=[]
                sigma = 1

                
                
