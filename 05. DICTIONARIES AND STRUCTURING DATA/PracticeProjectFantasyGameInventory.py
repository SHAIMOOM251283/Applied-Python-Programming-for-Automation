items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
   print("Inventory:")
   item_total = 0
   for k, v in inventory.items():
      print(str(v) + ' ' + k)
      item_total += v
      print("Total number of items: " + str(item_total))
displayInventory(items)

items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
      print(f"{key}: {value}") #Inside the f-string, you can include expressions (like variables or calculations) enclosed in curly braces {}.
      item_total += value
    print(f"Total number of items: {item_total}")
#    print("Total number of items: " + str(item_total))
displayInventory(items)

items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for key, value in inventory.items():
        print(f"{key}: {value}")
        total_items += value
    print(f"Total number of items: {total_items}")
displayInventory(items)