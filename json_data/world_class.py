import random


class Location:
    def __init__(self):
        location_size = self.determine_size()
        self.location_size = location_size
        print(location_size)

    def determine_size(self):
        #Reused this from lig
        population = random.randint(0 , 3000000)
        region_types = {"Large": ["City", "Grand Fortress", "Grand Library", "Grand City", "Imperial Free City"],
                             "Medium": ["Town", "Castle", "University Town", "Market Town", "Grand Harbour"],
                             "Small": ["Village", "Fief", "Abbey", "Fortification", "Barony", "Barracks"],
                             "Tiny": ["Hamlet", "Settlement", "Hunter's Post", "Outpost", "Chapel"]}
        region_population = {"Large": [80000,3000000],
                             "Medium": [22000, 79999],
                             "Small": [3000, 21999],
                             "Tiny": [1 , 2999]}
        for i in region_population.keys():
            pop_range = region_population[i]
            if pop_range[0] <= population <= pop_range[1]:
                location_size = {region_types[i][random.randint(0, len(region_types[i])-1)] : population}
        return location_size

town = Location()
print(town.__dict__)
print(dir(town))
size = town.location_size