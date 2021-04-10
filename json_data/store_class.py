

#This file initiates a store class, using data from the above json data and offers options to include pathfinder data
#Pathfinder data can be found here, with minor changes to the files to make the items 5e compatible
#https://gitlab.com/jrmiller82/pathfinder-2-sqlite/-/blob/master/data/weapons.yaml
import random
from pprint import pprint

import yaml

from name_data.name_controller import get_single_name


class Store:
    #Current args: culture, remaining_stores, region_wealth
    # Location size and culture are provided by a Location class, so town.culture and town.location_size are the arguments provided
    def __init__(self, culture, store_type, region_wealth):
        #Location size is passed by the Location class
        self.store_type = store_type
        self.name = self.find_valid_name(culture, self.store_type)
        self.store_wealth = self.determine_store_wealth(region_wealth)
        self.inventory = self.populate_stock(self.store_type, self.store_wealth, outclasses_area=True)
        self.notable_npcs = self.create_npcs(culture, self.store_wealth)
    print("Creating store class")

    @staticmethod
    def determine_store_type(region_store):
        #This function will use stores (called in world class) to determine which types of stores are still needed,
        # it will take the first call and set up the store
        # Should determine whether the store is a citizen_store or a hero_store
        assign_types = ["General_Store", "Wandmaker", "Alchemist", "Enchanter", "Scribe"]


        return "Blacksmith"

    @staticmethod
    def find_valid_name(culture, store_type):
        #This function should use the culture input to determine where the names will come from using method 1 : using name data from the generators before
        #Method 2 would use a small data scraping database that will reference cultural names : French: boutique, maison ect German: Brauerei, Metzger
        print("Test name being returned")
        name = get_single_name(culture)
        affix_list = {"General_Store": ["Storage Stop", "Shop", "Boutique", "Kiosk", "General Store"],
                      "Wandmaker": ["Emporium", "Enchantments", "Sanctum", "Arcanium" ],
                      "Alchemist": ["Emporium", "Enchantments", "Sanctum", "Arcanium", "Flask Makers", "Apothecary"],
                      "Enchanter": ["Emporium", "Enchantments", "Sanctum", "Arcanium", "Rubricurium"],
                      "Scribe": ["Quillery", "Scribe Services", "Library", "Scriptures", "Antique Books"],
                      "Blacksmith": ["Smithy", "Forge", "Weaponsmiths", "Armoursmiths", "Anvil", "Arsenal"]}
        #Concats string
        name = f"{name}'s {random.choice(affix_list[store_type])}"

        return name

    def determine_store_wealth(self, local_wealth):
        #This will set out how wealthy the local area is, and add in some variance to determine how wealthy the store is
        outclasses_area = False
        upper_band, lower_band = ["Affluent","Prosperous", "Rich", "Strong"], ["Average", "Struggling", "Poor"]
        #Stores in upper column can have maximum 2 legendary artifacts, and minimum have a very rare item.
        #Stores in lower column can have max 2 rare artifacts, and minimum one common magic item

        if local_wealth in upper_band:
            print("This area is quite rich!")
            store_wealth = {"artifact": range(0,1), "legendary": range(0, 2), "very rare": range(1, 4), "rare": range(1,5),
                            "uncommon": range(0, 3), "common": range(0,3)}

        elif local_wealth in lower_band:
            print("This area has potential ...")
            outclasses_area = random.randint(1, 20)
            store_wealth = {"very rare": range(0, 1), "rare": range(0,2),
                            "uncommon": range(0, 4), "common": range(0,4)}
            if outclasses_area == 19 or outclasses_area == 20:
                print("The local store, {}, is truly out of place, its fine goods and raiment's seem odd in this rather less fortunate region ...".format(self.name))
                outclasses_area = True
                store_wealth = {"artifact": range(1, 2), "legendary": range(1, 2), "very rare": range(0, 2),
                                "rare": range(0, 2),
                                "uncommon": range(0, 4), "common": range(0, 4)}

        #Populate stock uses the wealth calculation to make a reasonable inventory for the store
        inventory = self.populate_stock(self.store_type, local_wealth, outclasses_area)

        store_wealth = {"store_wealth": store_wealth, "inventory": inventory}

        return local_wealth

    @staticmethod
    def populate_stock(store_type, local_wealth, outclasses_area):
        #Calculates what could be available
        with open("cleaned_data/items-base.yaml", "r+") as f:
            print()
            items_dict = yaml.safe_load(f)
        first = list(items_dict.keys())[0]
        print("First is ", first)
        items = items_dict[first]
        stock = ["Sword", "Dagger", "Horse"]
        print(stock)
        return stock

    def create_npcs(self, culture, local_wealth):
        #Creates NPCs using namegen, creates "NPC" Objects
        print("Npcs")
        npcs = ["Bob", "Bill", "Jenny"]
        assign_quests = self.find_quests(npcs, local_wealth)
        return npcs

    def find_quests(self, npcs, local_wealth):

        return "There are no quests"

# new_store = Store()