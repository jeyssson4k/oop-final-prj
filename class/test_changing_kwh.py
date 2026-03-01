from Plants import Coalplant
from PlantParams import CoalPlantParams


print("Testing the integration between plants and params\n")

plant0 = Coalplant(CoalPlantParams)

#condiciones iniciales
plant0.set_initial_kwh(20000)

print(plant0)
i = 0
while(True):
    new_limit = 40000
    plant0.change_kwh_used_with_operating(new_limit)
    
    print(f"{new_limit}, {plant0.kwh_used}")

    if new_limit == plant0.kwh_used:
        break


