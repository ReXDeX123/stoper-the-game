import random
class gracz:
    def __init__(self,hp,n,dmg,ataki,name,skin,effect=[]):
        self.name=name
        self.skin=skin
        self.hp=hp*(n*10)//3
        self.dmg=dmg*n//3
        self.ataki=ataki
        self.effect=effect
        self.kr=0
        self.dmgorg=dmg*n//3
        self.os=0
        self.lvl=n
        self.kys=0
    def atak(self,enemy,tatak):
        if tatak == "bite"and "bite" in self.ataki:
            if "krwawienie" not in enemy.effect:
                if enemy.typ == "slime":
                    enemy.hp -= 5*self.dmg//2
                    print(f"atak nie jest efektywny poniewarz przeciwnik to {enemy.typ}")
                else:
                    enemy.hp -= 5*self.dmg
                enemy.effect.append("krwawienie")
                print(fr"{self.name} urzywa {tatak} hp {enemy.name} spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
                print(fr'został na {enemy.name} nałożony efekt {enemy.effect[len(enemy.effect)-1]}🩸')
            elif "krwawienie" in enemy.effect:
                enemy.hp -= 5*self.dmg
                enemy.hp -= 5*self.dmg
                print(fr"przeciwnik nie nadał ci efektu krwawienia")
                print(fr"{self.name} urzywa {tatak} hp {enemy.name} spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
        if tatak == "smite"and "smite" in self.ataki:
            lvlsmite=self.lvl
            if lvlsmite > 5:
               lvlsmite = 6
            if enemy.typ == "slime":
                print(f"atak jest super efektowny przeciwko {enemy.typ}")
                enemy.hp -= (enemy.hp // 8) *2
            else:
                enemy.hp -= enemy.hp // 8
            print(fr"{self.name} urzywa {tatak} hp {enemy.name} spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
        if tatak == "lifedrain"and "lifedrain" in self.ataki:
            lvldrain=10-self.lvl
            if lvldrain < 0:
                lvldrain = 1 
            enemy.hp -= 5*self.dmg
            self.hp += 5*self.dmg//lvldrain
            print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
            print(fr"przeciwnik leczy się do {self.hp}❤") 
        if tatak == "osłabienie"and "osłabienie" in self.ataki:
            if "osłabienie" not in enemy.effect:
                enemy.effect.append("osłabienie")
                print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
                print(fr'został {enemy.name} nałożony efekt {enemy.effect[len(enemy.effect)-1]}🥀')
                enemy.os = 5
            elif "osłabienie" in enemy.effect:
                enemy.hp -= 5*self.dmg
                print(fr"{self.name} nie moze wykonac na {self.enemy} wiec uderza cie i zostaje ci "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
        if tatak == "krzyk starej":
            if "osłabienie" in self.effect:
                print("osłabienie 🥀 zostało zdjęte")
                self.effect.remove("osłabienie")
            elif "krzyk starej" not in self.effect:
                self.effect.append("krzyk starej")
                self.kys = 3
            else: 
                enemy.hp -= 5*self.dmg
                print(fr"self.name nie moze wykonac na {enemy.name} wiec uderza cie i zostaje ci "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
class mob:
    def __init__(self,hp,n,dmg,ataki,name,skin,typ,effect=[]):
        self.name=name
        self.skin=skin 
        self.lvl=random.randint((1+n)*2,n*5)
        self.hp=hp*self.lvl//3
        self.dmgorg=dmg*self.lvl//3
        self.dmg=dmg*self.lvl//3
        self.ataki=ataki
        self.effect=effect
        self.typ=typ
        self.kr=0
        self.os=0
        self.kys=0
    def atak(self,enemy):
        tatak=random.choice(self.ataki)
        if tatak == "bite":
            if "krwawienie" not in enemy.effect:
                enemy.hp -= 5*self.dmg
                enemy.effect.append("krwawienie")
                enemy.kr = 3
                print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
                print(fr'został na {enemy.name} nałożony efekt {enemy.effect[len(enemy.effect)-1]}🩸')
            elif "krwawienie" in enemy.effect:
                enemy.hp -= 5*self.dmg
                enemy.hp -= 5*self.dmg
                print(fr"przeciwnik nie nadał ci efektu krwawienia")
                print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
        if tatak == "smite":
           lvlsmite=self.lvl//2
           if lvlsmite > 5:
               lvlsmite = 6
           enemy.hp -= enemy.hp // 8
           print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
        if tatak == "lifedrain":
            lvldrain=10-self.lvl//2
            if lvldrain < 0:
                lvldrain = 1 
            enemy.hp -= 5*self.dmg
            self.hp += 5*self.dmg//lvldrain
            print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
            print(fr"przeciwnik leczy się do {self.hp}❤") 
        if tatak == "osłabienie":
            if "osłabienie" not in enemy.effect:
                enemy.effect.append("osłabienie")
                print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
                print(fr'został na {enemy.name} nałożony efekt {enemy.effect[len(enemy.effect)-1]}🥀')
                enemy.os = 5
            elif "osłabienie" in enemy.effect:
                enemy.hp -= 5*self.dmg
                print(fr"self.name nie moze wykonac na {enemy.name} wiec uderza cie i zostaje ci "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
        if tatak == "krzyk starej":
            if "osłabienie" in self.effect:
                print("osłabienie 🥀 zostało zdjęte")
                self.effect.remove("osłabienie")
            elif "krzyk starej" not in self.effect:
                self.effect.append("krzyk starej")
                self.kys = 3
            else: 
                enemy.hp -= 5*self.dmg
                print(fr"self.name nie moze wykonac na {enemy.name} wiec uderza cie i zostaje ci "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
def effekty(enemy,ty):
    if "krwawienie" in enemy.effect:
        enemy.kr -=1
        if enemy == agracz:
            print(r"krwawisz 🩸")
        else:
            print(fr"{enemy.name} krwawi 🩸")
        enemy.hp -= 10 *ty.dmg
        if enemy.kr < 1:
            enemy.effect.remove("krwawienie")
    if  "osłabienie" in enemy.effect:
        enemy.os -=1
        if enemy == agracz:
            print(r"jestes osłabiony 🥀")
        else:
            print(fr"{enemy.name} jest osłabiony 🥀")
        enemy.dmg = enemy.dmgorg // 3
        if enemy.os < 1:
            enemy.dmg = enemy.dmgorg
            enemy.effect.remove("osłabienie")
    if  "krzyk starej" in ty.effect:
        print(f"{ty.name} został zsigmowany 💪")
        ty.dmg = (ty.dmgorg * 1.5)//1
        ty.kys-=1
        if ty.kys < 0:
            ty.dmg = ty.dmgorg
            ty.effect.remove("krzyk starej")
        
                
n=3
agracz=gracz(hp=100,n=n,dmg=10,ataki=["bite","smite","osłabienie","lifedrain","krzyk starej"],name="gracz",skin=r"🐱‍👤")
slime=mob(hp=200,n=n,dmg=10,ataki=["bite","smite","lifedrain","osłabienie","krzyk starej"],name="slime",skin=r"🟢",typ="slime")
print(fr"{agracz.hp}❤{agracz.skin} {n} lvl VS {slime.hp}❤{slime.skin} {slime.lvl} lvl")
while slime.hp > 0:
    print(f"twoje ataki to {agracz.ataki}")
    ligma=input("jaki atak wyprowadzasz ")
    if ligma not in agracz.ataki:
        print("no debil")
        continue
    effekty(agracz,slime)
    effekty(slime,agracz)
    agracz.atak(enemy=slime,tatak=ligma)
    if agracz.hp <=0:
        break 
    slime.atak(agracz)    
    
    
    
    
            
    
