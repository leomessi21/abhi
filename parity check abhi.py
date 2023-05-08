def parity_check(binary_string):
    # Count the number of 1's in the binary string
    num_ones = 0
    for bit in binary_string:
        if bit == '1':
            num_ones += 1

    # Check parity
    if num_ones % 2 == 0:
        print("Even parity detected.")
    else:
        print("Odd parity detected.")

# Example usage
binary_string = '1010111'
parity_check(binary_string)
