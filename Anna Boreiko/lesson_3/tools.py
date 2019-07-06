#!/usr/bin/python3.7

import unittest

class TestBase(unittest.TestCase):
    
    def printer(self):
        res = []
        def print(*args,**kwargs):
            res.append(" ".join([str(i) for i in args]))
            
        def out():
            return "\n".join(res)
        
        return print,out
        
    def inputer(self,seq=[]):
        cp = seq[::]
        cp.reverse()
        def input(*args):
            if cp:
              return str(cp.pop())
            return ""
        return input
    
    def iotester(self,testfn,expected_input,expected_print,*args):
        print,print_out = self.printer()
        testfn(print,self.inputer(expected_input),*args)
        self.assertEqual(print_out(),expected_print.strip())
        
    @staticmethod    
    def runner():
        unittest.main()
        
