import unittest
from modules.ModuleB import ModuleB
from unittest.mock import Mock
from unittest.mock import patch

# no need to test FileNotFOundError in Module B as this would require student to intentionally change
# a files permission to be not readable by current user

# setter method not tested as it is not required, Use "Whats the pythonic way to use getters and setters" stack overflow guide
# to assist in calling setter method w/ mocks IF you want to test


class TestB(unittest.TestCase):

    def test_loadFile_read_data(self):
        # create instance of Module B w/ mock Mod. F obj
        mock_ModuleF = Mock()
        test_ModuleB = ModuleB(mock_ModuleF)
        
        # create test .txt file with data
        test_file = "test_data.txt"
        
        test_name1 = "test_name"
        test_name2 = "another_test_name"
        test_number1 = "1234"
        test_number2 = "54321"
        
        test_data1 = "test_name,1234\n"
        test_data2 = "another_test_name,54321"
        
        with open(test_file, 'w') as f:
            f.write(test_data1)
            f.write(test_data2)
    
        # this method call returns data [], should be an arr of two entry objects
        test_ModuleB.loadFile(test_file)    	
    
        self.assertEqual(test_ModuleB.loadFile(test_file)[0].name, test_name1)
        self.assertEqual(test_ModuleB.loadFile(test_file)[0].number, test_number1)
        self.assertEqual(test_ModuleB.loadFile(test_file)[1].name, test_name2)
        self.assertEqual(test_ModuleB.loadFile(test_file)[1].number, test_number2)
    
    @patch.object(ModuleB, "loadFile")
    def test_loadFile_IOError(self, mock_loadFile):
        
        # call to mock method
        mock_loadFile("test_non_existent_file")
    
        # assertion statements
        mock_loadFile.assert_called()
        mock_loadFile.assert_called_with("test_non_existent_file")

    def test_getter_f(self):
        # create instance of Module B w/ mock Mod. F obj
        mock_ModuleF = Mock()
        test_ModuleB = ModuleB(mock_ModuleF)
        
        # assert that getter method retrieves mock Mod. F obj
        self.assertEqual(test_ModuleB.f, mock_ModuleF)


if __name__ == '__main__':
    unittest.main()
    
