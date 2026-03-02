from enum import Enum

# this classes describes all properties in order to create new plants
# i do not want to change values directly in the factory class so i prefer
# to create a new class where to find the values


## ! it is necessary to add logic that describes when the plant needs maintainement

## ramp_rate means how many steps are needed to make 
## a change in the current capacity used by the plant
class CoalPlantParams(Enum):
    PRICE = 100_000
    MAX_KWH = 100_000
    MIN_OPERATIVE_KWH = 10_000
    MAINTAIN_COST = 7_000
    MAINTAIN_DAYS_RATIO = 10
    TYPE = "COAL"
    RAMP_RATE = 4

class GasTurbineParams(Enum):
    PRICE = 135_000
    MAX_KWH = 140_000
    MIN_OPERATIVE_KWH = 28_000
    MAINTAIN_COST = 7_750
    MAINTAIN_DAYS_RATIO = 15
    TYPE = "GAS TURBINE"
    RAMP_RATE = 6

class SolarFarmParams(Enum):
    PRICE = 190_000
    MAX_KWH = 80_000
    MIN_OPERATIVE_KWH = 1_000
    MAINTAIN_COST = 1_380
    MAINTAIN_DAYS_RATIO = 7
    TYPE = "SOLAR FARM"
    RAMP_RATE = 1

class HydroPlantParams(Enum):
    PRICE = 7_000_000
    MAX_KWH = 2_000_000
    MIN_OPERATIVE_KWH = 50_000
    MAINTAIN_COST = 10_000
    MAINTAIN_DAYS_RATIO = 30
    TYPE = "HYDRO"
    RAMP_RATE = 3

class WindTurbineParams(Enum):
    PRICE = 90_000
    MAX_KWH = 10_000
    MIN_OPERATIVE_KWH = 0
    MAINTAIN_COST = 800
    MAINTAIN_DAYS_RATIO = 3
    TYPE = "WIND TURBINE"
    RAMP_RATE = 2

class NuclearPlantParams(Enum):
    PRICE = 17_000_000
    MAX_KWH = 9_000_000
    MIN_OPERATIVE_KWH = 80_000
    MAINTAIN_COST = 80_000
    MAINTAIN_DAYS_RATIO = 20
    TYPE = "NUCLEAR"
    RAMP_RATE = 3