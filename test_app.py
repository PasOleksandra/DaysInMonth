import unittest
from eks import get_days_in_month

class TestDaysInMonth(unittest.TestCase):
    def test_valid_months(self):
        self.assertEqual(get_days_in_month("January"), 31)
        self.assertEqual(get_days_in_month("February"), 28)
        self.assertEqual(get_days_in_month("March"), 31)
        self.assertEqual(get_days_in_month("April"), 30)
        self.assertEqual(get_days_in_month("May"), 31)
        self.assertEqual(get_days_in_month("June"), 30)
        self.assertEqual(get_days_in_month("July"), 31)
        self.assertEqual(get_days_in_month("August"), 31)
        self.assertEqual(get_days_in_month("September"), 30)
        self.assertEqual(get_days_in_month("October"), 31)
        self.assertEqual(get_days_in_month("November"), 30)
        self.assertEqual(get_days_in_month("December"), 31)

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            get_days_in_month("InvalidMonth")

    def test_case_insensitivity(self):
        self.assertEqual(get_days_in_month("january"), 31)
        self.assertEqual(get_days_in_month("FEBRUARY"), 28)
        self.assertEqual(get_days_in_month("MaRcH"), 31)

if __name__ == "__main__":
    unittest.main()
