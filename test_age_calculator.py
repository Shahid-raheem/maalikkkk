#!/usr/bin/env python3
"""
Test script for Age Calculator Software
"""

import datetime
import unittest
from age_calculator import AgeCalculator

class TestAgeCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = AgeCalculator()
    
    def test_date_parsing(self):
        """Test various date format parsing"""
        test_cases = [
            ('2000-01-15', datetime.date(2000, 1, 15)),
            ('15-01-2000', datetime.date(2000, 1, 15)),
            ('01/15/2000', datetime.date(2000, 1, 15)),
            ('15/01/2000', datetime.date(2000, 1, 15)),
            ('January 15, 2000', datetime.date(2000, 1, 15)),
            ('15 January 2000', datetime.date(2000, 1, 15)),
        ]
        
        for date_str, expected in test_cases:
            with self.subTest(date_str=date_str):
                result = self.calculator.parse_date(date_str)
                self.assertEqual(result, expected)
    
    def test_invalid_date_parsing(self):
        """Test invalid date format parsing"""
        invalid_dates = [
            'invalid-date',
            '2000-13-40',  # Invalid month and day
            '32/12/2000',  # Invalid day
            '',  # Empty string
            '2000',  # Year only
        ]
        
        for date_str in invalid_dates:
            with self.subTest(date_str=date_str):
                result = self.calculator.parse_date(date_str)
                self.assertIsNone(result)
    
    def test_age_calculation(self):
        """Test age calculation accuracy"""
        # Mock today's date for consistent testing
        original_today = self.calculator.today
        self.calculator.today = datetime.date(2024, 7, 9)
        
        # Test case: Born on 2000-01-15
        birth_date = datetime.date(2000, 1, 15)
        years, months, days = self.calculator.calculate_age(birth_date)
        
        # Should be 24 years, 5 months, 24 days on 2024-07-09
        self.assertEqual(years, 24)
        self.assertEqual(months, 5)
        self.assertEqual(days, 24)
        
        # Restore original date
        self.calculator.today = original_today
    
    def test_future_date_error(self):
        """Test that future dates raise ValueError"""
        future_date = datetime.date(2030, 1, 1)
        with self.assertRaises(ValueError):
            self.calculator.calculate_age(future_date)
    
    def test_age_string_formatting(self):
        """Test age string formatting"""
        test_cases = [
            (0, 0, 0, "Born today!"),
            (1, 0, 0, "1 year"),
            (2, 0, 0, "2 years"),
            (1, 1, 0, "1 year, 1 month"),
            (2, 2, 0, "2 years, 2 months"),
            (1, 1, 1, "1 year, 1 month, 1 day"),
            (2, 2, 2, "2 years, 2 months, 2 days"),
            (0, 1, 0, "1 month"),
            (0, 0, 1, "1 day"),
            (0, 2, 5, "2 months, 5 days"),
        ]
        
        for years, months, days, expected in test_cases:
            with self.subTest(years=years, months=months, days=days):
                result = self.calculator.get_age_string(years, months, days)
                self.assertEqual(result, expected)
    
    def test_total_days_calculation(self):
        """Test total days calculation"""
        # Mock today's date
        original_today = self.calculator.today
        self.calculator.today = datetime.date(2024, 7, 9)
        
        birth_date = datetime.date(2024, 7, 8)  # Yesterday
        total_days = self.calculator.calculate_total_days(birth_date)
        self.assertEqual(total_days, 1)
        
        birth_date = datetime.date(2024, 7, 9)  # Today
        total_days = self.calculator.calculate_total_days(birth_date)
        self.assertEqual(total_days, 0)
        
        # Restore original date
        self.calculator.today = original_today
    
    def test_next_birthday_calculation(self):
        """Test next birthday calculation"""
        # Mock today's date
        original_today = self.calculator.today
        self.calculator.today = datetime.date(2024, 7, 9)
        
        # Birthday hasn't happened this year
        birth_date = datetime.date(2000, 12, 25)
        next_birthday, days_remaining = self.calculator.get_next_birthday(birth_date)
        expected_next = datetime.date(2024, 12, 25)
        self.assertEqual(next_birthday, expected_next)
        self.assertEqual(days_remaining, 169)  # Days from July 9 to Dec 25
        
        # Birthday already happened this year
        birth_date = datetime.date(2000, 1, 15)
        next_birthday, days_remaining = self.calculator.get_next_birthday(birth_date)
        expected_next = datetime.date(2025, 1, 15)
        self.assertEqual(next_birthday, expected_next)
        
        # Restore original date
        self.calculator.today = original_today

if __name__ == '__main__':
    unittest.main()