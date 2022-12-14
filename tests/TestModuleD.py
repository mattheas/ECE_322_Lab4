import unittest
from modules.ModuleD import ModuleD
from unittest.mock import Mock
from data.Entry import Entry


# As told in the lab manual no need to test getters/ setters, focus on the main methods, although these would normally be tested. Also
# as a note the the deleteData method in ModuleD permanently deletes the element in memory, so re-initialization of data list must be 
# performed between assert() calls


class TestD(unittest.TestCase):

    def test_insertData_method(self):
        # create instance of Module D w/ mock Mod. F & Gobj
        mock_ModuleF = Mock()
        mock_ModuleG = Mock()
        test_ModuleD = ModuleD(mock_ModuleF, mock_ModuleG)
        
        # test data
        test_name = "Bob"
        test_number = "135849"
        test_filename = "test_insertData.txt"
        test_data = []
        
        # assertions that call method to insert data
        self.assertEqual(test_ModuleD.insertData(test_data, test_name, test_number, test_filename)[0].name, test_name)
        self.assertEqual(test_ModuleD.insertData(test_data, test_name, test_number, test_filename)[0].number, test_number)
        
        
    def test_updateData_method(self):
        # create instance of Module D w/ mock Mod. F & Gobj
        mock_ModuleF = Mock()
        mock_ModuleG = Mock()
        test_ModuleD = ModuleD(mock_ModuleF, mock_ModuleG)
        
        # populate test data array
        test_name = "danny"
        test_name1 = "sammy"
        test_name2 = "flammy"
        test_num = "437892"
        test_num1 = "789234"
        test_num2 = "761237"
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1), Entry(test_name2,test_num2)]
        
        test_filename = "test_updateData.txt"
        update_index = 0
        test_update_name = "notDanny"
        test_update_number = "84921"
        
        # assertions that call method to update data
        self.assertEqual(test_ModuleD.updateData(test_data, update_index, test_update_name, test_update_number, test_filename)[update_index].name, test_update_name)
        self.assertEqual(test_ModuleD.updateData(test_data, update_index, test_update_name, test_update_number, test_filename)[update_index].number, test_update_number)
                
                 
    def test_deleteData_method(self):
        # create instance of Module D w/ mock Mod. F & Gobj
        mock_ModuleF = Mock()
        mock_ModuleG = Mock()
        test_ModuleD = ModuleD(mock_ModuleF, mock_ModuleG)
        
        # populate test data array
        test_name = "danny"
        test_name1 = "sammy"
        test_num = "437892"
        test_num1 = "789234"
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        
        test_filename = "test_deleteData.txt"
        delete_index = 1
        
        # assert length of list before data is deleted
        self.assertEqual(len(test_data), 2)
        
        # assert length of new list with element deleted
        self.assertEqual(len(test_ModuleD.deleteData(test_data, delete_index, test_filename)), 1)
        
        
        # assert list has remaining element left (also need to re-initialize test_data list)
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        self.assertEqual(test_ModuleD.deleteData(test_data, delete_index, test_filename)[0].name, test_name)
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        self.assertEqual(test_ModuleD.deleteData(test_data, delete_index, test_filename)[0].number, test_num)
        
        
if __name__ == '__main__':
    unittest.main()
    
