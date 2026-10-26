import itertools

def distance_between_cells(start, target, a):
    pass

number_of_cells, number_of_hops = map(int, input().split(" "))
targets = input().split(" ")

if number_of_hops <= number_of_cells:
    print(*targets + ["a" for _ in range(number_of_cells - number_of_hops)])
else:
    cells = set(targets)
    shortest_distance = float("inf")
    result = None
    if len(cells) < number_of_cells:
        for number_of_cells_used in range(len(cells), number_of_cells + 1):
            # If we have more cells than we use, they should always go at the start/end and they don't matter
            for ordering in itertools.permutations(targets, number_of_cells_used):  # permutations on targets rather than product on cells as there's no reason to have a cell more times than it is visited
                if any(c not in ordering for c in cells): continue
                raise NotImplementedError()
    else:
        for ordering in itertools.permutations(cells):
            # No repeats, so very simple
            distance = 0
            for i, start_pos in enumerate(targets[:-1]):
                end_pos = targets[i + 1]
                distance += abs(ordering.index(end_pos) - ordering.index(start_pos))
                if distance > shortest_distance:
                    break
            if distance < shortest_distance:
                shortest_distance = distance
                result = " ".join(ordering)
    print(result)
