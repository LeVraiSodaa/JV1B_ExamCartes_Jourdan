class Cartes:
    def __init__(self,name,cost,desc):
        self.__nom = name
        self.__cout = cost
        self.__description = desc

    def getCost(self):
        return self.__cout
    def getName(self):
        return self.__nom
    def getDesc(self):
        return self.__description


class Mage:
    def __init__(self,hp,mana,name,tot,act,hand,defa,play):
        self.__nom = name
        self.__vie = hp
        self.__total = tot
        self.__actuel = act
        self.__mana = mana
        self.__main = hand
        self.__defausse = defa
        self.__zonedejeu = play

    def get(self):
        return self.__vie
    def getName(self):
        return self.__nom
    def getAct(self):
        return self.__actuel
    def getTot(self):
        return self.__total
    def getMana(self):
        return self.__mana
    def getHand(self):
        return self.__main
    def getDefa(self):
        return self.__defausse
    def getPlay(self):
        return self.__zonedejeu

    
class Cristal(Cartes):
    def __init__(self,cost,vale,desc,name):
        Cartes.__init__(cost,desc,name)
        self.__valeur = vale
    def getVale(self):
        return self.__valeur
    
class Creature(Cartes):
    def __init__(self,cost,hp,atk,name,desc):
        Cartes.__init__(cost,desc,name)
        self.__vie = hp
        self.__attaque = atk
    def getHp(self):
        return self.__vie
    def getAtk(self):
        return self.__attaque
    
class Blast(Cartes):
    def __init__(self,vale,cost,name,desc):
        Cartes.__init__(cost,name,desc)
        self.__valeur = vale
    def getVale(self):
        return self.__valeur