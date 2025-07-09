#!/usr/bin/env python3
"""
Age Calculator Software
A simple and user-friendly age calculator that computes age in years, months, and days.
"""

import datetime
import sys
from typing import Tuple, Optional

class AgeCalculator:
    """A class to calculate age based on birth date."""
    
    def __init__(self):
        self.today = datetime.date.today()
    
    def parse_date(self, date_string: str) -> Optional[datetime.date]:
        """
        Parse date string in various formats.
        
        Args:
            date_string: Date string in various formats
            
        Returns:
            datetime.date object or None if parsing fails
        """
        # Common date formats to try
        formats = [
            "%Y-%m-%d",      # 2000-01-15
            "%d-%m-%Y",      # 15-01-2000
            "%m/%d/%Y",      # 01/15/2000
            "%d/%m/%Y",      # 15/01/2000
            "%Y.%m.%d",      # 2000.01.15
            "%d.%m.%Y",      # 15.01.2000
            "%B %d, %Y",     # January 15, 2000
            "%d %B %Y",      # 15 January 2000
            "%Y-%m-%d",      # 2000-1-15 (single digit month/day)
        ]
        
        for fmt in formats:
            try:
                return datetime.datetime.strptime(date_string.strip(), fmt).date()
            except ValueError:
                continue
        
        return None
    
    def calculate_age(self, birth_date: datetime.date) -> Tuple[int, int, int]:
        """
        Calculate age in years, months, and days.
        
        Args:
            birth_date: Birth date as datetime.date object
            
        Returns:
            Tuple of (years, months, days)
        """
        if birth_date > self.today:
            raise ValueError("Birth date cannot be in the future")
        
        # Calculate years
        years = self.today.year - birth_date.year
        
        # Calculate months
        months = self.today.month - birth_date.month
        
        # Calculate days
        days = self.today.day - birth_date.day
        
        # Adjust for negative days
        if days < 0:
            # Go back one month
            months -= 1
            # Calculate days in previous month
            if self.today.month == 1:
                prev_month = 12
                prev_year = self.today.year - 1
            else:
                prev_month = self.today.month - 1
                prev_year = self.today.year
            
            # Get last day of previous month
            last_day_prev_month = datetime.date(prev_year, prev_month + 1, 1) - datetime.timedelta(days=1)
            days = last_day_prev_month.day + days
        
        # Adjust for negative months
        if months < 0:
            years -= 1
            months += 12
        
        return years, months, days
    
    def get_age_string(self, years: int, months: int, days: int) -> str:
        """
        Format age as a readable string.
        
        Args:
            years: Number of years
            months: Number of months
            days: Number of days
            
        Returns:
            Formatted age string
        """
        parts = []
        
        if years > 0:
            parts.append(f"{years} year{'s' if years != 1 else ''}")
        
        if months > 0:
            parts.append(f"{months} month{'s' if months != 1 else ''}")
        
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        
        if not parts:
            return "Born today!"
        
        return ", ".join(parts)
    
    def calculate_total_days(self, birth_date: datetime.date) -> int:
        """
        Calculate total days lived.
        
        Args:
            birth_date: Birth date as datetime.date object
            
        Returns:
            Total number of days lived
        """
        return (self.today - birth_date).days
    
    def get_next_birthday(self, birth_date: datetime.date) -> Tuple[datetime.date, int]:
        """
        Get next birthday date and days remaining.
        
        Args:
            birth_date: Birth date as datetime.date object
            
        Returns:
            Tuple of (next_birthday_date, days_remaining)
        """
        this_year_birthday = birth_date.replace(year=self.today.year)
        
        if this_year_birthday >= self.today:
            next_birthday = this_year_birthday
        else:
            next_birthday = birth_date.replace(year=self.today.year + 1)
        
        days_remaining = (next_birthday - self.today).days
        return next_birthday, days_remaining

def main():
    """Main function to run the age calculator."""
    print("=" * 50)
    print("        AGE CALCULATOR SOFTWARE")
    print("=" * 50)
    print()
    
    calculator = AgeCalculator()
    
    while True:
        print("Please enter your birth date in one of these formats:")
        print("  • YYYY-MM-DD (e.g., 2000-01-15)")
        print("  • DD-MM-YYYY (e.g., 15-01-2000)")
        print("  • MM/DD/YYYY (e.g., 01/15/2000)")
        print("  • DD/MM/YYYY (e.g., 15/01/2000)")
        print("  • Month DD, YYYY (e.g., January 15, 2000)")
        print("  • DD Month YYYY (e.g., 15 January 2000)")
        print()
        
        date_input = input("Enter your birth date (or 'quit' to exit): ").strip()
        
        if date_input.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using Age Calculator!")
            break
        
        if not date_input:
            print("Error: Please enter a valid date.")
            print()
            continue
        
        # Parse the date
        birth_date = calculator.parse_date(date_input)
        
        if birth_date is None:
            print("Error: Could not parse the date. Please check the format and try again.")
            print()
            continue
        
        try:
            # Calculate age
            years, months, days = calculator.calculate_age(birth_date)
            total_days = calculator.calculate_total_days(birth_date)
            next_birthday, days_to_birthday = calculator.get_next_birthday(birth_date)
            
            # Display results
            print()
            print("-" * 50)
            print("AGE CALCULATION RESULTS")
            print("-" * 50)
            print(f"Birth Date: {birth_date.strftime('%B %d, %Y')}")
            print(f"Today's Date: {calculator.today.strftime('%B %d, %Y')}")
            print()
            print(f"Your Age: {calculator.get_age_string(years, months, days)}")
            print(f"Total Days Lived: {total_days:,} days")
            print(f"Next Birthday: {next_birthday.strftime('%B %d, %Y')}")
            print(f"Days to Next Birthday: {days_to_birthday} days")
            print("-" * 50)
            print()
            
        except ValueError as e:
            print(f"Error: {e}")
            print()
        
        # Ask if user wants to calculate another age
        another = input("Would you like to calculate another age? (y/n): ").strip().lower()
        if another not in ['y', 'yes']:
            print("Thank you for using Age Calculator!")
            break
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThank you for using Age Calculator!")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)