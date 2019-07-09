#!/usr/bin/python3.7
from main import *
from tools import TestBase

class TestLesson(TestBase):
    
    def a(self,a,b):
        self.assertEqual(a,b)
        
    def test_print_hello(self):
        self.iotester(print_hello,[],"привет")
        
    def test_print_sum(self):
        self.iotester(print_sum,[],"5")

    def test_print_pivot(self):
        self.iotester(print_pivot,[],"False",10)
        self.iotester(print_pivot,[],"True",20)
<<<<<<< Updated upstream
        
    def test_type_dispatch(self):
        self.iotester(type_dispatch,[],"number",10)
        self.iotester(type_dispatch,[],"float_number",10.10)
        self.iotester(type_dispatch,[],"string","hello")
        
    def test_ifelse_coordinates(self):
        self.iotester(type_dispatch,["1","1"],"I")
        self.iotester(type_dispatch,["1","0"],"undefined")
        self.iotester(type_dispatch,["1","-1"],"IV")
        self.iotester(type_dispatch,["0","0"],"undefined")
        self.iotester(type_dispatch,["0","1"],"undefined")
        self.iotester(type_dispatch,["-1","-1"],"III")
        self.iotester(type_dispatch,["-1","1"],"II")
        
    def test_ifelse_small_game(self):
        self.iotester(ifelse_small_game,["m"],"3")
        self.iotester(ifelse_small_game,["y","m"],"5")
        self.iotester(ifelse_small_game,["y","y"],"6")
        self.iotester(ifelse_small_game,["n","m"],"1")
        self.iotester(ifelse_small_game,["n","n"],"0")
        self.iotester(ifelse_small_game,["n","y"],"2")
        self.iotester(ifelse_small_game,["n","y"],"2")
=======
>>>>>>> Stashed changes

    def test_print_pivot_1(self):
        self.iotester(print_pivot_1,[],"True",19)
        self.iotester(print_pivot_1,[],"True",26)
        self.iotester(print_pivot_1,[],"False",3)
        self.iotester(print_pivot_1,[],"False",12)
        self.iotester(print_pivot_1,[],"False",17)
        self.iotester(print_pivot_1,[],"False",29)
        
    def test_print_pivot_2(self):
        self.iotester(print_pivot_2,[],"True",8)
        self.iotester(print_pivot_2,[],"True",4)
        self.iotester(print_pivot_2,[],"True",10)
        self.iotester(print_pivot_2,[],"True",19)
        self.iotester(print_pivot_2,[],"True",26)
        self.iotester(print_pivot_2,[],"False",3)
        self.iotester(print_pivot_2,[],"False",12)
        self.iotester(print_pivot_2,[],"False",17)
        self.iotester(print_pivot_2,[],"False",29)
        
    def test_print_roman(self):
        self.iotester(print_roman,[],"I",1)
        self.iotester(print_roman,[],"II",2)
        self.iotester(print_roman,[],"III",3)
        self.iotester(print_roman,[],"~",4)
        self.iotester(print_roman,[],"~",0)
        
    def print_type_convert_1(self):
        self.iotester(print_type_convert_1,["123"],"133",10)
        self.iotester(print_type_convert_1,["-10"],"0",10)
        
    def print_type_convert_3(self):
        self.iotester(print_type_convert_1,[],"137","4","133")
        self.iotester(print_type_convert_1,[],"28","10","18")

    def print_type_convert_2(self):
        self.iotester(print_type_convert_2,[],"1334",133,4)
        self.iotester(print_type_convert_2,[],"100",10,0)
        self.iotester(print_type_convert_2,[],"10-10",10,-10)

    def test_return_sum(self):
        self.a(return_sum(),7)
        
    def test_return_sum_1(self):
        self.a(return_sum_1(9),9)
        self.a(return_sum_1(5),5)
        
    def test_return_sum_2(self):
        self.a(return_sum_2(9,1),10)
        self.a(return_sum_2(3,2),5)

    def test_return_sum_3(self):
        self.a(return_sum_3(1)(9,1),10)
        self.a(return_sum_3(1)(3,2),5)
        self.a(return_sum_3(0)(9,1),8)
        self.a(return_sum_3(0)(3,2),1)
<<<<<<< Updated upstream

    def test_iterate_1(self):
        self.iotester(iterate_1,[],"1\n2\n3\n4\n5")

    def test_iterate_2(self):
        self.iotester(iterate_1,["","","yes"],"3\n3\n4")
        
    def test_iterate_3(self):
        self.iotester(iterate_1,[],"*\n**\n***",3)
        
    def test_iterate_4(self):
        self.iotester(iterate_1,[],"""
   *
  ***
 ******
********
        """,4)
        
    def test_iterate_5(self):
        self.iotester(iterate_5,[],"-5 -12 -14")
        
    def test_vector_1(self):
        self.a(vector_1(),[1,2,3])
        
    def test_vector_2(self):
        self.a(len(vector_2(200)),200)

    def test_vector_3(self):
        self.a(len(vector_2(200,19)),200)
        self.a(len(vector_2(200,19)[0]),19)
        
    def test_vector_4(self):
        self.a(vector_4("(())"),True)
        self.a(vector_4("()()()"),True)
        self.a(vector_4("(()(()()))"),True)
        self.a(vector_4("())"),False)
        self.a(vector_4("()()("),False)
        self.a(vector_4("(()((()))"),False)
        
    def test_vector_5(self):
        self.a(vector_4("(())"),True)
        self.a(vector_4("()()()"),True)
        self.a(vector_4("(()(()()))"),True)
        self.a(vector_4("())"),False)
        self.a(vector_4("()()("),False)
        self.a(vector_4("(()((()))"),False)
=======
>>>>>>> Stashed changes
        
if __name__ == '__main__':
    TestBase.runner()
