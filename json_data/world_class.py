import random


class Location:
    def __init__(self):
        location_size = self.determine_size()
        self.location_size = location_size
        self.economic_situation = self.determine_economy(location_size)
        print(location_size)

    def determine_size(self):
        #Reused this from lig
        population = random.randint(0 , 1500000)
        region_types = {"Large": ["City", "Grand Fortress", "Grand Library", "Grand City", "Imperial Free City"],
                             "Medium": ["Town", "Castle", "University Town", "Market Town", "Grand Harbour"],
                             "Small": ["Village", "Fief", "Abbey", "Fortification", "Barony", "Barracks"],
                             "Tiny": ["Hamlet", "Settlement", "Hunter's Post", "Outpost", "Chapel"]}
        region_population = {"Large": [80000,1500000],
                             "Medium": [22000, 79999],
                             "Small": [3000, 21999],
                             "Tiny": [1 , 2999]}
        for i in region_population.keys():
            pop_range = region_population[i]
            if pop_range[0] <= population <= pop_range[1]:
                location_size = {region_types[i][random.randint(0, len(region_types[i])-1)] : population}
        return location_size
    def determine_economy(self, loc_size):
        #Pop size is determined by getting first result from individual location size, holding the numeric value
        pop_size = loc_size.get(list(loc_size.keys())[0])
        #Should add region modifier to economy after the fact
        #TODO: Modify population modifier to add economic value points
        population_modifier = {"Large": [80000, 1500000],
                             "Medium": [22000, 79999],
                             "Small": [3000, 21999],
                             "Tiny": [1, 2999]}
        print("break")
        modifier_range = {"Large": [-500, 1500],
                          "Medium": [100, 900],
                          "Small": [-300, 600],
                          "Tiny": [-600, 300]}
        for i in population_modifier:
            pop_range = population_modifier.get(i)
            print(type(pop_range), pop_size)
            if pop_range[0] <= pop_size<= pop_range[1]:

                print("Size is contained within {}".format(population_modifier.get(i)))
                numeric_modifier = modifier_range.get(i)
                pop_modifier = random.randint(numeric_modifier[0], numeric_modifier[1])
                break
        print(pop_modifier)
        economic_value = random.randint(0, 2000)
        pop_modifier = pop_modifier + economic_value
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
        if pop_modifier < 0:
            economic_modifier = "Desolate"
        else:
            for g in economic_status:
                economic_tag = economic_status.get(g)
                
        return "Hello"

    def determine_population_ration(self, location, size):
        print("Starting")

def populate_region():
    print("Populating region")
    #TODO: create 5-7 regions, add to them a set amount of each size (6 cities, 15 towns, 25+ villages, x many tiny)
town = Location()
print(town.__dict__)
print(dir(town))
size = town.location_size