import unittest
import AddNum


class TestAddNum(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(AddNum.sum(10,30))
    
    
    
    
if __name__ == '__main__':
    unittest.main()
