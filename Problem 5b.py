AMOUNTS_NEEDED = [12, 12, 40]

amounts = list(map(float, input().split(" ")))

amount_bought = [0.0 for _ in range(3)]

while any(n > 0 for n in amounts):
    if all(n > 0 for n in amounts):
        parts_used = min([amount / amount_needed for amount, amount_needed in zip(amounts, AMOUNTS_NEEDED)])
        amounts = [amount - parts_used * amount_needed for amount, amount_needed in zip(amounts, AMOUNTS_NEEDED)]
    else:
        parts_used = min([amount / amount_needed for amount, amount_needed in zip(amounts, AMOUNTS_NEEDED)], key=lambda x: 1000000 if x == 0 else x)
        amounts_required = [parts_used * amount_needed for amount_needed in AMOUNTS_NEEDED]
        pass
