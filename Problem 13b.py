import math
from functools import cache
import itertools
from collections import Counter


class MyCounter(Counter):
    def __hash__(self):
        return hash(",".join(f"{k}:{v}" for k, v in self.items()))


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
    return MyCounter(result.values())


@cache
def get_best_time(efficiencies: MyCounter):
    best_time = float("inf")
    de_countered = sum([[k] * v for k, v in efficiencies.items()], [])
    for assignments in itertools.permutations(range(len(de_countered)), min(number_of_tasks, processors_used)):
        worst_time = 0
        for n in range(number_of_tasks):
            time = durations[n] / de_countered[assignments[n]]
            if time > worst_time:
                worst_time = time
            if time > best_time: break
        if worst_time < best_time:
            best_time = worst_time
    return best_time


number_of_tasks, number_of_slots = map(int, input().split(" "))

durations = list(map(int, input().split(" ")))

# 2 processors at 60% get an average 60% usage of the 2 slots, whereas 1 at 100% and one empty gets 50% average, so using 2 is better
# 3 proc: 60, 30, 60 gets 50%; gap in mid get 66%

# There's no reason to leave gaps; if odd number of slots, #_#_#_...# ceil(n/2); if even, #_#_...#_ n/2
# There's no reason to use more than there are processes
processors_used = number_of_tasks
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
    print(get_best_time(get_efficiencies(usages)))
else:
    best_time_found = float("inf")
    for positions in itertools.combinations(range(1, number_of_slots), processors_to_place):
        local_usages = [usages[i] or i in positions for i in range(number_of_slots)]
        time_for_positions = get_best_time(get_efficiencies(local_usages))
        if time_for_positions < best_time_found:
            best_time_found = time_for_positions
    print(best_time_found)
