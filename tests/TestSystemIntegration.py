import unittest
from modules.ModuleA import ModuleA
from modules.ModuleB import ModuleB
from modules.ModuleC import ModuleC
from modules.ModuleD import ModuleD
from modules.ModuleE import ModuleE
from modules.ModuleF import ModuleF
from modules.ModuleG import ModuleG
from unittest.mock import patch
from data.Entry import Entry


class TestSystemIntegration(unittest.TestCase):

    def setUp(self):
        # create system
        self.F = ModuleF()
        self.G = ModuleG()
        self.A = ModuleA(ModuleB(self.F), ModuleC(self.F), ModuleD(self.F, self.G), ModuleE())
        self.filename = "data.txt"


    @patch.object(ModuleA, "run")
    def test_system_no_command(self, mock_run):
        # call to mock method
        mock_run()
    
        # assertion statements
        mock_run.assert_called()
        mock_run.assert_called_with()
        
        self.A.run()
        
        
    @patch.object(ModuleA, "run")
    def test_system_help_command(self, mock_run):
        # call to mock method
        mock_run("help")
    
        # assertion statements
        mock_run.assert_called()
        mock_run.assert_called_with("help")
        
        self.A.run("help")
        
        
    def test_system_load_command(self):
        # load database into program
        self.A.run("load",self.filename)
    
        # assert database is in program as expected
        count = 0
        with open(self.filename) as fp:
            Lines = fp.readlines()
            for line in Lines:
                count += 1
                values=line.strip().split(",")
                if (len(values) == 2):
                    self.assertEqual(self.A.data[count-1].name, values[0])
                    self.assertEqual(self.A.data[count-1].number, values[1])
        
        
    def test_system_add_command(self):
        self.A.run( "add","Ahmed","477848")
        
        # assert database is updated
        count = 0
        with open(self.filename) as fp:
            Lines = fp.readlines()
            for line in Lines:
                count += 1
                values=line.strip().split(",")
                if (len(values) == 2):
                    self.assertEqual(self.A.data[count-1].name, values[0])
                    self.assertEqual(self.A.data[count-1].number, values[1])
        

if __name__ == '__main__':
    unittest.main()
    
