

#This file initiates a store class, using data from the above json data and offers options to include pathfinder data
#Pathfinder data can be found here, with minor changes to the files to make the items 5e compatible
#https://gitlab.com/jrmiller82/pathfinder-2-sqlite/-/blob/master/data/weapons.yaml
import random

from name_data.name_controller import get_single_name


class Store:
    #Current args: culture, remaining_stores, region_wealth
    # Location size and culture are provided by a Location class, so town.culture and town.location_size are the arguments provided
    def __init__(self, culture, store_type, region_wealth, *args):
        #Location size is passed by the Location class
        self.store_type = store_type
        self.name = self.find_valid_name(culture, self.store_type)
        self.store_wealth = self.determine_regional_wealth(region_wealth)
        self.inventory = self.populate_stock(self.store_wealth, outclasses_area=True)
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
        affix_list = {"General_Store": ["Storage stop", "Shop", "Boutique", "Kiosk"],
                      "Wandmaker": ["Emporium", "Enchantments", "Sanctum", "Arcanium" ],
                      "Alchemist": ["Emporium", "Enchantments", "Sanctum", "Arcanium", "Flask Makers"],
                      "Enchanter": ["Emporium", "Enchantments", "Sanctum", "Arcanium", "Rubricurium"],
                      "Scribe": ["Quillery", "Scribe Services", "Library", "Scriptures", "Antique Books"],
                      "Blacksmith": ["Smithy", "Forge", "Weaponsmiths", "Armoursmiths", "Anvil", "Arsenal"]}
        name = f"{name}'s {random.choice(affix_list[store_type])}"

        return name

    def determine_regional_wealth(self, local_wealth):
        #This will set out how wealthy the local area is, and add in some variance to determine how wealthy the store is
        outclasses_area = False
        #Populate stock uses the wealth calculation to make a reasonable inventory for the store
        #inventory = self.populate_stock(local_wealth, outclasses_area)
        return "nothing"

    @staticmethod
    def populate_stock(local_wealth, outclasses_area):
        #Calculates what could be available
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