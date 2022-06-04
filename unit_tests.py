import unittest
import subFiles.input_functions as IFC
from subFiles.classes import *
from subFiles.right_angle import *


class TestTextFunctions(unittest.TestCase):
    def test_index_input(self):
        self.assertEqual(IFC.clean_int_input(" 1"), "1")
        self.assertEqual(IFC.clean_int_input("asd;lk"), "")
        self.assertEqual(IFC.clean_int_input("7\n"), "7")
    def test_test(self):
        self.assertEqual(1,1)


if __name__ == "__main__":
    print("testing")
    unittest.main()
