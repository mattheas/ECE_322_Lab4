import unittest
from modules.ModuleB import ModuleB
from unittest.mock import Mock

# no need to test FileNotFOundError in Module B as this would require student to intentionally change
# a files permission to be not readable by current user

class TestB(unittest.TestCase):

    def test_loadFile_method(self):
        print("ello govna")

    def test_setter_f(self):
        # create instance of Module B w/ mock Mod. F obj
        mock_ModuleF = Mock()
        test_ModuleB = ModuleB(mock_ModuleF)
        
        # assert that getter method retrieves mock Mod. F obj
        self.assertEqual(test_ModuleB.f, mock_ModuleF)
        
        # use setter method
        new_mock_ModuleF = Mock()
        test_ModuleB.f(new_mock_ModuleF)
        
        # assert method updated attribute
        self.assertEqual(test_ModuleB.f, new_mock_ModuleF)
        
        
    def test_getter_f(self):
        # create instance of Module B w/ mock Mod. F obj
        mock_ModuleF = Mock()
        test_ModuleB = ModuleB(mock_ModuleF)
        
        # assert that getter method retrieves mock Mod. F obj
        self.assertEqual(test_ModuleB.f, mock_ModuleF)


if __name__ == '__main__':
    unittest.main()
    
