# Technical-Challenge

## Package Sorting Function

This repository contains a Python function to sort packages based on their dimensions and mass.

### Function Logic

A package is classified into one of three categories:

- **STANDARD:** If the package is neither bulky nor heavy.
- **SPECIAL:** If the package is either bulky or heavy, but not both.
- **REJECTED:** If the package is both bulky and heavy.

#### Criteria:

- **Bulky:** 
  - Volume (width × height × length) is **greater than or equal to 1,000,000**.
  - **OR** any single dimension is **greater than or equal to 150**.
- **Heavy:** 
  - Mass is **greater than or equal to 20**.

### Example Usage

```python
def sort(width, height, length, mass):
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
```

### How to Run

1. Clone this repository.
2. Run the Python file containing the `sort` function and test cases.

### License

This project is licensed under the MIT License.
