ELDERBERRIES_NEEDED, SUGAR_NEEDED, WATER_NEEDED = 12, 12, 40

elderberries, sugar, water = map(float, input().split(" "))

elderberries_bought = sugar_bought = water_bought = 0.0

while any(n > 0 for n in [elderberries, sugar, water]):
    if all(n > 0 for n in [elderberries, sugar, water]):
        parts_used = min(elderberries / ELDERBERRIES_NEEDED, sugar/SUGAR_NEEDED, water/WATER_NEEDED)
        elderberries -= parts_used * ELDERBERRIES_NEEDED
        sugar -= parts_used * SUGAR_NEEDED
        water -= parts_used * WATER_NEEDED
    else:
        parts_used = min(elderberries / ELDERBERRIES_NEEDED, sugar / SUGAR_NEEDED, water / WATER_NEEDED, key=lambda x: 1000000 if x == 0 else x)

