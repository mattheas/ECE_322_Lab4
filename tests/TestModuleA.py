import unittest
from modules.ModuleA import ModuleA
from unittest.mock import Mock

class TestA(unittest.TestCase):

    def setUp(self):
        # create instance of Module A w/ mock obj's for parameters
        self.mock_ModuleB = Mock()
        self.mock_ModuleC = Mock()
        self.mock_ModuleD = Mock()
        self.mock_ModuleE = Mock()
        self.test_ModuleA = ModuleA(self.mock_ModuleB, self.mock_ModuleC, self.mock_ModuleD, self.mock_ModuleE)


    def test_parseDelete_method(self):
        
        test_filename = "test_file_ModuleA.txt"
        test_data = []
        self.test_ModuleA.filename = test_filename
        self.test_ModuleA.data = test_data
        index_to_del = 2
        
        # mock return value of deleteData method to return empty list
        self.mock_ModuleD.deleteData.return_value = []
        self.assertTrue(self.test_ModuleA.parseDelete(index_to_del))
        
        # mock return value of deleteData method to return None
        self.mock_ModuleD.deleteData.return_value = None
        self.assertFalse(self.test_ModuleA.parseDelete(index_to_del))
        
        
    def test_displayHelp_method(self):
        
        # mock the method??
        
        # assertion
        self.assertTrue(self.test_ModuleA.displayHelp())
        
        
    def test_parseLoad_method(self):
        
        test_filename = "test_file_ModuleA.txt"
        test_data = []
        self.test_ModuleA.data = test_data
        
        # mock return value of loadFile method to return empty list
        self.mock_ModuleB.loadFile.return_value = []
        self.assertTrue(self.test_ModuleA.parseLoad(test_filename))
        
        # mock return value of loadFile method to return None
        self.mock_ModuleB.loadFile.return_value = None
        self.assertFalse(self.test_ModuleA.parseLoad(test_filename))
        
        
    def test_parseAdd_method(self):
        
        test_filename = "test_file_ModuleA.txt"
        test_data = []
        self.test_ModuleA.filename = test_filename
        self.test_ModuleA.data = test_data
        
        test_name = "Bobby"
        test_number = "42349"
        
        # assertion statement, method returns true because d is a mocked obj, so the method call just returns a 
        # mock obj, meaning self._data != None
        self.assertTrue(self.test_ModuleA.parseAdd(test_name, test_number))
        
        

if __name__ == '__main__':
    unittest.main()
    
