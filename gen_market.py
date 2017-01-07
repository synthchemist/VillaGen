import random
import configuration as config
import gen_NPC

def run(num_market, set_race):    
    market_list = []
    while num_market != 0:
        
        gen_NPC.run(set_race)
        propname, sex = gen_NPC.run(set_race)
        if sex == 'male': 
            pronoun = 'His'
        else: #female
            pronoun = 'Her'
        
        randmarket = random.choice(config.rand_stores)
        store = open(randmarket + '.txt')
        name1 = store.readlines()
        name1 = random.choice(name1).strip()
        market_list.append(propname +  'is a ' + random.choice(config.descriptors) + ' ' + randmarket + '.\n' + pronoun + ' store, ' + name1 + ', is found towards the ' + random.choice(config.area) + ' part of town.\n\n')

        num_market = num_market - 1
    
    market_info = '\n'.join(market_list)
    return market_info

