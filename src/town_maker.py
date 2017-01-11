import random
import configuration as config

def run(set_size, set_loc):


    lib_info  = ['Libraries:\nNone']
    town = open(set_loc + '.txt')
    name1 = town.readlines()
    town_name = random.choice(name1).strip()
    if set_size == 'Small':

        population = random.randrange(50, 350, 10)
        num_tav = 1
        num_smith = 1
        num_shrine = random.randint(0, 1)
        num_lib = random.choice(config.tenpercent)
        
        num_market = 1
        genstore = 1

            
        


    elif set_size == 'Medium':
    
        population = random.randrange(350, 500, 50)
        num_tav = random.randint(2, 4) 
        num_smith = 2
        num_shrine = random.randint(1, 2) 
        num_lib = random.choice(config.fourtypercent)
        num_market = 3
        genstore = 2
     
        
    else: ## Large
    
        population = random.randrange(500, 1000, 100)
        num_tav = random.randint(4, 6) 
        num_smith = 3
        num_shrine = random.randint(2, 3)
        num_market = 4
        num_lib = random.randint(1, 2)
        genstore = 2

    return population, num_tav, num_smith, num_market, num_lib, genstore, town_name, lib_info
