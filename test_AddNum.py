import unittest
import AddNum


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(AddNum.add(10, 5), 15)
        self.assertEqual(AddNum.add(-1, 1), 0)
        self.assertEqual(AddNum.add(-1, -1), -2)
    
    
    
    
if __name__ == '__main__':
    unittest.main()
