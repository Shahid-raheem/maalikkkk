# Age Calculator Software

A comprehensive and user-friendly age calculator that computes your exact age in years, months, and days. This Python-based tool supports multiple date formats and provides detailed age information including total days lived and days until next birthday.

## Features

- **Multiple Date Formats**: Supports various input formats including:
  - `YYYY-MM-DD` (e.g., 2000-01-15)
  - `DD-MM-YYYY` (e.g., 15-01-2000)
  - `MM/DD/YYYY` (e.g., 01/15/2000)
  - `DD/MM/YYYY` (e.g., 15/01/2000)
  - `Month DD, YYYY` (e.g., January 15, 2000)
  - `DD Month YYYY` (e.g., 15 January 2000)

- **Comprehensive Age Information**:
  - Exact age in years, months, and days
  - Total days lived
  - Next birthday date
  - Days remaining until next birthday

- **Error Handling**: Robust input validation and error messages
- **Interactive Interface**: User-friendly command-line interface
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Usage

### Running the Age Calculator

```bash
python3 age_calculator.py
```

### Interactive Mode

The program will prompt you to enter your birth date in any of the supported formats:

```
==================================================
        AGE CALCULATOR SOFTWARE
==================================================

Please enter your birth date in one of these formats:
  • YYYY-MM-DD (e.g., 2000-01-15)
  • DD-MM-YYYY (e.g., 15-01-2000)
  • MM/DD/YYYY (e.g., 01/15/2000)
  • DD/MM/YYYY (e.g., 15/01/2000)
  • Month DD, YYYY (e.g., January 15, 2000)
  • DD Month YYYY (e.g., 15 January 2000)

Enter your birth date (or 'quit' to exit): 
```

### Example Output

```
--------------------------------------------------
AGE CALCULATION RESULTS
--------------------------------------------------
Birth Date: January 15, 2000
Today's Date: July 9, 2024

Your Age: 24 years, 5 months, 24 days
Total Days Lived: 8,941 days
Next Birthday: January 15, 2025
Days to Next Birthday: 190 days
--------------------------------------------------
```

### Using as a Python Module

You can also import and use the AgeCalculator class in your own Python programs:

```python
from age_calculator import AgeCalculator
import datetime

# Create calculator instance
calculator = AgeCalculator()

# Parse a date string
birth_date = calculator.parse_date("2000-01-15")

# Calculate age
years, months, days = calculator.calculate_age(birth_date)

# Get formatted age string
age_string = calculator.get_age_string(years, months, days)
print(f"Age: {age_string}")

# Get total days lived
total_days = calculator.calculate_total_days(birth_date)
print(f"Total days lived: {total_days:,}")

# Get next birthday info
next_birthday, days_remaining = calculator.get_next_birthday(birth_date)
print(f"Next birthday: {next_birthday}, Days remaining: {days_remaining}")
```

## Running Tests

To run the test suite:

```bash
python3 test_age_calculator.py
```

## File Structure

- `age_calculator.py` - Main age calculator program
- `test_age_calculator.py` - Comprehensive test suite
- `README.md` - This documentation file

## License

This software is provided as-is for educational and personal use.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the age calculator.