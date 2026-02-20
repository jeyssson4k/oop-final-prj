from enum import Enum

# this classes describes all properties in order to create new plants
# i do not want to change values directly in the factory class so i prefer
# to create a new class where to find the values

class CoalPlantParams(Enum):
    PRICE = 1e6
    MAX_KWH = 100e3
    MIN_OPERATIVE_KWH = 10e3
    MAINTAIN_COST = 9e3

class GasTurbineParams(Enum):
    PRICE = 1.35e3
    MAX_KWH = 140e3
    MIN_OPERATIVE_KWH = 28e3
    MAINTAIN_COST = 7.75e3

