import unittest
from modules.ModuleE import ModuleE


class TestE(unittest.TestCase):

    def test_exitProgram_method(self):

        with self.assertRaises(SystemExit):
            # call exitProgram method
            ModuleE.exitProgram(self)


if __name__ == '__main__':
    unittest.main()
    
