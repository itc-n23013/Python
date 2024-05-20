from inventory import display_inventory
def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] += 1


inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
