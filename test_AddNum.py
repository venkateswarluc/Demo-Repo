import unittest
import calc


class TestAddNum(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(calc.add(10,5),15)
    self.assertEqual(calc.add(10,10),20)
    self.assertEqual(calc.add(10,25),35)
    self.assertEqual(calc.add(10,50),60)
    
    
    
if __name__ == '__main__':
    unittest.main()
