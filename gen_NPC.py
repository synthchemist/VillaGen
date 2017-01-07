import random 

class NPC: 
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.name = first + ' ' + last        
        self.attribute =  False
        self.appearance = False
        self.personality = False


def run(set_race): 


    gender = ['male', 'female']
    sex = random.choice(gender)
    first = open(set_race + '_' + sex + '.txt')
    name1 = first.readlines()
    first = random.choice(name1).strip()

    last = open(set_race + '_surnames.txt')
    name2 = last.readlines()
    last = random.choice(name2).strip()

    npcname = NPC(first, last)
    propname = npcname.name

    return propname, sex
