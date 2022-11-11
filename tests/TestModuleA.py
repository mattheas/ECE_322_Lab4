import unittest
from modules.ModuleA import ModuleA
from unittest.mock import Mock

class TestA(unittest.TestCase):

    def test_parseDelete_method(self):
        # create instance of Module A w/ mock obj's for parameters
        mock_ModuleB = Mock()
        mock_ModuleC = Mock()
        mock_ModuleD = Mock()
        mock_ModuleE = Mock()
        test_ModuleA = ModuleA(mock_ModuleB, mock_ModuleC, mock_ModuleD, mock_ModuleE)
        
        test_filename = "test_file_ModuleA.txt"
        test_data = []
        test_ModuleA.filename = test_filename
        test_ModuleA.data = test_data
        
        # assertion statement, method returns true because d is a mocked obj, so the method call just returns a 
        # mock obj, meaning self._data != None
        index_to_del = 2
        self.assertTrue(test_ModuleA.parseDelete(index_to_del))
        
        
    def test_displayHelp_method(self):
        # create instance of Module A w/ mock obj's for parameters
        mock_ModuleB = Mock()
        mock_ModuleC = Mock()
        mock_ModuleD = Mock()
        mock_ModuleE = Mock()
        test_ModuleA = ModuleA(mock_ModuleB, mock_ModuleC, mock_ModuleD, mock_ModuleE)
        
        # assertion
        self.assertTrue(test_ModuleA.displayHelp())
        
        
    def test_parseLoad_method(self):
        # create instance of Module A w/ mock obj's for parameters
        mock_ModuleB = Mock()
        mock_ModuleC = Mock()
        mock_ModuleD = Mock()
        mock_ModuleE = Mock()
        test_ModuleA = ModuleA(mock_ModuleB, mock_ModuleC, mock_ModuleD, mock_ModuleE)
        
        test_filename = "test_file_ModuleA.txt"
        test_data = []
        test_ModuleA.data = test_data
        
        # assertion statement, method returns true because b is a mocked obj, so the method call just returns a 
        # mock obj, meaning self._data != None
        self.assertTrue(test_ModuleA.parseLoad(test_filename))
        
        
    def test_parseAdd_method(self):
        # create instance of Module A w/ mock obj's for parameters
        mock_ModuleB = Mock()
        mock_ModuleC = Mock()
        mock_ModuleD = Mock()
        mock_ModuleE = Mock()
        test_ModuleA = ModuleA(mock_ModuleB, mock_ModuleC, mock_ModuleD, mock_ModuleE)
        
        test_filename = "test_file_ModuleA.txt"
        test_data = []
        test_ModuleA.filename = test_filename
        test_ModuleA.data = test_data
        
        test_name = "Bobby"
        test_number = "42349"
        
        # assertion statement, method returns true because d is a mocked obj, so the method call just returns a 
        # mock obj, meaning self._data != None
        self.assertTrue(test_ModuleA.parseAdd(test_name, test_number))
        
        

if __name__ == '__main__':
    unittest.main()
    
