"Advent of Code 2019 Day 01"

with open('day_1.input', 'r') as f:
    masses = [int(module_mass) for module_mass in f.readlines()]


def calculate_recursive_fuel(fuel_mass: object) -> object:
    """Calculate the recursive fuel needed to launch a mass of fuel."""
    new_fuel_mass = fuel_mass // 3 - 2
    if new_fuel_mass <= 0:
        return 0
    return new_fuel_mass + calculate_recursive_fuel(new_fuel_mass)


absolute_fuel_sum = 0
estimated_fuel_sum = 0
for module_mass in masses:
    fuel = module_mass // 3 - 2
    absolute_fuel_sum += fuel
    estimated_fuel_sum += fuel + calculate_recursive_fuel(fuel)

# Answer One
print("The absolute fuel sum is {}".format(absolute_fuel_sum))

# Answer Two
print("The estimated fuel sum is {}".format(estimated_fuel_sum))