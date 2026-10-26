import math

import itertools


def get_efficiencies(usages):
    result = {}
    for i, used in enumerate(usages):
        if not used: continue
        neighbours = 0
        if i != 0 and usages[i - 1]:
            neighbours += 1
        if i != len(usages) - 1 and usages[i + 1]:
            neighbours += 1
        result[i] = [1, 0.6, 0.3][neighbours]
    return result


number_of_tasks, number_of_slots = map(int, input().split(" "))

durations = list(map(int, input().split(" ")))

# 2 processors at 60% get an average 60% usage of the 2 slots, whereas 1 at 100% and one empty gets 50% average, so using 2 is better
# 3 proc: 60, 30, 60 gets 50%; gap in mid get 66%

# There's no reason to leave gaps; if odd number of slots, #_#_#_...# ceil(n/2); if even, #_#_...#_ n/2
# There's no reason to use more than there are processes
for processors_used in range(min(number_of_tasks, math.ceil(number_of_slots / 2)), number_of_tasks + 1):
    usages = [False for _ in range(number_of_slots)]
    processors_to_place = processors_used

    # Start by placing in the first slot
    usages[0] = True
    processors_to_place -= 1

    if processors_to_place <= math.ceil((number_of_slots - 2) / 2):
        # We don't need any to be adjacent
        for i in range(2, number_of_slots, 2):
            usages[i] = True
            processors_to_place -= 1
    else:
        for positions in itertools.combinations(range(1, number_of_slots - 1), processors_to_place):
            pass

    efficiencies = get_efficiencies(usages)

    for assignments in itertools.permutations((i for i, used in enumerate(usages) if used), min(number_of_tasks, processors_used)):
        time = max(durations[n]/efficiencies[assignments[n]] for n in range(number_of_tasks))
        pass
