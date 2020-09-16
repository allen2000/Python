import unittest
from unittest import runner
import HTMLReport

# 被测试类
class myclass(object):
    @classmethod
    def add(self, a, b):
        return a + b #将两个传入参数进行相加操作
    @classmethod
    def sub(self, a, b):
        return a - b #将两个传入参数进行相减操作
    @classmethod
    def mul(self, a, b):
        return a * b #将两个传入参数进行相乘操作
    @classmethod
    def div(self, a, b):
        return a / b #将两个传入参数进行相除操作

class TestAddSubFunctions(unittest.TestCase):
    def setUp(self):
        self.c=myclass()
        print ("setup completed!")
    #@unittest.skip("skipping")
    def test_0add(self):
        a,b,except_result=30,40,70
        self.assertEqual(self.c.add(a,b),except_result,'断言失败，%s + %s != %s' %(a, b, except_result))
        #self.assertTrue(self.c.add(30,40)==70)
    def test_1sub(self):
        self.assertTrue(self.c.sub(100,30)==70)
    def tearDown(self):
        print ("test completed!") 
    def tearDown(self):
        print ("tearDown completed")

class TestMulDivFunctions(unittest.TestCase):
    def setUp(self):
        self.c=myclass()
        print ("setup completed!")
    #@unittest.skip("skipping")
    def test_2mul(self):
        a,b,except_result=5,14,71
        self.assertTrue(self.c.mul(a,b)==except_result,'断言失败，%s * %s != %s' %(a, b, except_result))
    def test_3div(self):
        self.assertTrue(self.c.div(350,5)==70)
    def tearDown(self):
        print ("test completed!") 
    def tearDown(self):
        print ("tearDown completed")

if __name__ == '__main__':
    #unittest.main()  
    # 根据给定的测试类，获取其中所有以“test”开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestAddSubFunctions)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestMulDivFunctions)
    # 将多个测试类加载到测试套件中
    #通过调整suit2和suite1的顺序，可以设定执行顺序
    suite = unittest.TestSuite([suite2, suite1])      
    # 设置verbosity = 2，可以打印出更详细的执行信息
    runner = HTMLReport.TestRunner(
        report_file_name='Calc_Testing',
        output_path='report',
        description='用于验证四则运算的正确性',
        #thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
        #thread_start_wait=3,  # 各线程启动延迟，默认 0 s
        sequential_execution=False,
        lang='cn'
    )
    runner.run(suite)
    #unittest.TextTestRunner(verbosity = 2).run(suite)
