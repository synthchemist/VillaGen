import gen_NPC 
import random
import configuration as config


   
def run(genstore, set_race):

    genstore_list = []

    while genstore != 0:

        gen_NPC.run(set_race)
        propname, sex = gen_NPC.run(set_race)
        if sex == 'male': 
            pronoun = 'his'
        else: #female
            pronoun = 'her'

        store = open('general_store' + '.txt')
        name1 = store.readlines()
        name1 = random.choice(name1).strip()
        genstore_list.append(propname + 'is the proprietor \"' + name1 + '\" a general store. \nA ' + random.choice(config.descriptors) + ' ' + set_race + ' ' + pronoun + ' store can be found in the ' + random.choice(config.area) + ' section of town.\n')
        genstore = genstore - 1 

    genstore_info = '\n'.join(genstore_list)  
    return genstore_info
