import unittest
from modules.ModuleF import ModuleF
from unittest.mock import patch


### change code
# F has no stubs, i.e no objects to mock
# the "driver" is basically the unit test


class TestF(unittest.TestCase):
    
    @patch.object(ModuleF, "displayData")
    def test_displayData_method(self, mock_displayData):
    
    	print("mock displayData test")
    	
    	# call to mock method
    	mock_displayData("some data")
    	
    	# assertion statements
    	mock_displayData.assert_called()
    	mock_displayData.assert_called_with("some data")
       


if __name__ == '__main__':
    unittest.main()
