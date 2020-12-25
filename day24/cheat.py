import re
my_regex = "((?<!n|s)e)|((?<!n|s)w)|(se)|(nw)|(sw)|(ne)"

flip_list = []
tile_map = {}

input_filename = "day24/input.txt"
# input_filename = "sample_input.txt"
with open(input_filename, 'r') as reader:
    for line in reader:
        temp = str(line.rstrip())
        flip_list.append(["".join(d) for d in re.findall(my_regex, temp)])


def hex_step(location, direction):
    # Function to take a step in the given direction on the hexagonal grid
    x = location[0]
    y = location[1]
    z = location[2]
    if direction == 'w':
        return x - 1, y + 1, z
    elif direction == 'e':
        return x + 1, y - 1, z
    elif direction == 'nw':
        return x, y + 1, z - 1
    elif direction == 'ne':
        return x + 1, y, z - 1
    elif direction == 'se':
        return x, y - 1, z + 1
    elif direction == 'sw':
        return x - 1, y, z + 1
    else:
        print(f"Unknown direction: {direction}. Location = {location}")
        return location


def neighbor_coord_list(coords: tuple):
    # A function to get the coordinates of all tiles next to the tile at coords
    # Using an x, y, z hexagonal coordinate grid

    tx = coords[0]
    ty = coords[1]
    tz = coords[2]
    coord_list = [(tx - 1, ty + 1, tz), (tx + 1, ty - 1, tz), (tx, ty + 1, tz - 1),
                  (tx + 1, ty, tz - 1), (tx, ty - 1, tz + 1), (tx - 1, ty, tz + 1)]
    return coord_list


def update_map(c_dict: dict):
    # One round of Game of Life
    # Takes a dictionary of tile coordinates, counts neighbors, and updates tiles
    neighbor_count = {}

    # Find each black tile, and increment a neighbor counter for each of its neighbors
    for this_coord in c_dict:
        if c_dict[this_coord] == 'black':
            neighbor_list = neighbor_coord_list(this_coord)
            for this_neighbor in neighbor_list:
                try:
                    neighbor_count[this_neighbor] += 1
                except KeyError:
                    neighbor_count[this_neighbor] = 1

    # n_map is the new c_dict that we will build
    n_map = {}
    active_count = 0

    # Go through each tile with a black neighbor tile and flip it if necessary
    for this_coord in neighbor_count:
        try:
            current_state = c_dict[this_coord]
        except KeyError:
            current_state = 'white'
        if current_state == 'black' and neighbor_count[this_coord] not in [1, 2]:
            n_map[this_coord] = 'white'
        elif current_state == 'white' and neighbor_count[this_coord] == 2:
            n_map[this_coord] = 'black'
        else:
            n_map[this_coord] = current_state

        # Increment the counter if this tile is black after all the flipping
        if n_map[this_coord] == 'black':
            active_count += 1

    return n_map, active_count


for this_flipped_tile in flip_list:
    # Starting at the origin, step through each instruction and flip the tile
    loc = (0, 0, 0)
    for this_step in this_flipped_tile:
        loc = hex_step(loc, this_step)
    try:
        if tile_map[loc] == "black":
            tile_map[loc] = "white"
        else:
            tile_map[loc] = "black"
    except KeyError:
        tile_map[loc] = "black"

# Count the black tiles for part 1
p1counter = 0
for this_tile in tile_map:
    if tile_map[this_tile] == "black":
        p1counter += 1

# Game of life for part 2
for _ in range(100):
    tile_map, p2counter = update_map(tile_map)

print(f"Part 1: {p1counter}")
print(f"Part 2: {p2counter}")