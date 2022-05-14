import unittest
from dateUtil import Datetime
import pytz

class TestDateUtil(unittest.TestCase):

    def test_convert_utc_milis_jakarta_timezone(self):
        # When
        result = Datetime.convert_from_utc_milis_to_local_timezone(utc_milis=1652345652000,timezone=pytz.timezone('Asia/Jakarta'))

        # Expect
        output = '12.05.2022 15:54:12'
        self.assertEqual(result, output)

    def test_jakarta_timezone_to_utc_milis(self):
        # when
        result = Datetime.convert_local_timezone_to_utc_milis(localtime='12.05.2022 15:54:12') 
        
        # Expect
        output = 1652345652000
        
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()