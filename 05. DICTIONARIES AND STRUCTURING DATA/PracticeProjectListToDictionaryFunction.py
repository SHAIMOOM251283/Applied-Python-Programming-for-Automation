#items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#def displayInventory(inventory):
#    print("Inventory:")
#    total_items = 0
#    for key, value in inventory.items():
#        print(f"{key}: {value}")
#        total_items += value
#    print(f"Total number of items: {total_items}")
#displayInventory(items)

items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
items = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for key, value in inventory.items():
        print(f"{key}: {value}")
        total_items += value
    print(f"Total number of items: {total_items}")
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory
displayInventory(items)
updated_inventory = addToInventory(items, dragonLoot)
print("\nUpdated Inventory:")
displayInventory(updated_inventory)

items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
items = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for key, value in inventory.items():
        print(f"{key}: {value}")
        total_items += value
    print(f"Total number of items: {total_items}")
def addItemsToInventory(inventory, items_to_add):
    for item in items_to_add:
        inventory[item] = inventory.get(item, 0) + 1
# Call the function to add items to the existing inventory
addItemsToInventory(items, dragonLoot)
# Display the updated inventory
displayInventory(items)

