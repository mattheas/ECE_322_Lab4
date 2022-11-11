import unittest
from modules.ModuleC import ModuleC
from data.Entry import Entry
from unittest.mock import Mock

# As told in the lab manual no need to test getters/ setters, focus on the main methods, although these would normally be tested


class TestC(unittest.TestCase):

    def test_sortData_method(self):
        # create lists of unsorted and sorted Entry obj's
        test_name = "zan"
        test_name1 = "abc"
        test_name2 = "bgf"
        test_num = "123456"
        test_num1 = "234098"
        test_num2 = "42439"
        unsorted_data_list = [Entry(test_name,test_num), Entry(test_name1,test_num1), Entry(test_name2,test_num2)]
        sorted_data_list = [Entry(test_name1,test_num1), Entry(test_name2,test_num2), Entry(test_name,test_num)]
    	
        # create instance of Module c w/ mock Mod. F obj
        mock_ModuleF = Mock()
        test_ModuleC = ModuleC(mock_ModuleF)

        self.assertEqual(test_ModuleC.sortData(unsorted_data_list)[0].name, sorted_data_list[0].name)
        self.assertEqual(test_ModuleC.sortData(unsorted_data_list)[1].name, sorted_data_list[1].name)
        self.assertEqual(test_ModuleC.sortData(unsorted_data_list)[2].name, sorted_data_list[2].name)
        
        
if __name__ == '__main__':
    unittest.main()
    
