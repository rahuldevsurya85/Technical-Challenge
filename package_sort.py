def sort(width, height, length, mass):
    """
    Sorts packages into STANDARD, SPECIAL, or REJECTED stacks based on size and mass.

    - A package is BULKY if its volume >= 1,000,000 or any dimension >= 150.
    - A package is HEAVY if its mass >= 20.
    - If a package is both BULKY and HEAVY, it is REJECTED.
    - If a package is either BULKY or HEAVY (but not both), it is SPECIAL.
    - Otherwise, it is STANDARD.
    """
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example test cases
test_cases = [
    (50, 50, 50, 10),     # STANDARD
    (200, 20, 30, 5),     # SPECIAL (bulky)
    (20, 20, 20, 25),     # SPECIAL (heavy)
    (150, 150, 150, 20),  # REJECTED (bulky and heavy)
    (100, 100, 100, 20),  # SPECIAL (heavy)
    (149, 149, 151, 5),   # SPECIAL (bulky)
    (10, 10, 10, 19.99),  # STANDARD
]

for w, h, l, m in test_cases:
    result = sort(w, h, l, m)
    print(f"sort({w}, {h}, {l}, {m}) -> {result}")