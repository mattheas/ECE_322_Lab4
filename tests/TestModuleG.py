import unittest
from modules.ModuleG import ModuleG
from unittest.mock import patch
from data.Entry import Entry


### change code
#  has no stubs, i.e no objects to mock
# the "driver" is basically the unit test

# no need to test FileNotFOundError in Module G OR B
# filename is a string,... data.txt used in Mainprogram.py
# data is an entry obj with name and number


class TestF(unittest.TestCase):
    
    def test_updateData_method(self):
        print("mock update data test")
    	
        test_filename = "test_write.txt"
        test_name = "name"
        test_name1 = "name1"
        test_num = "123456"
        test_num1 = "234098"
        data_list = [Entry(test_name,test_num), Entry(test_name1,test_num1)]

        # call updateData method
        ModuleG.updateData(self,test_filename, data_list)

        # assertion calls to check data is written to .txt file
        count = 0
        with open(test_filename) as fp:
            Lines = fp.readlines()
            first_line = True
            for line in Lines:
                count += 1
                values=line.strip().split(",")
                if (first_line):
                    first_line=False
                    self.assertEqual(values[0], test_name)
                    self.assertEqual(values[1], test_num)		
                else:
                    self.assertEqual(values[0], test_name1)
                    self.assertEqual(values[1], test_num1)
      
if __name__ == '__main__':
    unittest.main()
