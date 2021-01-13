import random


class Location:
    def __init__(self, *args):
        #Pop input should be introduced in the region class
        pop_input = random.randint(0, 100000)

        self.location_size = self.determine_size(pop_input)
        loc_size = self.location_size.get(list(self.location_size.keys())[0])
        self.economic_situation = self.determine_economy(self.location_size)
        self.npc_ratio = self.determine_npc_ratio(loc_size, self.economic_situation)
        print(loc_size)

    def determine_size(self, population):
        #Reused this from lig
        region_types = {"Large": ["City", "Grand Fortress", "Grand Library", "Grand City", "Imperial Free City"],
                             "Medium": ["Town", "Castle", "University Town", "Market Town", "Grand Harbour"],
                             "Small": ["Village", "Fief", "Abbey", "Fortification", "Barony", "Barracks"],
                             "Tiny": ["Hamlet", "Settlement", "Hunter's Post", "Outpost", "Chapel"]}
        #Regional population should range from 80,000 to 3 million, for now it is 10k maximum to use randint more effectively
        region_population = {"Large": [80000, 100000],
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
        population_modifier = {"Large": [80000, 160000],
                             "Medium": [22000, 79999],
                             "Small": [3000, 21999],
                             "Tiny": [1, 2999]}
        print("break")
        modifier_range = {"Large": [-300, 1200],
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

        economic_value = random.randint(0, 2000)
        pop_modifier = pop_modifier + economic_value
        economic_status = {"Affluent": [3900, 4200],
                           "Prosperous": [3500, 3899],
                           "Rich": [3000, 3499],
                           "Strong": [2300, 2999],
                           "Stable": [1700, 2299],
                           "Average": [900, 1699],
                           "Struggling": [500, 899],
                           "Poor": [250, 499],
                           "Impoverished": [100, 249],
                           "Desolate": [0, 99]
                           }
        if pop_modifier < 0:
            return "Desolate"
        else:
            for g in economic_status:
                economic_tag = economic_status.get(g)
                if economic_tag[0] <= pop_modifier <= economic_tag[1]:
                    print("Economic Status is {}".format(g))
                    status = g
                    return g



    def determine_npc_ratio(self, loc_size, pop_economy):
        #Usable NPC's should range from 40 - 500 with a reserve amount of 2x the chosen amount
        #TODO: Load npc ration with NPC objects, using a future npc_class.py
        print(loc_size)
        print("Starting")

def populate_region():
    print("Populating region")
    #TODO: create 5-7 regions, add to them a set amount of each size (6 cities, 15 towns, 25+ villages, x many tiny)
town = Location()
print(town.__dict__)
print(dir(town))
size = town.location_size