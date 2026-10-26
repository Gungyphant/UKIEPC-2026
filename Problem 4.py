import math


def find_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


number_of_verts, start_vert, end_vert = map(int, input().split(" "))
start_vert -= 1
end_vert -= 1

verts = []
for i in range(number_of_verts):
    verts.append(list(map(int, input().split(" "))))

triangles = []
for i in range(number_of_verts - 2):
    triangles.append(list(map(lambda x: int(x) - 1, input().split(" "))))

distance_matrix = [[None for _ in range(len(verts))] for _ in range(len(verts))]

for triangle in triangles:
    a, b, c = triangle
    distance_matrix[a][b] = distance_matrix[b][a] = find_distance(verts[a], verts[b])
    distance_matrix[a][c] = distance_matrix[c][c] = find_distance(verts[a], verts[c])
    distance_matrix[b][c] = distance_matrix[c][b] = find_distance(verts[b], verts[c])

visited = {start_vert: 0}  # vert: distance from start
to_check = [start_vert]
while end_vert not in visited:
    vert_to_check = min(to_check, key=lambda x: visited[x])  # Pick the node closest to the start
    neighbours = [(node, distance) for node, distance in enumerate(distance_matrix[vert_to_check]) if distance is not None]
    for node, distance in neighbours:
        full_distance = visited[vert_to_check] + distance
        if node not in visited and node not in to_check:
            visited[node] = full_distance
            to_check.append(node)
        elif full_distance < visited[node]:
            visited[node] = full_distance
    to_check.remove(vert_to_check)

print(visited[end_vert])
