

from Tkinter import * 
import random
master = Tk()
master.wm_title("VillaGen")


import configuration as config




def MakeSettlement():


# retrive user defined variables

    set_size = variable_size.get() 
    set_race = variable_race.get()
    set_loc = variable_loc.get()

## import all functions needed this can be outside def MakeSettlement(): but I put it here fore neatness


    import town_maker 
    import gen_NPC
    import gen_tav   
    import gen_smith
    import gen_market
    import gen_lib
    import gen_genstore


 # initiate make town 

    town_maker.run(set_size, set_loc)
    population, num_tav, num_smith, num_market, num_lib, genstore, town_name, lib_info = town_maker.run(set_size, set_loc)

# initiate general store 


    gen_genstore.run(genstore, set_race) 
    genstore_info = gen_genstore.run(genstore, set_race) 
    
 # initiate make town 

## initiating tavern generator

    gen_tav.run(num_tav, set_race)
    tav_info = gen_tav.run(num_tav, set_race)

#    tavwrite.append(gen_tav.run(num_tav, set_race))
#    tav_list = tav_info.readlines()
#    tav_list = tav_info.strip()


 ## initiating smith generator     

    gen_smith.run(num_smith, set_race)
    smith_info = gen_smith.run(num_smith, set_race)   


# initiating market generator 

    gen_market.run(num_market, set_race)
    market_info = gen_market.run(num_market, set_race)




#initiate library generator 

    gen_lib.run(num_lib, set_race)

    if num_lib > 0: 
        lib_info = gen_lib.run(num_lib, set_race)
    else: 
        lib_info = ''.join(lib_info)
    
       
# stitching all the lists together and putting them inside the text box 

        
    w.insert(END, 'Name: ' + town_name + '\nPopulation: Aprox. ' + str(population) + 'people \n\n' + 'Taverns and Inns; \n' + tav_info + '\nGeneral Sotres: \n' + genstore_info + '\nBlacksmiths: \n' + smith_info + '\n\n' + 'Stores of interest:\n' + market_info  + lib_info + '\n\n')

#drop down boxes

variable_size = StringVar(master)
variable_size.set('Small')

variable_loc = StringVar(master)
variable_loc.set('Coastal')

variable_race = StringVar(master)
variable_race.set('Dwarf')

size = OptionMenu(master, variable_size, 'Small', 'Medium', 'Large')
size.pack()

local = OptionMenu(master, variable_loc, 'Coastal', 'Desert', 'Forest', 'Mountain', 'Swamp', 'River')
local.pack()

race = OptionMenu(master, variable_race, 'Dwarf','Elf', 'Human')
race.pack()

#text box

w = Text (master, height=40, width=120)
w.pack()

generate = Button(master, text = "Generate Settlement", command = MakeSettlement) 
generate.pack()

#clearing textbox

def Clear():
    w.delete(1.0, END)

clear = Button(master, text = "Clear", command = Clear) 
clear.pack()


mainloop()
