"Advent of Code 2019 Day 04"

def read_file(name):
    with open(f"day_4.input") as f:
        content = f.readlines()
    return [x.strip() for x in content]



def number_matching_criteria(part_two=False):
    "Return number of numbers mathching criteria."
    num_matched = 0
    input = read_file("04")
    start, end = [int(num) for num in input[0].split("-")]
    for n in range(start, end + 1):
        digits = [int(x) for x in list(str(n))]
        adjacent = False
        increase = False
        if digits == sorted(digits):
            increase = True
        else:
            pass

        for digit in digits:
            if part_two:
                if digits.count(digit) == 2:
                    adjacent = True
                    break
            else:
                if digits.count(digit) > 1:
                    adjacent = True
                    break

        if adjacent and increase:
            num_matched += 1

    return num_matched


# Answer One
print("Matches under first criteria:", number_matching_criteria())

# Answer Two
print("Matches under second criteria:", number_matching_criteria(True))