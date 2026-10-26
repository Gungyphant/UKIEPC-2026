import itertools


def paint_canvas(instructions):
    canvas = [["" for _ in range(width)] for _ in range(height)]
    for (axis, id, colour) in instructions:
        if axis == "y":
            canvas[id - 1] = [colour for _ in range(width)]
        else:
            canvas = [[colour if id - 1 == i else cell for i, cell in enumerate(row)] for row in canvas]
    return ["".join(line) for line in canvas]

height, width = map(int, input().split(" "))
target = [input() for _ in range(height)]
colours_used = list(set(sum((list(set(row)) for row in target), [])))
for number_of_paints in range(min(height, width), (height * width - (min(height, width) - 1)) + 1):  # At least, 1 paint for each row/column; at most, one paint for each square with the final one required to do an entire row/column
    for axes in itertools.product(["x", "y"], repeat=number_of_paints):
        for ids in itertools.product(range(max(width, height)), repeat=number_of_paints):
            if any((axes[i] == "x" and ids[i] > width or axes[i] == "y" and ids[i] > height) for i in range(number_of_paints)):
                continue
            for colours in itertools.product(colours_used, repeat=number_of_paints):
                instructions = [(axes[i], ids[i], colours[i]) for i in range(number_of_paints)]
                if paint_canvas(instructions) == target:
                    print(instructions)
                    exit()
print("impossible")
# print(*paint_canvas([("y", 1, "a"), ("y", 2, "a"), ("y", 3, "a"), ("y", 4, "a"), ("x", 5, "b")]), sep="\n")
