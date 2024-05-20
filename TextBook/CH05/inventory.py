def display_inventory(inventory):
    print("持ち物リスト:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"アイテム総数: {item_total}")

stuff = {
    'ロープ': 1,
    'たいまつ': 6,
    '金貨': 42,
    '手裏剣': 1,
    '矢': 12
}

display_inventory(stuff)
