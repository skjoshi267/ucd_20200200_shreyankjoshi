from datetime import datetime
import unittest
from stock_database import stock_data

class Test_Stock_Search(unittest.TestCase):
    def test_validate_period_pos(self):
        date_val = stock_data.validate_period("2020-01-01")
        self.assertEqual(date_val,datetime.strptime("2020-01-01","%Y-%m-%d").date())
    
    def test_validate_period_neg(self):
        date_val = stock_data.validate_period("This is a failed test")
        self.assertEqual(date_val,"")

if __name__ == "__main__":
    unittest.main()
