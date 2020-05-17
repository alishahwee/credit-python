from cs50 import get_int

# Define main function
def main():
    # Declare variables
    n = get_int("Number: ")
    digits = count_digits(n)
    checksum = checksum_value(n)

    # Check validity
    if checksum == 0 and digits > 12 and digits < 17:
        card_type(n, digits)
    else:
        print("INVALID")

# Find card type
def card_type(n, digits):
    digits_left = digits
    first_digit = second_digit = 0

    # Iterate through n to reach the first and second
    while n != 0:
        n //= 10
        digits_left -= 1
        if digits_left == 1:
            first_digit = n % 10
        elif digits_left == 2:
            second_digit = n % 10

    # Condition to check which credit card
    if first_digit == 3 and (second_digit == 4 or second_digit == 7) and digits == 15:
        print("AMEX")
    elif first_digit == 5 and (second_digit == 1 or second_digit == 2 or second_digit == 3 or second_digit == 4 or second_digit == 5) and digits == 16:
        print("MASTERCARD")
    elif first_digit == 4 and (digits == 13 or digits == 16):
        print("VISA")
    else:
        print("INVALID")

# Calculate checksum
def checksum_value(n):
    # Initialize values
    count = sum = acc = 0

    # Iterate through n
    while n != 0:
        current_digit = n % 10
        # Factor every other digit starting with second-to-last
        if count % 2 == 1:
            factor_digit = current_digit * 2
            while factor_digit != 0:
                acc += factor_digit % 10
                factor_digit //= 10
        # Add leftover digits together
        elif count % 2 == 0:
            sum += current_digit
        n //= 10
        count += 1
    # Final sum
    sum += acc
    return sum % 10

# Count the total digits
def count_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

main()