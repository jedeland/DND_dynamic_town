

#This file initiates a store class, using data from the above json data and offers options to include pathfinder data
#Pathfinder data can be found here, with minor changes to the files to make the items 5e compatible
#https://gitlab.com/jrmiller82/pathfinder-2-sqlite/-/blob/master/data/weapons.yaml

class Store:
    def __init__(self, *args):
        self.name = self.find_valid_name(self.culture)
        self.store_type = self.determine_store_type(self.remaining_stores)
    print("Creating store class")

    def find_valid_name(self, culture):
        #This function should use the culture input to determine where the names will come from using method 1 : using name data from the generators before
        #Method 2 would use a small data scraping database that will reference cultural names : French: boutique, maison ect German: Brauerei, Metzger
        print("Test name being returned")
        return "Bobbies Blacksmiths"

    def determine_store_type(self, stores):
        #This function will use stores (called in world class) to determine which types of stores are still needed, it will take the first call and set up the store
        return "Blacksmith"