stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory: dict):
    # your code goes here
    totalItemCount = 0
    print("Inventory:")
    # print each item's name and how many there are of that item
    # keep track of total number of all items
    for itemName, itemCount in inventory.items() :
        totalItemCount += itemCount
        print(itemCount, itemName)
    print("Total number of items:", totalItemCount)

displayInventory(stuff)