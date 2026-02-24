# controls user's balance, plants and user's response when demand changes
class User:
    def __init__(self):
        self.balance = 1e3
        self.plants = []
        self.current_power = 0 # there is no plants yet 
        self.max_power = 0 # there is no max kwh because there is no plants yet

    def change_used_plant_capacity(id:int, capacity: int):
        # select a plant by id and then set the new used_capacity
        # check if the capacity exceeds the plant's max_capacity
        # if yes then assign the plant's max_capacity 
        plant = None
        for pl in plants:
            if pl.id == id:
                plant = pl

        if plant is None:
            print(f"Warning: The plant with id {id} does not exist.")
        else:
            if capacity > pl.max_kwh:
                pl.kwh_used = max_kwh
            else if capacity < 0:
                pl.kwh_used = min_operative_kwh
            else:
                pl.kwh_used = capacity
        pass
    