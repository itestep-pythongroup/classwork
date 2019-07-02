#!/usr/bin/python3.7
from main import *
from tools import TestBase

class TestLesson(TestBase):
    
    def test_make_check_is_isd(self):
        self.iotester(make_check,["y"],"""

Beef__________ ( 1.3 ) 1.9259259259259258
Chicken_______ ( 2.3 ) 4.77037037037037
Tomatoes______ ( 3.7 ) 8.51
Avocado_______ ( 5.0 ) 4.0740740740740735
Tax___________ ( 20% ) 3.8560740740740735
Total+Tax_____         23.13644444444444

        """)
    def test_make_check_not_is_usd(self):

        self.iotester(make_check,["n"],"""

Beef__________ ( 1.3 ) 52.0
Chicken_______ ( 2.3 ) 128.79999999999998
Tomatoes______ ( 3.7 ) 8.51
Avocado_______ ( 5.0 ) 110.0
Tax___________ ( 20% ) 59.861999999999995
Total+Tax_____         359.1719999999999


        """)        
        
if __name__ == '__main__':
    TestBase.runner()
