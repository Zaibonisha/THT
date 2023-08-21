def number_to_text(numeral):
    ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    large_units = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    number = int(numeral)

    if number == 0:
        return ones[0]

    text_parts = []
    groups = []
    while number > 0:
        groups.append(number % 1000)
        number //= 1000

    for i, group in enumerate(reversed(groups)):
        if group == 0:
            continue

        hundreds_digit = group // 100
        tens_digit = (group % 100) // 10
        ones_digit = group % 10

        if hundreds_digit > 0:
            text_parts.append(ones[hundreds_digit] + ' Hundred')
            if tens_digit > 0 or ones_digit > 0:
                text_parts.append('and')

        if tens_digit == 1:
            text_parts.append(ones[group % 100])
        else:
            if tens_digit > 0:
                text_parts.append(tens[tens_digit])
                if ones_digit > 0:
                    text_parts.append('-')
            if ones_digit > 0 and tens_digit != 1:  # Avoid hyphen for teens (e.g., "Twenty-One" not "Twenty-One-")
                text_parts.append(ones[ones_digit])

        if i > 0 and group > 0:
            text_parts.append(large_units[i])

    return ' '.join(text_parts)

import inflect

def number_to_text(numeral):
    p = inflect.engine()
    return p.number_to_words(numeral)

def test_number_to_text():
    test_cases = [
        ('0', 'Zero'),
        ('1', 'One'),
        ('10', 'Ten'),
        ('11', 'Eleven'),
        ('19', 'Nineteen'),
        ('20', 'Twenty'),
        ('21', 'Twenty-One'),
        ('99', 'Ninety-Nine'),
        ('100', 'One Hundred'),
        ('101', 'One Hundred and One'),
        ('999', 'Nine Hundred and Ninety-Nine'),
        ('1000', 'One Thousand'),
        ('1001', 'One Thousand and One'),
        ('9999', 'Nine Thousand, Nine Hundred and Ninety-Nine'),
        ('10000', 'Ten Thousand'),
        ('19093', 'Nineteen Thousand and Ninety-Three'),
        ('1000000', 'One Million'),
        ('1000001', 'One Million and One'),
        ('123456789', 'One Hundred and Twenty-Three Million, Four Hundred and Fifty-Six Thousand, Seven Hundred and Eighty-Nine'),
    ]

    for numeral, expected in test_cases:
        result = number_to_text(numeral)
        assert result.lower() == expected.lower(), f"Error: For input {numeral}, expected '{expected}', but got '{result}'"

    print("All test cases passed!")

# Run the test suite
test_number_to_text()
