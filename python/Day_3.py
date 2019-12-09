"Advent of Code 2019 Day 03"

from collections import defaultdict

def read_file(name):
    with open(f"day_3.input") as f:
        content = f.readlines()
    return [x.strip() for x in content]


def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])


def get_wire_positions(wire):
    x, y = 0, 0
    positions = set()

    for i in range(len(wire)):
        for _ in range(int(wire[i][1:])):
            direction = wire[i][0]

            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "D":
                y += 1
            elif direction == "U":
                y -= 1

            positions.add((x, y))

    return positions


def get_distance_for_crossings(wire, crossings2):
    crossing2 = defaultdict(int)
    distance = 0
    x, y = 0, 0

    for i in range(len(wire)):
        for _ in range(int(wire[i][1:])):
            direction = wire[i][0]

            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "D":
                y += 1
            elif direction == "U":
                y -= 1

            distance += 1

            if (x, y) in crossings2:
                crossing2[(x, y)] = distance

    return crossing2

def solve():
    input = read_file("03")
    wire_1 = input[0].split(",")
    wire_2 = input[1].split(",")

    positions_1 = get_wire_positions(wire_1)
    positions_2 = get_wire_positions(wire_2)

    crossings = positions_1.intersection(positions_2)

    return min([manhattan(pos) for pos in crossings])

def solve2():
    input = read_file("03")
    wire_1 = input[0].split(",")
    wire_2 = input[1].split(",")

    x1, y1, x2, y2 = 0, 0, 0, 0

    positions_1 = get_wire_positions(wire_1)
    positions_2 = get_wire_positions(wire_2)

    crossings2 = positions_1.intersection(positions_2)

    crossing_distance_1 = get_distance_for_crossings(wire_1, crossings2)
    crossing_distance_2 = get_distance_for_crossings(wire_2, crossings2)

    return min([crossing_distance_1[crossing2] + crossing_distance_2[crossing2] for crossing2 in crossings2])


result = solve()
print(f"Solution: {result}")

result2 = solve2()
print(f"Solution: {result2}")