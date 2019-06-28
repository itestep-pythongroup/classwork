#!/usr/bin/python3.7
from main import *
from tools import TestBase

class TestLesson(TestBase):
    
    def test_print_hello(self):
        self.iotester(print_hello,[],"hello world")

    def test_yes_or_no(self):
        self.iotester(print_yes_or_no,["y"],"yes")
        self.iotester(print_yes_or_no,["n"],"no")
        self.iotester(print_yes_or_no,[""],"------")
    
        
if __name__ == '__main__':
    TestBase.runner()
