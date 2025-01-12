def displayInventory(inventory):
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + " " + str(key))
        item_total += value

    print(f"Total Number of Items: {item_total}")


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(stuff)
print("****************")


def add_to_inventory(inventory, add_items):
    for item in add_items:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item] = 1
    return inventory
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(stuff, dragon_loot)

displayInventory(stuff)