from User import User
from PlantParams import (
    CoalPlantParams, GasTurbineParams, SolarFarmParams,
    HydroPlantParams, WindTurbineParams, NuclearPlantParams
)
from Plants import (
    Coalplant, GasTurbine, SolarFarm, 
    HydroPlant, WindTurbine, NuclearPlant
)
import random

class Store:
    available_plants = []
    
    # Diccionario de mapeo: relaciona el Enum de parámetros con la Clase
    PLANT_MAP = {
        CoalPlantParams: Coalplant,
        GasTurbineParams: GasTurbine,
        SolarFarmParams: SolarFarm,
        HydroPlantParams: HydroPlant,
        WindTurbineParams: WindTurbine,
        NuclearPlantParams: NuclearPlant
    }

    PLANT_PRICES = {
        "COAL": 94_000,
        "GAS TURBINE": 86_000,
        "SOLAR FARM": 110_000,
        "HYDRO": 5_900_000,
        "WIND TURBINE": 48_000,
    }

    @staticmethod
    def show_available_plants():
        for pl in Store.available_plants:
            print(f"id({pl.id}) - {pl.type}: price: ${pl.price}") 

    @staticmethod
    def generate_plants():
        # Limpiar la tienda antes de generar nuevas (opcional)
        Store.available_plants = []
        
        cantidad = random.randint(1, 5)
        posibles_params = list(Store.PLANT_MAP.keys())
        
        for _ in range(cantidad):
            # 1. Elegimos un parámetro al azar
            param_elegido = random.choice(posibles_params)
            
            # 2. Obtenemos la CLASE correspondiente del mapeo
            clase_planta = Store.PLANT_MAP[param_elegido]
            
            # 3. Instanciamos dinámicamente pasando el parámetro
            # Esto llama al __init__ de BasePlant a través de la subclase
            nueva_planta = clase_planta(param_elegido)
            
            Store.available_plants.append(nueva_planta)
        
        print(f"Tienda: Se han generado {cantidad} nuevas plantas.")

    @staticmethod
    def sell_plant(user: User, plant_id):
        for pl in user.plants:
            if pl.id == plant_id:
                print(f"Info: {pl.type} plant with id {pl.id} will be sold at ${Store.PLANT_PRICES[pl.type]}")
                user.plants = [item for item in user.plants if item.id != plant_id]
                user.balance += Store.PLANT_PRICES[pl.type]
    
    @staticmethod
    def buy_plant(user: User, id):
        if id not in [pl.id for pl in Store.available_plants]:
            print(f"Warning: This id does not exist.")
            return

        for pl in Store.available_plants:
            if id == pl.id:
                if user.balance >= pl.price:
                    print(f"Info: you acquired a {pl.type} plant!")
                    user.balance -= pl.price
                    user.plants.append(pl)
                    available_plants = [item for item in Store.available_plants if item.type != type]
                    return
                else:
                    print(f"Warning: you do not have enough balance to do this transaction")
                    return