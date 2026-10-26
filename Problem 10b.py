import itertools
import math

number_of_swimmers, number_of_lanes = map(int, input().split(" "))

unsorted_speeds = list(map(int, input().split(" ")))

# Split the speeds up into [number_of_lanes] groups
speeds = sorted(unsorted_speeds)
proto_splits = [i * len(speeds) / number_of_lanes for i in range(1, number_of_lanes)]
best_average_speed = 0
best_assignments = None
undecideds = [n for n in proto_splits if not n.is_integer()]
for round_ups in itertools.product([False, True], repeat=len(undecideds)):
    decision_id = 0
    splits = []
    for split in proto_splits:
        if not split.is_integer():
            if round_ups[decision_id]:
                splits.append(math.ceil(split))
            else:
                splits.append(math.floor(split))
            decision_id += 1
        else:
            splits.append(int(split))
    lanes = [speeds[:splits[0]]] + [speeds[splits[i]:splits[i + 1]] for i in range(len(splits) - 1)] + [speeds[splits[-1]:]]
    average_speed = sum(min(lane) * len(lane) for lane in lanes) / number_of_swimmers
    if average_speed > best_average_speed:
        best_average_speed = average_speed
        best_assignments = [next(i + 1 for i, lane in enumerate(lanes) if speed in lane) for speed in unsorted_speeds]
print(best_average_speed)
print(*best_assignments)
