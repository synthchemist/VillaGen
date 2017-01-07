import gen_NPC 
import random
import configuration as config


   
def run(num_smith, set_race):

    smith_list = []

    while num_smith != 0:

        gen_NPC.run(set_race)
        propname, sex = gen_NPC.run(set_race)
        if sex == 'male': 
            pronoun = 'his'
        else: #female
            pronoun = 'her'
        smith_list.append(propname + 'is a ' + random.choice(config.descriptors) + ' blacksmith ' + pronoun + ' forge can be found in the ' + random.choice(config.area) + ' part of town.\n')
        num_smith = num_smith - 1 

    smith_info = '\n'.join(smith_list)  
    return smith_info
