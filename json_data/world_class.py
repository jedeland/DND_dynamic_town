import random


class Location:
    def __init__(self):
        location_size = self.determine_size()
        self.location_size = location_size
        self.economic_situation = self.determine_economy(location_size)
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
    def determine_economy(self, location):
        #Should add region modifier to economy after the fact
        #TODO: Modify population modifier to add economic value points
        population_modifier = {"Large": [80000, 3000000],
                             "Medium": [22000, 79999],
                             "Small": [3000, 21999],
                             "Tiny": [1, 2999]}
        print()
        economic_value = random.randint(0, 2000)
        economic_status = {"Affluent": [2700, 3000],
                           "Prosperous": [2200, 2699],
                           "Rich": [2000, 2199],
                           "Strong": [1700, 1999],
                           "Stable": [1000, 1699],
                           "Average": [700, 999],
                           "Struggling": [400, 699],
                           "Poor": [250, 399],
                           "Impoverished": [100, 249],
                           "Desolate": [0, 99]
                           }
        return "Hello"

def populate_region():
    print("Populating region")
    #TODO: create 5-7 regions, add to them a set amount of each size (6 cities, 15 towns, 25+ villages, x many tiny)
town = Location()
print(town.__dict__)
print(dir(town))
size = town.location_size