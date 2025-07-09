#!/usr/bin/env python3
"""
Example usage of the Age Calculator as a Python module
"""

from age_calculator import AgeCalculator
import datetime

def main():
    """Demonstrate programmatic usage of AgeCalculator"""
    
    print("Age Calculator - Programmatic Usage Example")
    print("=" * 50)
    
    # Create calculator instance
    calculator = AgeCalculator()
    
    # Example birth dates to demonstrate
    example_dates = [
        "2000-01-15",
        "1990-06-25",
        "1985-12-03",
        "2010-03-20",
        "January 1, 1995"
    ]
    
    print(f"Today's date: {calculator.today.strftime('%B %d, %Y')}")
    print()
    
    for date_str in example_dates:
        print(f"Analyzing birth date: {date_str}")
        print("-" * 40)
        
        # Parse the date
        birth_date = calculator.parse_date(date_str)
        
        if birth_date:
            try:
                # Calculate age
                years, months, days = calculator.calculate_age(birth_date)
                age_string = calculator.get_age_string(years, months, days)
                total_days = calculator.calculate_total_days(birth_date)
                next_birthday, days_to_birthday = calculator.get_next_birthday(birth_date)
                
                # Display results
                print(f"  Parsed date: {birth_date}")
                print(f"  Age: {age_string}")
                print(f"  Total days lived: {total_days:,}")
                print(f"  Next birthday: {next_birthday.strftime('%B %d, %Y')}")
                print(f"  Days to next birthday: {days_to_birthday}")
                
            except ValueError as e:
                print(f"  Error: {e}")
        else:
            print(f"  Error: Could not parse date '{date_str}'")
        
        print()
    
    # Demonstrate error handling
    print("Error Handling Examples:")
    print("-" * 40)
    
    # Invalid date format
    invalid_date = calculator.parse_date("invalid-date")
    print(f"Invalid date 'invalid-date': {invalid_date}")
    
    # Future date
    try:
        future_date = datetime.date(2030, 1, 1)
        calculator.calculate_age(future_date)
    except ValueError as e:
        print(f"Future date error: {e}")
    
    print()
    print("Demo completed successfully!")

if __name__ == "__main__":
    main()