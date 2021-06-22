import unittest
import AddNum


class TestAddNum(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(AddNum.add(10,5),15)
    self.assertEqual(AddNum.add(10,10),20)
    self.assertEqual(AddNum.add(10,25),35)
    self.assertEqual(AddNum.add(10,50),60)
    
    
    
if __name__ == '__main__':
    unittest.main()
