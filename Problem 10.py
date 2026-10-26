import itertools

number_of_swimmers, number_of_lanes = map(int, input().split(" "))

speeds = list(map(int, input().split(" ")))

best_average_speed = 0
best_assignments = None
for assignments in itertools.product(range(1, number_of_lanes + 1), repeat=number_of_swimmers):
    lane_swimmers = [[speed for i, speed in enumerate(speeds) if assignments[i] == lane] for lane in range(1, number_of_lanes + 1)]
    lane_speeds = [min(lane, default=0) for lane in lane_swimmers]
    average_speed = sum(speed * len(lane) for speed, lane in zip(lane_speeds, lane_swimmers)) / number_of_swimmers
    if average_speed > best_average_speed:
        best_average_speed = average_speed
        best_assignments = assignments

print(best_average_speed)
print(*best_assignments)
