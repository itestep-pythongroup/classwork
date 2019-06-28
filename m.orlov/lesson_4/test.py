#!/usr/bin/python3.7
from main import *
from tools import TestBase

class TestLesson(TestBase):
    
    def test_print_hello(self):
        self.iotester(print_hello,[],"hello worl")
        
if __name__ == '__main__':
    TestBase.runner()
