import configuration as config
import random
import gen_NPC

def run(num_tav, set_race):
    print(num_tav)
    tav_list = []
    while num_tav != 0:

        gen_NPC.run(set_race)
        propname, sex = gen_NPC.run(set_race)
        tavern1 = open('tavnames1.txt')
        name1 = tavern1.readlines()
        name1 = random.choice(name1).strip()

        tavern2 = open('tavnames2.txt')
        name2 = tavern2.readlines()
        name2 = random.choice(name2).strip()
        tavern_name = 'The ' + name1 + ' ' + name2
        sort = random.choice(config.tavern_sort)
        tav_list.append(tavern_name + '.\nThe inkeeper is a ' + sex + ' ' + set_race +  " named " + propname + '. \nIt\'s a ' + sort +' ' + 'located in the ' + random.choice(config.area) + ' part of town.\n')
    #    tavwrite.append(tav_info)
        num_tav = num_tav - 1
    
    tav_info = '\n'.join(tav_list)
    del tav_list[:]
    return tav_info
    print(tav_info)
