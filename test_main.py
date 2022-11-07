import unittest
from main import product
class test_main(unittest.TestCase):

    # testing our product function
    def test_product(self):
        
        # This array has the daily return fake data similar to our excel sheet
        inArr=[1.01,1.02,1.03]

        # this array has expected values for the total returns after manual/excel calculations
        expectedArr=[1.00,3.02,6.11]

        # This array will hold values that our product function returns
        outArr=[]
        for i in range(1, len(inArr)+1):
            j = round(product(i,inArr),2)
            outArr.append(j)
        
        # Here we make an assertion to see if our test passed
        self.assertEqual(outArr, expectedArr)
        
        # When we run this test file, first our graph will open and after closing that window, our terminal will have the results of our unit tests

if __name__ == '__main__':
    unittest.main()