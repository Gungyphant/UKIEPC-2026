import itertools

expression = input()
pre, result = expression.split("=")
addend1, addend2 = pre.split("+")

for values in itertools.permutations(range(10), 5):
    local_result = result
    for letter, val in zip("abcde", values):
        local_result = local_result.replace(letter, str(val))
    local_result = int(local_result)

    local_addend1 = addend1
    for letter, val in zip("abcde", values):
        local_addend1 = local_addend1.replace(letter, str(val))
    local_addend1 = int(local_addend1)

    if local_addend1 > local_result: continue

    local_addend2 = addend2
    for letter, val in zip("abcde", values):
        local_addend2 = local_addend2.replace(letter, str(val))
    local_addend2 = int(local_addend2)

    if local_addend1 + local_addend2 == local_result:
        print("".join(str(n) for n in values))
        exit()
print("impossible")
