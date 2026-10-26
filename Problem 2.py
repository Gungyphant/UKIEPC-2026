import itertools

lowest = {k: 10001 for k in "xyz"}
highest = {k: -10001 for k in "xyz"}
point_sets = []
for axes in ["xy", "zy", "xz"]:  # which coordinates are they
    number_of_points, *data = map(int, input().split(" "))
    points: list[tuple[int, int]] = []
    is_second_coordinate = False
    first_coordinate = None
    for datum in data:
        if not is_second_coordinate:
            first_coordinate = datum
        if is_second_coordinate:
            points.append((first_coordinate, datum))
        is_second_coordinate = not is_second_coordinate
    point_sets.append(points)

    first_axis, second_axis = axes

    lowest[first_axis] = min(lowest[first_axis], min(p[0] for p in points))
    lowest[second_axis] = min(lowest[second_axis], min(p[1] for p in points))

    highest[first_axis] = max(highest[first_axis], max(p[0] for p in points))
    highest[second_axis] = max(highest[second_axis], max(p[1] for p in points))

points_in_statue = [(x, y, z) for x in range(lowest["x"], highest["x"] + 1) for y in range(lowest["y"], highest["y"] + 1) for z in range(lowest["z"], highest["z"] + 1)]

# TODO: eliminate the points for all z that don't fit first set; all x that don't fit second, etc
pass
