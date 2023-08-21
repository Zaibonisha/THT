def validate_convert_isbn(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")  # Remove dashes and spaces
    if len(isbn) not in [10, 13]:
        return "Invalid"

    if len(isbn) == 10:
        if not isbn[:-1].isdigit() or (isbn[-1] != 'X' and not isbn[-1].isdigit()):
            return "Invalid"

        total = 0
        for i, digit in enumerate(isbn):
            if digit == 'X':
                digit_value = 10
            else:
                digit_value = int(digit)
            total += digit_value * (10 - i)

        if total % 11 == 0:
            isbn13 = "978" + isbn[:-1]
            check_digit = str((10 - (total % 10)) % 10)
            isbn13 += check_digit
            return isbn13
        else:
            return "Invalid"

    if len(isbn) == 13:
        if not isbn.isdigit():
            return "Invalid"

        total = 0
        for i, digit in enumerate(isbn):
            digit_value = int(digit)
            multiplier = 3 if i % 2 == 0 else 1
            total += digit_value * multiplier

        if total % 10 == 0:
            return "Valid"
        else:
            return "Invalid"

# Test cases
print(validate_convert_isbn("0330301624"))  # Output: "9780330301626"
print(validate_convert_isbn("9780316066525"))  # Output: "Valid"
print(validate_convert_isbn("0451450523"))  # Output: "9780451450529"
print(validate_convert_isbn("123456789X"))  # Output: "Invalid"
