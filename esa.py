import random
class gracz:
    def __init__(self,hp,n,dmg,ataki,name,skin,effect=[]):
        self.name=name
        self.skin=skin
        self.hp=hp*(n*10)//3
        self.dmg=dmg*n//3
        self.ataki=ataki
        self.effect=effect
    def atak(self,enemy,tatak):
        if tatak == "bite"and "bite" in self.ataki:
            if "krwawienie" not in enemy.effect:
                enemy.hp -= 5*self.dmg
                enemy.effect.append("krwawienie")
                print(fr"{self.name} urzywa {tatak} hp {enemy.name} spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
                print(fr'został na cb nałożony efekt {enemy.effect[len(enemy.effect)-1]}🩸')
            elif "krwawienie" in enemy.effect:
                enemy.hp -= 5*self.dmg
                enemy.hp -= 5*self.dmg
                print(fr"przeciwnik nie nadał ci efektu krwawienia")
                print(fr"{self.name} urzywa {tatak} hp {enemy.name} spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
        if tatak == "smite"and "smite" in self.ataki:
           lvlsmite=self.lvl//2
           if lvlsmite > 5:
               lvlsmite = 6
           enemy.hp -= enemy.hp // 8
           print(fr"{self.name} urzywa {tatak} hp {enemy.name} spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
        if tatak == "lifedrain"and "lifedrain" in self.ataki:
            lvldrain=10-self.lvl//2
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
                print(fr'został na cb nałożony efekt {enemy.effect[len(enemy.effect)-1]}🩸')
            elif "osłabienie" in enemy.effect:
                enemy.hp -= 5*self.dmg
                print(fr"przeciwnik nie moze wykonac na tobie {self.name} wiec uderza cie i zostaje ci "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"wygrałeś")
class mob:
    def __init__(self,hp,n,dmg,ataki,name,skin,typ,effect=[]):
        self.name=name
        self.skin=skin
        self.lvl=random.randint((1+n)*2,n*5)
        self.hp=hp*self.lvl//3
        self.dmg=dmg*self.lvl//3
        self.ataki=ataki
        self.effect=effect
        self.typ=typ
    def atak(self,enemy):
        tatak=random.choice(self.ataki)
        if tatak == "bite":
            if "krwawienie" not in enemy.effect:
                enemy.hp -= 5*self.dmg
                enemy.effect.append("krwawienie")
                print(fr"{self.name} urzywa {tatak} twoje hp spada do "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
                print(fr'został na cb nałożony efekt {enemy.effect[len(enemy.effect)-1]}🩸')
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
                print(fr'został na cb nałożony efekt {enemy.effect[len(enemy.effect)-1]}🩸')
            elif "osłabienie" in enemy.effect:
                enemy.hp -= 5*self.dmg
                print(fr"przeciwnik nie moze wykonac na tobie {self.name} wiec uderza cie i zostaje ci "+ fr"{enemy.hp}❤" if enemy.hp > 0 else r"przegrałeś")
n=3
agracz=gracz(hp=100,n=n,dmg=10,ataki=["bite"],name="gracz",skin=r"🐱‍👤")
slime=mob(hp=200,n=n,dmg=10,ataki=["bite","smite","lifedrain","osłabienie"],name="slime",skin=r"🟢",typ="slime")
print(fr"{agracz.hp}❤{agracz.skin} {n} lvl VS {slime.hp}❤{slime.skin} {slime.lvl} lvl")
while slime.hp > 0:
    print(f"twoje ataki to {agracz.ataki}")
    ligma=input("jaki atak wyprowadzasz ")
    agracz.atak(enemy=slime,tatak="bite")
    if agracz.hp <=0:
       break 
    slime.atak(agracz)
    
    
    
    
    
            
    
