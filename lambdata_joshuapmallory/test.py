import unittest
import numpy as np
from utility_functions import google_drive_useable


class function_tester(unittest.TestCase):
    '''Obligatory docstring, test square root functions!'''
    
    def test_google_drive_useable(self):
        '''docstring'''
        self.assertEqual(google_drive_useable('https://drive.google.com/open?id=1pEOgqOZcgxwu7gA4GnFuMwO_wVBLQ7cf')
                        ,'https://drive.google.com/uc?id=1pEOgqOZcgxwu7gA4GnFuMwO_wVBLQ7cf'
                        )

    
if __name__ == '__main__':
    unittest.main()