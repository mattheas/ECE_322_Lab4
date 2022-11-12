import unittest
from modules.ModuleA import ModuleA
from unittest.mock import Mock
from unittest.mock import patch
from data.Entry import Entry


class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.mock_ModuleB = Mock()
        self.mock_ModuleC = Mock()
        self.mock_ModuleD = Mock()
        self.mock_ModuleE = Mock()
        self.test_ModuleA = ModuleA(self.mock_ModuleB, self.mock_ModuleC, self.mock_ModuleD, self.mock_ModuleE)
        
        self.test_filename = "test_file_ModuleA.txt"


    def test_parseDelete_method(self):
        
        test_data = []
        self.test_ModuleA.filename = self.test_filename
        self.test_ModuleA.data = test_data
        index_to_del = 2
        
        # mock return value of deleteData method to return empty list
        self.mock_ModuleD.deleteData.return_value = []
        self.assertTrue(self.test_ModuleA.parseDelete(index_to_del))
        self.mock_ModuleD.deleteData.assert_called_with(test_data, index_to_del, self.test_filename)
        
        # mock return value of deleteData method to return None
        self.mock_ModuleD.deleteData.return_value = None
        self.assertFalse(self.test_ModuleA.parseDelete(index_to_del))
        self.mock_ModuleD.deleteData.assert_called_with(test_data, index_to_del, self.test_filename)
        
        
    @patch.object(ModuleA, "displayHelp")
    def test_displayHelp_method(self, mock_displayHelp):
        
        # call to mock method
        mock_displayHelp()
        
        # assertion statements
        mock_displayHelp.assert_called()
        self.assertTrue(self.test_ModuleA.displayHelp())
        
        
    def test_parseLoad_method(self):
        
        test_data = []
        self.test_ModuleA.data = test_data
        
        # mock return value of loadFile method to return empty list
        self.mock_ModuleB.loadFile.return_value = []
        self.assertTrue(self.test_ModuleA.parseLoad(self.test_filename))
        
        # mock return value of loadFile method to return None
        self.mock_ModuleB.loadFile.return_value = None
        self.assertFalse(self.test_ModuleA.parseLoad(self.test_filename))
        
        
    def test_parseAdd_method(self):
        
        test_data = []
        self.test_ModuleA.filename = self.test_filename
        self.test_ModuleA.data = test_data
        
        test_name = "Bobby"
        test_number = "42349"
        
        # mock return value of insertData method to return empty list
        self.mock_ModuleD.insertData.return_value = []
        self.assertTrue(self.test_ModuleA.parseAdd(test_name, test_number))
        
        # mock return value of insertData method to return None
        self.mock_ModuleD.insertData.return_value = None
        self.assertFalse(self.test_ModuleA.parseAdd(test_name, test_number))
        
        
    def test_runSort_method(self):
    
        # mock return value of sortData method to return empty list
        self.mock_ModuleC.sortData.return_value = []
        self.assertTrue(self.test_ModuleA.runSort())
        
        # mock return value of sortData method to return None
        self.mock_ModuleC.sortData.return_value = None
        self.assertFalse(self.test_ModuleA.runSort())
        
        
    def test_parseUpdate_method(self):
        # populate test data array
        test_name = "Manny"
        test_name1 = "Hanny"
        test_num = "87635"
        test_num1 = "96453"
        test_data = [Entry(test_name,test_num), Entry(test_name1,test_num1)]
        
        test_new_name = "Not Hanny"
        test_new_number = "123693"
        index_to_update = 1
        
        # mock return value of updateData method to return updated list with new person/ num at index 1
        self.mock_ModuleD.updateData.return_value = [Entry(test_name,test_num), Entry(test_new_name,test_new_number)]
        self.assertTrue(self.test_ModuleA.parseUpdate(index_to_update, test_new_name, test_new_number))
        self.mock_ModuleD.updateData.assert_called_with(index_to_update, test_new_name, test_new_number, self.test_filename)
        
        # mock return value of updateData method to return None
        self.mock_ModuleD.updateData.return_value = None
        self.assertFalse(self.test_ModuleA.parseUpdate(index_to_update, test_new_name, test_new_number))
        self.mock_ModuleD.updateData.assert_called_with(index_to_update, test_new_name, test_new_number, self.test_filename)
      
      
    def test_runExit_method(self):
        try:
            self.test_ModuleA.runExit()
        except:
            self.mock_ModuleE.exitProgram.assert_called_once()
    
    
    @patch.object(ModuleA, "run")
    def test_run_NO_command_given_method(self, mock_run):
        
        # call to mock method
        mock_run()
        
        # assertion statements
        mock_run.assert_called_with()
        mock_run.assert_called_once()
        
        
    def test_run_command_given_method(self):
        print("test")
    
        
if __name__ == '__main__':
    unittest.main()
    
