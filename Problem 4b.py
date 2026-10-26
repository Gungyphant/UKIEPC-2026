import math


def find_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_visible_nodes(node):
    result = []
    this_vert = verts[node]
    for other_node, other_vert in enumerate(verts):
        visible = True
        if other_vert[0] == this_vert[0]:
            gradient = 10000000
        elif other_vert[1] == this_vert[1]:
            gradient = 0.00000001
        else:
            gradient = (other_vert[1] - this_vert[1]) / (other_vert[0] - this_vert[0])
        intercept = this_vert[1] - gradient * this_vert[0]
        min_x, max_x = sorted([this_vert[0], other_vert[0]])
        min_y, max_y = sorted([this_vert[1], other_vert[1]])
        for wall in walls:
            wall_axis, wall_min, wall_max, wall_other_axis_val = wall
            if wall_axis == "x":
                if min_x <= wall_other_axis_val <= max_x:
                    line_y_at_wall = gradient * wall_other_axis_val + gradient
                    if wall_min <= line_y_at_wall <= wall_max:
                        visible = False
                        break
            else:
                if min_y <= wall_other_axis_val <= max_y:
                    line_x_at_wall = (wall_other_axis_val - intercept) / gradient
                    if wall_min <= line_x_at_wall <= wall_max:
                        visible = False
                        break
        if visible:
            result.append(other_node)
    return result


number_of_verts, start_vert, end_vert = map(int, input().split(" "))
start_vert -= 1
end_vert -= 1

verts = []
walls = []  # (axis, min, max, other_axis_val), e.g. (3, 1) to (3, 2) is (y, 1, 2, 3)
for i in range(number_of_verts):
    verts.append(list(map(int, input().split(" "))))
    if len(verts) > 1:
        wall_axis = "y" if verts[-1][0] != verts[-2][0] else "x"
        if wall_axis == "x":
            min_val, max_val = sorted([verts[-1][0], verts[-2][0]])
            other_axis_val = verts[-1][1]
        else:
            min_val, max_val = sorted([verts[-1][1], verts[-2][1]])
            other_axis_val = verts[-1][0]
        walls.append((wall_axis, min_val, max_val, other_axis_val))

triangles = []
for i in range(number_of_verts - 2):
    triangles.append(list(map(lambda x: int(x) - 1, input().split(" "))))

visited = {start_vert: 0}  # vert: distance from start
to_check = [start_vert]
while end_vert not in visited:
    vert_to_check = min(to_check, key=lambda x: visited[x])  # Pick the node closest to the start
    neighbours = [(node, find_distance(verts[vert_to_check], verts[node])) for node in get_visible_nodes(vert_to_check)]
    for node, distance in neighbours:
        full_distance = visited[vert_to_check] + distance
        if node not in visited and node not in to_check:
            visited[node] = full_distance
            to_check.append(node)
        elif full_distance < visited[node]:
            visited[node] = full_distance
    to_check.remove(vert_to_check)

print(visited[end_vert])
