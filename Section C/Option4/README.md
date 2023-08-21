
# ISBN Validation and Conversion Script

This Python script provides a function to validate and convert International Standard Book Numbers (ISBNs). ISBNs can be either ISBN-10 (10-digit) or ISBN-13 (13-digit). The script implements the validation rules for both ISBN types and can also convert valid ISBN-10s to ISBN-13s.

# Function Description
The script contains two main components:

# ISBN Validation and Conversion Function (validate_and_convert_isbn):

This function takes an input string representing an ISBN (with possible hyphens or 'X' at the end for ISBN-10) and performs the following tasks:

* Validates whether the input is a valid ISBN-10 or ISBN-13.
If the input is a valid ISBN-10, it converts it to an ISBN-13 by adding '978' to the start and adjusting the check digit for ISBN-13 validation.
* Returns the result as:
   *"Invalid" if the input is not a valid ISBN-10 or ISBN-13.
   *"Valid" if the input is a valid ISBN-13.
   *The converted ISBN-13 if the input is a valid ISBN-10.

# Test Cases (run_tests Function):

The script includes a set of test cases to validate the correctness of the ISBN validation and conversion function. These test cases cover various scenarios, including ISBN-10 to ISBN-13 conversion, valid ISBN-13 validation, invalid ISBNs, and ISBNs not divisible by 11 or 10.

# Usage
Clone or Download the Repository:

Clone or download the repository containing the script to your local machine.

# Running the Script:

Windows:

* Install Python if not already installed.
* Open Command Prompt (CMD).
* Navigate to the directory where the script is located. cd Option4
* Run: python isbn_validation_conversion.py.

macOS and Linux:

* Python is usually pre-installed.
* Open the terminal.
* Navigate to the script directory. cd Option4
* Run: python3 isbn_validation_conversion.py.
This will execute the script and display the test results, indicating whether the tests passed or failed.

# Interpreting the Results:

Each test case's input, expected result, and actual result will be displayed in the terminal. If the actual result matches the expected result, the test passes; otherwise, it will raise an assertion error.

# Customization
You can modify or add your own test cases to ensure the function works as expected in various scenarios.

# Credits
Script created by [Zaibonisha].

