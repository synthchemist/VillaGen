import random
import configuration as config
import gen_NPC

def run(num_lib, set_race):
    lib_list = []
    while num_lib != 0: 
        
        gen_NPC.run(set_race)
        propname, sex = gen_NPC.run(set_race)
        if sex == 'male': 
            pronoun = 'He'
        else: #female
            pronoun = 'She'
        

        
        randlib = open('Library.txt')
        name1 = randlib.readlines()
        name1 = random.choice(name1).strip()
        lib_list.append(propname + 'is the head Librarian at The ' + name1 + '. The Library is found in the ' + random.choice(config.area) + ' dstrict.\n')
        num_lib -=  1

    lib_info = '\n'.join(lib_list) 
    return lib_info
