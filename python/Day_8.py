"Advent of Code 2019 Day 08"

from collections import defaultdict

def check_corruption(layers):
    """Return one count * two count of layer with the least zeros in it."""
    least_zeros = (None, None)
    for layer, values in layers.items():
        zeros = values.count(0)
        if not least_zeros[0] or zeros < least_zeros[0]:
            least_zeros = (zeros, layer)

    zeros_layer = layers[least_zeros[1]]
    return zeros_layer.count(1) * zeros_layer.count(2)

def extract_layers(raw, size):
    layers2 = defaultdict(list)
    layer2 = -1

    for i in range(len(raw)):
        if not i % size:
            layer2 += 1
        layers2[layer2].append(raw[i])

    return layers2


def print_image(layers2):
    for y in range(6):
        for x in range(25):
            pos = x + y * 25
            for lay in range(100):
                if layers2[lay][pos] == 2:
                    continue
                if layers2[lay][pos] == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
                break
        print()


with open('day_8.input', 'r') as f:
    digits = [int(x) for x in list(f.read().strip())]

height, width = (6, 25)
size = height * width

i = 0
layers = {}
layer = 0
while i < len(digits):
    layers[layer] = digits[i: i+size]
    i += size
    layer += 1

# Answer One
print("Corruption Check", check_corruption(layers))

# Answer Two

size = 25 * 6
layers2 = extract_layers(digits, size)

print_image(layers2)