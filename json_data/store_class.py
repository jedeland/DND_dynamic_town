

#This file initiates a store class, using data from the above json data and offers options to include pathfinder data
#Pathfinder data can be found here, with minor changes to the files to make the items 5e compatible
#https://gitlab.com/jrmiller82/pathfinder-2-sqlite/-/blob/master/data/weapons.yaml

class Store:
    #Current args: culture, remaining_stores, region_wealth
    def __init__(self, *args):
        self.name = self.find_valid_name(self.culture)
        self.store_type = self.determine_store_type(self.remaining_stores)
        self.store_wealth = self.determine_regional_wealth(self.region_wealth)
        self.inventory = self.populate_stock(self.store_wealth)
        self.notable_npcs = self.create_npcs(self.culture, self.store_wealth)
    print("Creating store class")

    def find_valid_name(self, culture):
        #This function should use the culture input to determine where the names will come from using method 1 : using name data from the generators before
        #Method 2 would use a small data scraping database that will reference cultural names : French: boutique, maison ect German: Brauerei, Metzger
        print("Test name being returned")
        return "Boobies Blacksmiths"

    def determine_store_type(self, stores):
        #This function will use stores (called in world class) to determine which types of stores are still needed, it will take the first call and set up the store
        return "Blacksmith"

    def determine_regional_wealth(self, local_wealth):
        #This will set out how wealthy the local area is, and add in some variance to determine how wealthy the store is
        outclasses_area = False
        #Populate stock uses the wealth calculation to make a reasonable inventory for the store
        inventory = self.populate_stock(local_wealth, outclasses_area)
        return "Stable"

    def populate_stock(self, local_wealth, outclasses_area):
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