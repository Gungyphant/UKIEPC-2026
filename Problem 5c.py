AMOUNTS_NEEDED = [12, 12, 40]

amounts = list(map(float, input().split(" ")))

parts_for_each = [amount / amount_needed for amount, amount_needed in zip(amounts, AMOUNTS_NEEDED)]

parts_made = max(parts_for_each)
part_deficit = [parts_made - parts for parts in parts_for_each]
amount_to_buy = [deficit * amount_needed for deficit, amount_needed in zip(part_deficit, AMOUNTS_NEEDED)]

print(*amount_to_buy)
